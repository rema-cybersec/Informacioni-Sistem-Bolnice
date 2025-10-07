import customtkinter as ctk
from gui.records.Records import Records

class DijagnozaRecords(Records):
    WINDOW_WIDTH = 750
    WINDOW_HEIGHT = 600
    def __init__(self, master, dijagnoza):
        self.dijagnoza = dijagnoza
        self.key_obj = None
        super().__init__(master, dijagnoza)
        
        self.title("Dijagnoza Records")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

def start_session(master, dijagnoza):
    DijagnozaRecords(master, dijagnoza)