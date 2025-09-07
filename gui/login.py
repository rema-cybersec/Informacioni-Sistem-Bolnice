import customtkinter as ctk
import json
from bcrypt import checkpw
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

        self.password_entry = ctk.CTkEntry(self, placeholder_text="password", show="*")
        self.password_entry.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.login_button = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Placeholder Frame for Error Text
        self.placeholder_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.placeholder_frame.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
    
    def login(self):
        self.clear_children()
        if(self.username_entry.get() != ""):
            with open(ADMINS_JSON_PATH, 'r') as file:
                admins_data = json.load(file)
            for admin in admins_data:
                if admin["username"] == self.username_entry.get().strip():
                    if checkpw(self.password_entry.get().strip().encode('utf-8'), admin["password"].encode('utf-8')):
                        self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text="Welcome, Admin.", text_color=("green", "#00CC00"))
                        self.error_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
                        return
            with open(LEKARI_JSON_PATH, 'r') as file:
                    lekari_data = json.load(file)
            for lekar in lekari_data:
                if lekar["username"] == self.username_entry.get().strip():
                    if(checkpw(self.password_entry.get().strip().encode('utf-8'), lekar["password"].encode('utf-8'))):
                        self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text="Welcome, Lekar.", text_color=("green", "#00CC00"))
                        self.error_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
                        return
            self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text="Invalid username or password.", text_color=("red", "#CC0000"))
            self.error_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            print("Entry empty")
            self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text="Invalid username or password.", text_color=("red", "#CC0000"))
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