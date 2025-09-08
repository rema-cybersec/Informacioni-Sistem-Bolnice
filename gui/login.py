import customtkinter as ctk
import json
from bcrypt import checkpw
from config import ADMINS_JSON_PATH, LEKARI_JSON_PATH
from users.SysadminUser import SysadminUser
from gui.AdminView import start_admin_session

class LoginWindow(ctk.CTkToplevel):
    WINDOW_WIDTH=400
    WINDOW_HEIGHT=250
    ERROR_TEXT="Invalid username or password."
    ERROR_TEXT_COLOR=("red", "#CC0000")

    def __init__(self, app):
        super().__init__(app.app)
        self.app = app
        # Configuration
        self.title("Login")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

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
                    user = SysadminUser(admin["username"], self.password_entry.get().strip())
                    if user.ValidatePassword(admin):
                        self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text="Welcome, Admin.", text_color=("green", "#00CC00"))
                        self.error_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
                        
                        self.withdraw()
                        start_admin_session(self.app, user, validated=True)

                        return
            with open(LEKARI_JSON_PATH, 'r') as file:
                    lekari_data = json.load(file)
            for lekar in lekari_data:
                if lekar["username"] == self.username_entry.get().strip():
                    if(checkpw(self.password_entry.get().strip().encode('utf-8'), lekar["password"].encode('utf-8'))):
                        self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text="Welcome, Lekar.", text_color=("green", "#00CC00"))
                        self.error_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
                        return
            self.show_error_text()
        else:
            print("Entry empty")
            self.show_error_text()
    
    def quit_app(self):
        self.app.app.destroy()
            
    
    def clear_children(self):
        for child in self.placeholder_frame.winfo_children():
            child.destroy()
    def show_error_text(self):
        self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text=self.ERROR_TEXT, text_color=self.ERROR_TEXT_COLOR)
        self.error_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")


def setup():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")