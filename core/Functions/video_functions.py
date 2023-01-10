import datetime as dt
import threading
from typing import Literal

import pytube as tube


class VideoFunctions(tube.YouTube):

    def __init__(self):
         self.TIME_FORMAT = '%H:%M:%S'

    # To run each function in thread so the GUI doesnt get stuck
    @staticmethod
    def thread_function(function, arguments) -> None:

        function_in_thread = threading.Thread(target=function, args=arguments)

        function_in_thread.start()

    # Divides the filesize with the time taken for download
    @staticmethod
    def networkSpeed(filesize: int, time_took: int) -> int | None:
        try:
            size_in_mb = filesize/1000000
        except ZeroDivisionError:
            print("Filesize cant be zero!")
            return

        return int(size_in_mb/time_took)

    # Gets the times for the start and end the download function and subtracts them
    @staticmethod
    def timeTaken(start_time, end_time, in_seconds = True) -> list[str] | int:
        difference_in_time = str(end_time - start_time)

        time_components = difference_in_time.split(':')

        if not in_seconds:
            return time_components
        
        hours = int(time_components[0]) * 60 * 60
        minutes = int(time_components[1]) * 60
        seconds = hours + minutes + int(time_components[2])
        return hours + minutes + seconds

    # To convert seconds to hour:minute:seconds format
    @staticmethod
    def fromSeconds(sec: int) -> str:
        time_list = str(dt.timedelta(seconds=sec))
        time_list = time_list.split(":")

        modified_list = [times for times in time_list if int(times) != 0]
        return ":".join(modified_list)

    # To convert bytes to better size
    @staticmethod
    def fromBytes(bytes: int) -> float:

        return round(bytes/1000000, 1)

    # To show percentage of video downloaded
    @staticmethod
    def toPercentage(main_int, bytes) -> float:

        return round((bytes/main_int)*100, 1) 

    # To convert bytes to units(MB, GB, TB, etc.)
    def prettifyBytes(self, bytes: int) -> Literal['KB', 'MB', 'GB']:

        if bytes < 1:
            return "KB"

        elif bytes < 1000:
           return "MB"

        else:
            return "GB"

    # For creating a time object at start and end of the download function
    def createTime(self):
        _time = dt.datetime.now()

        time_string = _time.strftime(self.TIME_FORMAT)
        return dt.datetime.strptime(time_string, self.TIME_FORMAT)

    # For getting the video data
    def get_data(self, url) -> dict:
        data_dict = {}

        video = tube.YouTube(url)

        data_dict['title'] = video.title
        data_dict['duration'] = self.fromSeconds(video.length)
        data_dict['views'] = video.views
        data_dict['size'] = self.fromBytes(video.streams.get_highest_resolution().filesize_approx)
        data_dict['size_type'] = self.prettifyBytes(data_dict['size'])
        data_dict['thumbnail-url'] = video.thumbnail_url
        data_dict['available_resolutions'] = video.streams.filter(progressive=True)

        print(data_dict)

        return data_dict

    def download_video(self, url, path_for_download = None, progress_func = None) -> tuple:
        started_on = self.createTime()
        yt_object = tube.YouTube(url=url, on_progress_callback=progress_func)

        video = yt_object.streams.get_highest_resolution()
        video.download(output_path=path_for_download)

        ended_on = self.createTime()
        time_taken = self.timeTaken(started_on, ended_on)

        download_speed = round(self.networkSpeed(video.filesize, time_taken), 4)
        
        return time_taken, download_speed
    
    def get_playlist(self, url):
        return tube.Playlist(url)