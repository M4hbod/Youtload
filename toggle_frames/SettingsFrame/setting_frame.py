from doctest import master
import tkinter as tk
import customtkinter as ctk
import tkinter.filedialog as filedialog
import json



JSON_FILE_PATH = "main_frames\\toggle_frames\SettingsFrame\configs.json"

class SettingsFrame:


    #============ Initialization ============
    def __init__(self, master = None, font = ('Segoe UI Black', 10)):

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.grid(row=0, column=0, padx=7, pady=7, sticky='nswe')
        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_forget() 

        self.database = self.getJSON(JSON_FILE_PATH)

        self.video_download_path = self.database['path']



        #============ Widgets ============

        self.options_frame = ctk.CTkFrame(self.main_frame)
        self.options_frame.grid(row=0, sticky='nswe', padx=20, pady=20)

        #============ Inside path_frame ============


        # Path Label

        self.path_label = ctk.CTkLabel(self.options_frame, text="Path : ", text_font=font, width=50)
        self.path_label.grid(row=0, column=0)


        # Path Entry -> path for downloading videos

        self.path_entry = ctk.CTkEntry(self.options_frame, text_font=font, width=350)
        self.path_entry.grid(row=0, column=1, padx=5, pady=5)
        self.path_entry.insert(0, self.database['path'])
        


        # Browse Button -> for choosing a path

        self.path_button = ctk.CTkButton(self.options_frame, text="Browse", text_font=font, width=40, command=self.setPath)
        self.path_button.grid(row=0, column=2, padx=5, pady=5)






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
        #self.path_entry.configure(state=tk.NORMAL)
        self.path_entry.insert(0, str(path))
        #self.path_entry.configure(state=tk.DISABLED)
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

            data.close()

        return all_data

    def setJSON(self, filename, key, value):

        data_to_append = {key:value}
        with open(filename, 'w') as data:
            json.dump(data_to_append, data)

            data.close()




