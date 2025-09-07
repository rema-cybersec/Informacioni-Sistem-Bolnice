import customtkinter as ctk

class AdminView(ctk.CTkToplevel):
    WINDOW_WIDTH=500
    WINDOW_HEIGHT=300

    def __init__(self, master):
        super().__init__(master)

        self.title("AdminView")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.quit_app)
    
    def quit_app(self):
        self.master.destroy()

def setup():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

def start_admin_session(window, validated=False):
    if validated:
        setup()
        window.withdraw()
        AdminView(window.master)
    else:
        return