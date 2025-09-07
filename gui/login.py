import customtkinter as ctk

class LoginWindow(ctk.CTk):
    WINDOW_WIDTH=400
    WINDOW_HEIGHT=450
    def __init__(self):
        super().__init__()

        #config
        self.title("Login")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

def setup():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    setup()
    app = LoginWindow()
    app.mainloop()