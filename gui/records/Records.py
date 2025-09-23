import customtkinter as ctk

class Records(ctk.CTkToplevel):
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 300
    def __init__(self, master, user):
        super().__init__(master)

        self.user = user

        self.title("Admin Records")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.initialize_information_frame()
        self.initialize_button_frame()

    def initialize_information_frame(self):
        pass

    def initialize_button_frame(self):
        pass