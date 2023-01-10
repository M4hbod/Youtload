import os

class Directory:
    
    @staticmethod
    def get_current_directory():
        return os.getcwd()

    @staticmethod
    def create_directory(path):
        if not os.path.exists(path):
            os.makedirs(path) 

    @staticmethod
    def check_if_directory_exists(path):
        return os.path.isdir(path)
    
    @staticmethod
    def get_files_and_folders(path):
        return os.listdir(path)
    
    @staticmethod
    def clear_directory(path):
        for file in os.listdir(path):
            try:
                os.remove(os.path.join(path, file))
            except:
                pass