import tkinter as tk
import customtkinter as ctk
import pyperclip as clip

from ..Functions.video_functions import VideoFunctions
from .video_info_frame import VideoInfoFrame
from ..SettingsFrame.setting_frame import SettingsFrame 
from .video_download_progress import DownloadProgressFrame









#============ ContentFrame Window ============

class ContentFrame:


    #============ Init Function ============

    def __init__(self, master = None, font = ('Segoe UI Black', 10)):

        #============ ContentFrame Window ============

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_forget()
        self.is_showing = True






        #============ Objects ============

        self.function_manager = VideoFunctions()

        self.video_info_frame = VideoInfoFrame(self.main_frame, font)

        self.download_progress = DownloadProgressFrame(self.main_frame, font)

        self.setting_frame = SettingsFrame()





        #============ Main Functions ============

        self.search_data_function = lambda : self.function_manager.thread_function(self.video_info_frame.addData, (self.url_entry.get(), ))

        self.download_video_function = lambda : self.function_manager.thread_function(self.function_manager.downloadVideo, (self.url_entry.get(), self.setting_frame.video_download_path, self.download_progress.mainProgressFunction))

        # self.set_progress_bar_function = lambda : self.function_manager.thread_function(self.download_progress.mainProgressFunction, ())


        
        #============ Video Url Frame -> For Entry bar and search button ============

        self.video_url_frame = ctk.CTkFrame(self.main_frame)
        self.video_url_frame.grid(row=0, padx=20, pady=20)


        #============ Url Entry ============

        self.entry_value = tk.StringVar(self.main_frame)
        self.url_entry = ctk.CTkEntry(self.video_url_frame, width=250, placeholder_text="Video Url...", textvariable = self.entry_value, text_font=font)
        self.url_entry.grid(row=0, column=0, padx=5, pady=5)
        


        #============ Search Button ============

        self.search_video_button = ctk.CTkButton(self.video_url_frame, text="Search", width=50, text_font=font, command=self.search_data_function)
        self.search_video_button.grid(row=0, column=1, padx=5, pady=5)



        #============ Download Button ============

        self.search = ctk.CTkButton(self.main_frame, text="Download Now", width=50, text_font=font, command=self.download_video_function)
        self.search.grid(row=3, column=0, padx=5, pady=5)


    def toggleFrame(self, what_to_show : str):
        

        if what_to_show == "settings":
            self.main_frame.grid_forget()
            self.setting_frame.showFrame()

        elif what_to_show == "downloads":
            self.main_frame.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)
            self.setting_frame.hideFrame()  


    def getEntryValue(self):

        return self.entry_value.get() 


    def setEntryValue(self, text):

        self.video_url = self.url_entry.get()      

