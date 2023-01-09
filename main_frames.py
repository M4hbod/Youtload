import customtkinter as ctk
from PIL import Image

from frames.SettingsFrame.setting_frame import SettingsFrame
from frames.DownloadVideoFrame.download_video_frame import VideoInfoFrame


class AvailableMenuFrames():

    def __init__(self, master, text_font, tabs_font):

        # ==== Options Frame ====
        self.options_frame = ctk.CTkFrame(master, width=150)
        self.options_frame.grid(row=0, column=0, sticky='nswe', padx=7, pady=7)
        self.options_frame.grid_rowconfigure(0, minsize=10) 
        
        # ==== Content Frame ====
        self.content = ctk.CTkFrame(master)
        self.content.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_forget()
        
        self.video_info_frame = VideoInfoFrame()
        self.setting_frame = SettingsFrame()
        
        self.image_size = 30


        # Icons
        self.addurl_icon = ctk.CTkImage(Image.open(r'Icons\LightModeImages\addurl.png').resize((self.image_size, self.image_size), Image.NEAREST))
        self.download_icon = ctk.CTkImage(Image.open(r'Icons\LightModeImages\download.png').resize((self.image_size, self.image_size), Image.NEAREST))
        self.settings_icon = ctk.CTkImage(Image.open(r'Icons\LightModeImages\settings.png').resize((self.image_size, self.image_size), Image.NEAREST))

        # App Name Label
        self.app_name = ctk.CTkLabel(self.options_frame, text="Youtload", font=tabs_font)
        self.app_name.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')

        # Menu Bottons
        self.addurl_button = ctk.CTkButton(self.options_frame, image=self.addurl_icon, compound='left', text="Add Url", corner_radius=15, width=40, font=text_font, command=lambda: self.toggleFrame("addurl"))
        self.addurl_button.grid(row=2, column=0, padx=5, pady=5)

        self.downloads_button = ctk.CTkButton(self.options_frame, image=self.download_icon, compound='left', text="Downloads", corner_radius=15, width=40, font=text_font, command=lambda: self.toggleFrame("downloads"))
        self.downloads_button.grid(row=3, column=0, padx=5, pady=5)

        self.settings_button = ctk.CTkButton(self.options_frame, image=self.settings_icon, compound='left', text="Settings", corner_radius=15, width=40, font=text_font, command=lambda: self.toggleFrame("settings"))
        self.settings_button.grid(row=4, column=0, padx=5, pady=5)
       

    def toggleFrame(self, what_to_show: str):

        if what_to_show == "settings":
            self.video_info_frame.hideFrame()
            self.setting_frame.showFrame()

        elif what_to_show == "downloads":
            self.video_info_frame.showFrame()
            self.setting_frame.hideFrame()
            
        elif what_to_show == "addurl":
            self.video_info_frame.hideFrame()
            self.setting_frame.hideFrame()