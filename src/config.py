from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        self.loaded_dotenv = False
        
    def get(self, key):
        if not self.loaded_dotenv:
            load_dotenv()
            self.loaded_dotenv = True
        return os.environ.get(key)