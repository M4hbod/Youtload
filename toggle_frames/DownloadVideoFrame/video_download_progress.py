import tkinter as tk
import customtkinter as ctk
from ..Functions import video_functions as vf


#============ DownloadProgressFrame ============
class DownloadProgressFrame:

    def __init__(self, master = None, font = ('Segoe UI Black', 10)):
        
    #============ main frame configurations ============

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nswe")


    #============ Objects ============

        self.function_manager = vf.VideoFunctions()


    #============ inside mainframe ============


        #download label -> for showing 'Downloading...'

        self.download_label = ctk.CTkLabel(self.main_frame, text="Downloading...", text_font=font)
        self.download_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")


        #dwonload percentage label -> for showing how much video is downloaded

        self.downloaded_percentage_label = ctk.CTkLabel(self.main_frame, text="--", text_font=font)
        self.downloaded_percentage_label.grid(row=0, column=1, padx=10, pady=10, sticky="W")



#============ Attributes/Functions ============

    #mainProgressFunction -> For updating the download info

    def mainProgressFunction(self, stream, chunk, bytes_remaining):

        video_size = self.function_manager.fromBytes(stream.filesize) #Size of the video in prettified Format(from bytes to KB, MB, etc.)

        video_size_type = self.function_manager.prettifyBytes(video_size) #Video size format KB, MB, etc.

        bytes_remaining = stream.filesize - bytes_remaining #Remaining download size

        percentage = self.function_manager.toPercentage(stream.filesize, bytes_remaining) #Percentage of video downloaded

        progress_text = f"{percentage}% of {video_size} {video_size_type}" #Text for configuring to the percentage label

        self.downloaded_percentage_label.configure(text=progress_text)

        if percentage==100.0:
            self.download_label.configure(text="Completed!")



        


        

