import customtkinter as ctk
import tkinter as tk
from ..Functions import video_functions as vf
import customtkinter as ctk




class VideoInfoFrame():

    def __init__(self, master, font):

        #============ Main Video Info Frame ============       

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.grid(row=1, sticky='nswe', padx=20, pady=20)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(5, weight=2)

        self.function_manager = vf.VideoFunctions()



        #============ Video Title ============

        self.title_label = ctk.CTkLabel(self.main_frame, text="Title : ", text_font=font)
        self.title_label.grid(row=1, column=0, padx=2.5, pady=2.5, sticky='w')

        self.title = tk.Label(self.main_frame, text="--", bg="#343638", fg="white", font=font, wraplength=230)
        self.title.grid(row=1, column=1, padx=2.5, pady=2.5)



        #============ Video Duration ============

        self.duration_label = ctk.CTkLabel(self.main_frame, text="Duration : ", text_font=font)
        self.duration_label.grid(row=2, column=0, padx=2.5, pady=2.5, sticky='w')

        self.duration = tk.Label(self.main_frame, text="--", bg="#343638", fg="white", font=font, wraplength=230)
        self.duration.grid(row=2, column=1, padx=2.5, pady=2.5)



        #============ Video Views ============

        self.views_label = ctk.CTkLabel(self.main_frame, text="Views : ", text_font=font)
        self.views_label.grid(row=3, column=0, padx=2.5, pady=2.5, sticky='w')

        self.views = tk.Label(self.main_frame, text="--", bg="#343638", fg="white", font=font, wraplength=230)
        self.views.grid(row=3, column=1, padx=2.5, pady=2.5)



        #============ Video Download Size ============

        self.filesize_label = ctk.CTkLabel(self.main_frame, text="Download Size: ", text_font=font)
        self.filesize_label.grid(row=4, column=0, padx=2.5, pady=2.5, sticky='w')

        self.filesize = ctk.CTkLabel(self.main_frame, text="--", text_font=font)
        self.filesize.grid(row=4, column=1, padx=2.5, pady=2.5)






    #============ Frame Functions ============

    def addData(self, url):

        try:
            data_found = self.function_manager.getAllData(url)

            config_text = f"{str(data_found['size'])} {data_found['size_type']}"
            self.title.config(text=data_found['title'])
            self.duration.config(text=data_found['duration'])
            self.filesize.config(text=config_text)
            self.views.config(text=str(data_found['views']))

        except:
            self.title.config(text="Error!")
            self.duration.config(text="Error!")
            self.filesize.config(text="Error!")
            self.views.config(text="Error!")








        