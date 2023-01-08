import json

import customtkinter as ctk
from tkinter import messagebox

from core.functions import directory

JSON_FILE_PATH = "frames/SettingsFrame/configs.json"

class SettingsFrame:


    #============ Initialization ============
    def __init__(self, master = None, font = ('Segoe UI Black', 10)):

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.grid(row=0, column=0, padx=7, pady=7, sticky='nswe')
        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_forget() 

        self.database = self.getJSON(JSON_FILE_PATH)

        self.video_download_path = self.database['path']
        self.mode = self.database['mode']
        self.theme = self.database['theme']
        
        if self.video_download_path == "":
            self.video_download_path = f"{directory.get_current_directory()}\Download".replace("\\", "/")
        if self.mode == "":
            self.mode = "Dark"
        if self.theme == "":
            self.theme = "Blue"
        
        
        ctk.set_appearance_mode(self.mode)
        ctk.set_default_color_theme(self.theme.lower())



        #============ Widgets ============

        self.options_frame = ctk.CTkFrame(self.main_frame)
        self.options_frame.grid(row=0, sticky='nswe', padx=20, pady=(20,5))

        #============ Inside path_frame ============


        # Path Label

        self.path_label = ctk.CTkLabel(self.options_frame, text="Path: ", font=font, width=50)
        self.path_label.grid(row=0, column=0)


        # Path Entry -> path for downloading videos

        self.path_entry = ctk.CTkEntry(self.options_frame, font=font, width=470)
        self.path_entry.grid(row=0, column=1, padx=5, pady=5)
        self.path_entry.insert(0, self.video_download_path)
        


        # Browse Button -> for choosing a path

        self.path_button = ctk.CTkButton(self.options_frame, text="Browse", font=font, width=60, command=self.setPath)
        self.path_button.grid(row=0, column=2, padx=5, pady=5)


        # Appearamce Frame
        self.appearance_frame = ctk.CTkFrame(self.main_frame)
        self.appearance_frame.grid(row=1, sticky='nswe', padx=20, pady=5)
        
        # Appearance Mode Label
        self.appearance_mode_label = ctk.CTkLabel(self.appearance_frame, text="Mode:", font=font, width=50)
        self.appearance_mode_label.grid(row=1, column=0, padx=10, pady=(10, 10))
        
        # Appearance Mode OptionMenu -> Light, Dark, System
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.appearance_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=1, column=1, padx=30, pady=(10, 10))
        
        # Theme Label
        self.appearance_theme_label = ctk.CTkLabel(self.appearance_frame, text="Theme:", font=font, width=50)
        self.appearance_theme_label.grid(row=1, column=2, padx=30, pady=(10, 10))
        
        # Theme OptionMenu -> Light, Dark, System
        self.appearance_theme_optionemenu = ctk.CTkOptionMenu(self.appearance_frame, values=["Blue", "Green", "Dark-Blue"],
                                                                       command=self.change_appearance_theme_event)
        self.appearance_theme_optionemenu.grid(row=1, column=3, padx=20, pady=(10, 10))
        
        
        
        # Set Default Values
        self.appearance_mode_optionemenu.set(self.mode)
        self.appearance_theme_optionemenu.set(self.theme.title())



    #============ Attributes/core.functions ============

    #showFrame Function -> To show the frame by unforgetting the grid
    def showFrame(self):
        self.main_frame.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)


    #hideFrame Function -> Ofc, the vise versa of showFrame function
    def hideFrame(self):
        self.main_frame.grid_forget()


    #Set path Function -> Select a path for downloading the video
    def setPath(self):

        path = ctk.filedialog.askdirectory()
        if path == "":
            return
        
        self.path_entry.delete(0, ctk.END)
        self.path_entry.insert(0, str(path))
        self.video_download_path = path
        print(f"path: {self.video_download_path}")


        json_data = self.getJSON(JSON_FILE_PATH)
        if 'path' in json_data:
            del json_data['path']

            self.setJSON(JSON_FILE_PATH, "path", path)

    # Get JSON -> To get the data in the configs.json file
    def getJSON(self, filename):

        with open(filename, 'r') as data:
            all_data = json.load(data)

        return all_data

    def setJSON(self, filename, key, value):
        with open(filename, "r") as jsonFile:
            data = json.load(jsonFile)
        
        data[key] = value
        
        with open(filename, "w") as jsonFile:
            json.dump(data, jsonFile)

    # Change appearance mode event -> To change the appearance mode of the app
    def change_appearance_mode_event(self, new_appearance_mode: str):
        self.mode = new_appearance_mode
        self.setJSON(JSON_FILE_PATH, "mode", self.mode)
        ctk.set_appearance_mode(self.mode)
        
    def change_appearance_theme_event(self, new_appearance_theme: str):
        self.theme = new_appearance_theme
        self.setJSON(JSON_FILE_PATH, "theme", self.theme.lower())
        ctk.set_default_color_theme(self.theme.lower())
        messagebox.showinfo("Restart", "Please restart the app to apply the changes.")



