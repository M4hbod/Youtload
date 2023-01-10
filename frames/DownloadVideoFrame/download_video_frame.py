import customtkinter as ctk
import wget
from PIL import Image
from core.functions import json, directory
from core.functions import VideoFunctions

JSON_FILE_PATH = "frames/SettingsFrame/configs.json"

class VideoInfoFrame():

    def __init__(self, master = None, font = ('Segoe UI Black', 10)):
        
        # Settings Frame
        self.sex_frames = ctk.CTkFrame(master)
        self.sex_frames.grid(row=0, column=1, padx=7, pady=7, sticky='nswe')
        self.sex_frames.grid_columnconfigure(0, weight=0)
        self.sex_frames.grid_forget() 
            
        self.youtube = VideoFunctions()
        self.database = json.getJSON(JSON_FILE_PATH)
        self.path = self.database['path']
        if self.path == "":
            self.path = f"{directory.get_current_directory()}\Download".replace("\\", "/")
            
        self.search_data_function = lambda: self.youtube.thread_function(self.show_info, (self.url_entry.get(), ))
        self.download_video_function = lambda: self.youtube.thread_function(self.youtube.download_video, (self.url_entry.get(), self.path, self.progress_function))
        
        # ==== Video Url Frame ====
        self.video_url_frame = ctk.CTkFrame(self.sex_frames)
        self.video_url_frame.grid(row=0, padx=20, pady=20)
        
        # Search Bar
        self.entry_value = ctk.StringVar(self.sex_frames)
        self.url_entry = ctk.CTkEntry(self.video_url_frame, width=535, placeholder_text="Video Url...", textvariable = self.entry_value, font=font)
        self.url_entry.grid(row=0, column=0, padx=5, pady=5)
        
        # Search Button
        self.search_video_button = ctk.CTkButton(self.video_url_frame, text="Search", width=50, font=font, command=self.search_data_function)
        self.search_video_button.grid(row=0, column=1, padx=5, pady=5)
        
        # ==== Thumbnail Frame ==== 
        self.thumbnail_frame = ctk.CTkFrame(self.sex_frames)
        self.thumbnail_frame.grid(row=1, sticky='nswe', padx=20, pady=5)
        self.thumbnail_frame.grid_columnconfigure(3, weight=1)
        
        # Video Thumbnail
        self.thumbnail = ctk.CTkImage(Image.open(r"assets\Images\Logo.png"), size=(564, 247))
        self.thumbnail_label = ctk.CTkLabel(self.thumbnail_frame, text="", image=self.thumbnail, anchor='center')
        self.thumbnail_label.pack(pady=10)

        # ==== Info Frame ====
        self.info_frame = ctk.CTkFrame(self.sex_frames)
        self.info_frame.grid(row=2, sticky='nswe', padx=20, pady=5)
        self.info_frame.grid_columnconfigure(1, weight=1)
        self.info_frame.grid_rowconfigure(5, weight=2)

        # Video Title
        self.title_label = ctk.CTkLabel(self.info_frame, text="Title: ", font=font)
        self.title_label.grid(row=1, column=0, padx=10, pady=2.5, sticky='w')

        self.title = ctk.CTkLabel(self.info_frame, text="--", font=font)
        self.title.grid(row=1, column=1, padx=2.5, pady=2.5)

        # Video Duration
        self.duration_label = ctk.CTkLabel(self.info_frame, text="Duration: ", font=font)
        self.duration_label.grid(row=2, column=0, padx=10, pady=2.5, sticky='w')

        self.duration = ctk.CTkLabel(self.info_frame, text="--", font=font)
        self.duration.grid(row=2, column=1, padx=2.5, pady=2.5)
        
        # Video Views
        self.views_label = ctk.CTkLabel(self.info_frame, text="Views: ", font=font)
        self.views_label.grid(row=3, column=0, padx=10, pady=2.5, sticky='w')

        self.views = ctk.CTkLabel(self.info_frame, text="--", font=font)
        self.views.grid(row=3, column=1, padx=2.5, pady=2.5)

        # Video Download Size
        self.filesize_label = ctk.CTkLabel(self.info_frame, text="Download Size: ", font=font)
        self.filesize_label.grid(row=4, column=0, padx=10, pady=2.5, sticky='w')

        self.filesize = ctk.CTkLabel(self.info_frame, text="--", font=font)
        self.filesize.grid(row=4, column=1, padx=2.5, pady=2.5)
        
        # ==== Download Progress Frame ====
        self.download_progress_frame = ctk.CTkFrame(self.sex_frames)
        self.download_progress_frame.grid(row=3, padx=20, pady=5, sticky='nswe')
        self.info_frame.grid_columnconfigure(1, weight=1)
        self.info_frame.grid_rowconfigure(5, weight=2)
        
        # Download Progress
        self.download_label = ctk.CTkLabel(self.download_progress_frame, text="Downloading...", font=font)
        self.download_label.grid(row=0, column=0, padx=10, pady=2.5, sticky="W")
        
        self.downloaded_percentage_label = ctk.CTkLabel(self.download_progress_frame, text="", font=font)
        self.downloaded_percentage_label.grid(row=0, column=1, padx=(50, 160), pady=2.5)
        
        self.download_button = ctk.CTkButton(self.download_progress_frame, text="Download Now", width=50, font=font, command=self.download_video_function)
        self.download_button.grid(row=0, column=2, padx=5, pady=5)


    # Process Video Info
    def show_info(self, url):
        try:
            data_found = self.youtube.get_all_data(url)

            file_size = f"{str(data_found['size'])} {data_found['size_type']}"
            
            thumbnail = wget.download(data_found['thumbnail-url'], "temp/thumbnail.png", bar=None)
            thumbnail = Image.open(thumbnail)
            ratio = thumbnail.size[0] / 300
            self.thumbnail = ctk.CTkImage(thumbnail, size=(thumbnail.size[0] / ratio, thumbnail.size[1] / ratio))
            self.thumbnail_label.configure(self.info_frame, text="", image=self.thumbnail)
            
            self.update_info(data_found['title'], data_found['duration'], file_size, data_found['views'])

        except Exception as e:
            print(e)
            self.update_info("Error!", "Error!", "Error!", "Error!")

    # Update Video Info
    def update_info(self, title, duration, file_size, views):
        self.title.configure(text=title)
        self.duration.configure(text=duration)
        self.filesize.configure(text=file_size)
        self.views.configure(text=str(views))

    # Progress Update
    def progress_function(self, stream, chunk, bytes_remaining):
        video_size = self.youtube.fromBytes(stream.filesize) #Size of the video in prettified Format(from bytes to KB, MB, etc.)
        video_size_type = self.youtube.prettifyBytes(video_size) #Video size format KB, MB, etc.
        bytes_remaining = stream.filesize - bytes_remaining #Remaining download size
        percentage = self.youtube.toPercentage(stream.filesize, bytes_remaining) #Percentage of video downloaded
        progress_text = f"{percentage}% of {video_size} {video_size_type}" #Text for configuring to the percentage label
        self.downloaded_percentage_label.configure(text=progress_text)

        if percentage==100.0:
            self.download_label.configure(text="Completed!")
            
    #============ Attributes/core.functions ============

    #showFrame Function -> To show the frame by unforgetting the grid
    def showFrame(self):
        self.sex_frames.grid(row=0, column=1, padx=7, pady=7, sticky='nswe')

    #hideFrame Function -> Ofc, the vise versa of showFrame function
    def hideFrame(self):
        self.sex_frames.grid_forget()
