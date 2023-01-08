import customtkinter as ctk
from PIL import Image

from frames.DownloadVideoFrame.home_content_frame import ContentFrame


class AvailableMenuFrames():

    def __init__(self, master, text_font, tabs_font):

        
        self.options_frame = ctk.CTkFrame(master, width=150)
        self.options_frame.grid(row=0, column=0, sticky='nswe', padx=7, pady=7)
        self.options_frame.grid_rowconfigure(0, minsize=10) 
        self.image_size = 20

        self.content = ContentFrame()


        #============ icons ============  

        self.download_icon = ctk.CTkImage(Image.open(r'Icons\LightModeImages\download.png').resize((self.image_size, self.image_size), Image.NEAREST))
        self.settings_icon = ctk.CTkImage(Image.open(r'Icons\LightModeImages\settings.png').resize((self.image_size, self.image_size), Image.NEAREST))


        self.app_name = ctk.CTkLabel(self.options_frame, text="Youtload", font=tabs_font)
        self.app_name.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')


        self.download_button = ctk.CTkButton(self.options_frame, image=self.download_icon, compound='left', text="Downloads", corner_radius=15, width=40, font=text_font, command=lambda : self.content.toggleFrame("downloads"))
        self.download_button.grid(row=2, column=0, padx=5, pady=5)


        self.settings_button = ctk.CTkButton(self.options_frame, image=self.settings_icon, compound='left', text="Settings", corner_radius=15, width=40, font=text_font, command=lambda : self.content.toggleFrame("settings"))
        self.settings_button.grid(row=3, column=0, padx=5, pady=5)
       