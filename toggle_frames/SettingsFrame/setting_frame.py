from doctest import master
import tkinter as tk
import customtkinter as ctk
import tkinter.filedialog as filedialog
import json
import os



JSON_FILE_PATH = "toggle_frames\SettingsFrame\configs.json"

class SettingsFrame:


    #============ Initialization ============
    def __init__(self, master = None, font = ('Segoe UI Black', 10)):

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.grid(row=0, column=0, padx=7, pady=7, sticky='nswe')
        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_forget() 

        self.database = self.getJSON(JSON_FILE_PATH)

        self.video_download_path = self.database['path']
        self.style = self.database['style']
        
        if self.video_download_path == "":
            self.video_download_path = f"{os.getcwd()}\Download".replace("\\", "/")
        if self.style == "":
            self.style = "Dark"
        
        ctk.set_appearance_mode(self.style)



        #============ Widgets ============

        self.options_frame = ctk.CTkFrame(self.main_frame)
        self.options_frame.grid(row=0, sticky='nswe', padx=20, pady=20)

        #============ Inside path_frame ============


        # Path Label

        self.path_label = ctk.CTkLabel(self.options_frame, text="Path : ", font=font, width=50)
        self.path_label.grid(row=0, column=0)


        # Path Entry -> path for downloading videos

        self.path_entry = ctk.CTkEntry(self.options_frame, font=font, width=350)
        self.path_entry.grid(row=0, column=1, padx=5, pady=5)
        self.path_entry.insert(0, self.video_download_path)
        


        # Browse Button -> for choosing a path

        self.path_button = ctk.CTkButton(self.options_frame, text="Browse", font=font, width=40, command=self.setPath)
        self.path_button.grid(row=0, column=2, padx=5, pady=5)


        # Appearance Mode Label
        self.appearance_mode_label = ctk.CTkLabel(self.options_frame, text="Style:", font=font, width=50)
        self.appearance_mode_label.grid(row=1, column=0, padx=10, pady=(10, 10))
        
        # Appearance Mode OptionMenu -> Light, Dark, System
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.options_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=1, column=1, padx=20, pady=(10, 10))
        
        
        
        # Set Default Values
        self.appearance_mode_optionemenu.set(self.style)



    #============ Attributes/Functions ============

    #showFrame Function -> To show the frame by unforgetting the grid
    def showFrame(self):
        self.main_frame.grid(row=0, column=1, sticky='nswe', padx=7, pady=7)


    #hideFrame Function -> Ofc, the vise versa of showFrame function
    def hideFrame(self):
        self.main_frame.grid_forget()


    #Set path Function -> Select a path for downloading the video
    def setPath(self):

        path = filedialog.askdirectory()
        if path == "":
            return
        
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, str(path))
        self.video_download_path = path
        print(f"path : {self.video_download_path}")


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
        self.style = new_appearance_mode
        self.setJSON(JSON_FILE_PATH, "style", self.style)
        ctk.set_appearance_mode(self.style)



