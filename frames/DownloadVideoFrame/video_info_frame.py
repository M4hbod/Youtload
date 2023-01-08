import customtkinter as ctk
import wget
from PIL import Image

from core.functions import VideoFunctions

class VideoInfoFrame():

    def __init__(self, master, font):

        #============ Main Video Info Frame ============       

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.grid(row=2, sticky='nswe', padx=20, pady=5)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(5, weight=2)

        self.function_manager = VideoFunctions()

        
        #============ Thumbnail Frame ============
                
        self.thumbnail_frame = ctk.CTkFrame(master)
        self.thumbnail_frame.grid(row=1, sticky='nswe', padx=20, pady=5)
        self.thumbnail_frame.grid_columnconfigure(3, weight=1)
        
        #============ Video Thumbnail ============
        
        self.thumbnail = ctk.CTkImage(Image.open("Icons/Logo.png"), size=(300, 130))
        self.thumbnail_label = ctk.CTkLabel(self.thumbnail_frame, text="", image=self.thumbnail, anchor='center')
        self.thumbnail_label.pack(pady=10)

        #============ Video Title ============

        self.title_label = ctk.CTkLabel(self.main_frame, text="Title : ", font=font)
        self.title_label.grid(row=1, column=0, padx=10, pady=2.5, sticky='w')

        self.title = ctk.CTkLabel(self.main_frame, text="--", font=font)
        self.title.grid(row=1, column=1, padx=2.5, pady=2.5)



        #============ Video Duration ============

        self.duration_label = ctk.CTkLabel(self.main_frame, text="Duration : ", font=font)
        self.duration_label.grid(row=2, column=0, padx=10, pady=2.5, sticky='w')

        self.duration = ctk.CTkLabel(self.main_frame, text="--", font=font)
        self.duration.grid(row=2, column=1, padx=2.5, pady=2.5)



        #============ Video Views ============

        self.views_label = ctk.CTkLabel(self.main_frame, text="Views : ", font=font)
        self.views_label.grid(row=3, column=0, padx=10, pady=2.5, sticky='w')

        self.views = ctk.CTkLabel(self.main_frame, text="--", font=font)
        self.views.grid(row=3, column=1, padx=2.5, pady=2.5)



        #============ Video Download Size ============

        self.filesize_label = ctk.CTkLabel(self.main_frame, text="Download Size: ", font=font)
        self.filesize_label.grid(row=4, column=0, padx=10, pady=2.5, sticky='w')

        self.filesize = ctk.CTkLabel(self.main_frame, text="--", font=font)
        self.filesize.grid(row=4, column=1, padx=2.5, pady=2.5)






    #============ Frame core.functions ============

    def addData(self, url):

        try:
            data_found = self.function_manager.getAllData(url)

            config_text = f"{str(data_found['size'])} {data_found['size_type']}"
            thumbnail = wget.download(data_found['thumbnail-url'], "tmp/thumbnail.png", bar=None)
            thumbnail = Image.open(thumbnail)
            ratio = thumbnail.size[0] / 300
            
            print(thumbnail)
            self.thumbnail = ctk.CTkImage(thumbnail, size=(thumbnail.size[0] / ratio, thumbnail.size[1] / ratio))
            self.thumbnail_label.configure(self.main_frame, text="", image=self.thumbnail)
            self.title.configure(text=data_found['title'])
            self.duration.configure(text=data_found['duration'])
            self.filesize.configure(text=config_text)
            self.views.configure(text=str(data_found['views']))

        except Exception as e:
            print(e)
            self.title.configure(text="Error!")
            self.duration.configure(text="Error!")
            self.filesize.configure(text="Error!")
            self.views.configure(text="Error!")
