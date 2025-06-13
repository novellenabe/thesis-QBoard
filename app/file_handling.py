import os

class file_handling():    
    def __init__(self, main_window):
        super().__init__()
            
    def check_file_exist(filename):
        return os.path.exists(filename)
        
    def load_stylesheet(filename):
        try:
            with open(filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: Stylesheet file '{filename}' not found.")
            return ""
            
        except Exception as e:
            print(f"Error reading stylesheet file '{filename}' : {e}")
            return ""
    