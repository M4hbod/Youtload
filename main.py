import customtkinter as ctk

from main_frames import AvailableMenuFrames
from core.functions import directory
from frames.SettingsFrame.setting_frame import SettingsFrame
from frames.DownloadVideoFrame.download_video_frame import VideoInfoFrame

current_directory = directory.get_current_directory()
files_and_folders = directory.get_files_and_folders(current_directory)

if not directory.check_if_directory_exists('temp'):
    directory.create_directory('temp')

class MainApp:

    def __init__(self):

        #============ Main Window ============

        self.root = ctk.CTk()
        self.root.title("Youtload")
        self.root.geometry("800x580")
        self.root.minsize(800, 580)

        
        #============ Main Window Configurations ============

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.main_font = ('Segoe UI Black', 11)
        self.big_font = ('Segoe UI Black', 15)


        #============ Options Frame ============
        # In self.root at 1st row and 1st column
        
        self.option_frame = AvailableMenuFrames(self.root, self.main_font, self.big_font)


        self.root.mainloop()




app = MainApp()