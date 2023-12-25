from core.functions import json
import customtkinter as ctk
from core.functions import directory
from core.functions.video_functions import VideoFunctions
import re
from PIL import Image
import wget


class AddUrlFrame:
    def __init__(self, master=None, font=("Segoe UI Black", 10)):
        self.youtube = VideoFunctions()

        # ==== Add Url Frame ====
        self.addurl_frame = ctk.CTkScrollableFrame(master, width=100, height=100)
        self.addurl_frame.grid(row=0, column=1, padx=7, pady=7, sticky="nswe")
        self.addurl_frame.grid_columnconfigure(0, weight=0)
        self.addurl_frame.grid_forget()

        self.font = font
        self.video_index = 1

        # ==== Video Url Frame ====
        self.search_data = lambda: self.youtube.thread_function(
            self.process_url, (self.url_entry.get(),)
        )

        self.video_url_frame = ctk.CTkFrame(self.addurl_frame)
        self.video_url_frame.grid(row=0, padx=20, pady=20)
        self.video_url_frame.grid_columnconfigure((0, 1, 3), weight=1)

        # Search Bar
        self.entry_value = ctk.StringVar(self.addurl_frame)
        self.url_entry = ctk.CTkEntry(
            self.video_url_frame,
            width=535,
            placeholder_text="Video Url...",
            textvariable=self.entry_value,
            font=self.font,
        )
        self.url_entry.grid(row=0, column=0, padx=5, pady=5)

        # Search Button
        self.search_video_button = ctk.CTkButton(
            self.video_url_frame,
            text="Search",
            width=50,
            font=self.font,
            command=self.search_data,
        )
        self.search_video_button.grid(row=0, column=1, padx=5, pady=5)

    def process_url(self, url):
        if "list=" in url:
            videos = self.youtube.get_playlist(url)
            for video in videos:
                video_info = self.youtube.get_data(video)
                self.add_video(video_info["thumbnail-url"], video_info["title"])

    def add_video(self, thumbnail, title, qualities):
        exec(
            f"thumbnail{self.video_index} = wget.download('{thumbnail}', out=directory.get_current_directory() + '/temp/thumbnail{self.video_index}.jpg', bar=None)"
        )
        exec(
            f"thumbnail{self.video_index} = ctk.CTkImage(Image.open(thumbnail{self.video_index}), size=(50, 20))"
        )

        exec(
            f"self.video_frame{self.video_index} = ctk.CTkFrame(self.addurl_frame, width=610, height = 40)"
        )
        exec(
            f"self.video_frame{self.video_index}.grid(row={self.video_index}, padx=20, pady=5, sticky='w')"
        )
        exec(f"self.video_frame{self.video_index}.grid_propagate(False)")

        exec(
            f"self.checkbox{self.video_index} = ctk.CTkCheckBox(self.video_frame{self.video_index}, height=2, width=2, border_width=1, text='')"
        )
        exec(f"self.checkbox{self.video_index}.grid(row=0, column=0, padx=5, pady=5)")

        qualities.insert(0, "Default")
        exec(
            f"self.combobox{self.video_index} = ctk.CTkComboBox(self.video_frame{self.video_index}, border_width=1, values=qualities, width=80, font=self.font)"
        )
        exec(f"self.combobox{self.video_index}.grid(row=0, column=1, padx=5, pady=5)")

        exec(
            f"self.thumbnail{self.video_index} = ctk.CTkLabel(self.video_frame{self.video_index}, image=thumbnail{self.video_index})"
        )
        exec(f"self.thumbnail{self.video_index}.grid(row=0, column=2, padx=5, pady=5)")

        exec(
            f"self.title{self.video_index} = ctk.CTkLabel(self.video_frame{self.video_index}, text=title, font=self.font)"
        )
        exec(
            f"self.title{self.video_index}.grid(row=0, column=3, padx=5, pady=5, sticky='w')"
        )

        self.video_index += 1

    def show_frame(self):
        self.addurl_frame.grid(row=0, column=1, padx=7, pady=7, sticky="nswe")

    def hide_frame(self):
        self.addurl_frame.grid_forget()
