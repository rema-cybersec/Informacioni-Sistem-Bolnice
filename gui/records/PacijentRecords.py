import customtkinter as ctk
from gui.records.Records import Records

class PacijentRecords(Records):
    WINDOW_WIDTH = 750
    WINDOW_HEIGHT = 600
    def __init__(self, master, pacijent):
        self.dijagnoza = pacijent
        super().__init__(master, pacijent)
        
        self.title("Pacijent Records")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

def start_session(master, pacijent):
    PacijentRecords(master, pacijent)