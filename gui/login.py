import customtkinter as ctk
from config import ADMINS_JSON_PATH, LEKARI_JSON_PATH

class LoginWindow(ctk.CTk):
    WINDOW_WIDTH=400
    WINDOW_HEIGHT=350
    def __init__(self):
        super().__init__()

        # Configuration
        self.title("Login")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

        # Grid Configuration - 4x5
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure((0, 1, 3), weight=0)
        self.grid_rowconfigure(2, weight=1)

        # Item Configuration
        self.username_entry = ctk.CTkEntry(self, placeholder_text="username")
        self.username_entry.grid(row=0, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.password_entry = ctk.CTkEntry(self, placeholder_text="password")
        self.password_entry.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.login_button = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Placeholder Frame for Error Text
        self.placeholder_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.placeholder_frame.grid(row=2, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
    
    def login(self):
        self.clear_children()
        if(self.username_entry.get() != ""):
            pass
        else:
            print("Entry empty")
            self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text="Invalid Username", text_color=("red", "#CC0000"))
            self.error_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
    
    def clear_children(self):
        for child in self.placeholder_frame.winfo_children():
            child.destroy()

def setup():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    setup()
    app = LoginWindow()
    app.mainloop()