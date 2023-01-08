#External Imports
import customtkinter as ctk
import os
from PIL import Image, ImageTk
import os


#Inbuilt Imports
from available_menus_frame import AvailableMenuFrames
from toggle_frames.DownloadVideoFrame.home_content_frame import ContentFrame
from toggle_frames.SettingsFrame.setting_frame import SettingsFrame

current_directory = os.getcwd()
files_and_folders = os.listdir(current_directory)

if "downloaded_videos" in files_and_folders:
    pass

else:
    os.mkdir("downloaded_videos")


class MainApp:

    def __init__(self):

        #============ Main Window ============

        self.root = ctk.CTk()
        self.root.geometry("800x480")

        
        #============ Main Window Configurations ============

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.main_font = ('Segoe UI Black', 10)


        #============ Options Frame ============
        # In self.root at 1st row and 1st column
        
        self.option_frame = AvailableMenuFrames(self.root, self.main_font)



        #============ Content/Results Frame ============
        # In self.root at 1st row and 2nd column

        self.content_frame = ContentFrame(self.root, self.main_font)



        ##============ Settings Frame ============

        self.settings_frame = SettingsFrame(self.root)




        self.root.mainloop()




app = MainApp()