import customtkinter as ctk
from PIL import Image
import pystray

from core.functions import directory, json
from frames.DownloadVideoFrame.download_video_frame import VideoInfoFrame
from frames.SettingsFrame.setting_frame import SettingsFrame

current_directory = directory.get_current_directory()
files_and_folders = directory.get_files_and_folders(current_directory)

if not directory.check_if_directory_exists('temp'):
    directory.create_directory('temp')
else:
    directory.clear_directory('temp')

class MainApp:

    def __init__(self):
        # ==== Icon ====
        self.tray_icon = Image.open("tray.ico")

        # ==== Main Window ====
        self.root = ctk.CTk()
        self.root.title("Youtload")
        self.root.geometry("800x580")
        self.root.minsize(800, 580)
        self.root.protocol('WM_DELETE_WINDOW', self.close_app)

        # Main Window Configurations
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.text_font = ('Segoe UI Black', 11)
        self.tab_title = ('Segoe UI Black', 15)

        # ==== Options Frame ====
        self.menu_frame = ctk.CTkFrame(self.root, width=150)
        self.menu_frame.grid(row=0, column=0, sticky='nswe', padx=7, pady=7)
        self.menu_frame.grid_rowconfigure(0, minsize=10) 
        
        
        # ==== Content Frame ====
        self.content = ctk.CTkFrame(self.root)
        self.content.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_forget()
        
        # ==== Tab Frames ====
        self.video_info_frame = VideoInfoFrame(self.root)
        self.setting_frame = SettingsFrame(self.root)
        
        # ==== Icons ====
        self.icon_size = 30
        self.addurl_icon = ctk.CTkImage(Image.open(r'assets\Icons\LightModeImages\addurl.png').resize((self.icon_size, self.icon_size), Image.NEAREST))
        self.download_icon = ctk.CTkImage(Image.open(r'assets\Icons\LightModeImages\download.png').resize((self.icon_size, self.icon_size), Image.NEAREST))
        self.settings_icon = ctk.CTkImage(Image.open(r'assets\Icons\LightModeImages\settings.png').resize((self.icon_size, self.icon_size), Image.NEAREST))
        
        # self.option_frame = AvailableMenuFrames(self.root, self.main_font, self.tab_title)

        # ==== Menu ====
        # Tab Title
        self.app_name = ctk.CTkLabel(self.menu_frame, text="Youtload", font=self.tab_title)
        self.app_name.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')
        
        # Buttons
        self.addurl_button = ctk.CTkButton(self.menu_frame, image=self.addurl_icon, compound='left', text="Add Url", corner_radius=15, width=40, font=self.text_font, command=lambda: self.toggleFrame("addurl"))
        self.addurl_button.grid(row=2, column=0, padx=5, pady=5)

        self.downloads_button = ctk.CTkButton(self.menu_frame, image=self.download_icon, compound='left', text="Downloads", corner_radius=15, width=40, font=self.text_font, command=lambda: self.toggleFrame("downloads"))
        self.downloads_button.grid(row=3, column=0, padx=5, pady=5)

        self.settings_button = ctk.CTkButton(self.menu_frame, image=self.settings_icon, compound='left', text="Settings", corner_radius=15, width=40, font=self.text_font, command=lambda: self.toggleFrame("settings"))
        self.settings_button.grid(row=4, column=0, padx=5, pady=5)

        self.root.mainloop()

    def toggleFrame(self, what_to_show: str):

        if what_to_show == "settings":
            self.video_info_frame.hide_frame()
            self.setting_frame.show_frame()

        elif what_to_show == "downloads":
            self.video_info_frame.show_frame()
            self.setting_frame.hide_frame()
            
        elif what_to_show == "addurl":
            self.video_info_frame.hide_frame()
            self.setting_frame.hide_frame()
            
    def close_app(self):
        self.database = json.get_json(r"database\config.json")
        if self.database["tray"] == False:
            return self.root.destroy()
        
        self.root.withdraw()
        menu = (pystray.MenuItem('Show', self.show_app, default=True), pystray.MenuItem('Quit', self.quit_app))
        self.icon = pystray.Icon("name", self.tray_icon, "title", menu)
        self.icon.run()
        
    def show_app(self):
        self.icon.stop()
        self.root.after(0,self.root.deiconify)

    def quit_app(self):
        self.icon.stop()
        self.root.destroy()
        
app = MainApp()