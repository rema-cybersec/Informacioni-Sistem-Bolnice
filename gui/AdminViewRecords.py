import customtkinter as ctk
from config import ADMINS_JSON_PATH, LEKARI_JSON_PATH, COMPANY_KEY_GPG_PATH
import json
import base64

class AdminViewRecords(ctk.CTkToplevel):
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400
    ERROR_TEXT="Invalid username or password."
    ERROR_TEXT_COLOR=("red", "#CC0000")

    def __init__(self, master):
        super().__init__(master)

        self.title("View Records")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 4), weight=0)
        self.grid_rowconfigure(3, weight=1)

        self.title_label = ctk.CTkLabel(self, font=ctk.CTkFont(size=20, weight="bold"), text="View Records")
        self.title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="new")

        self.username_entry = ctk.CTkEntry(self, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=10, sticky="new")

        self.key_entry = ctk.CTkEntry(self, placeholder_text="company key", show="#")
        self.key_entry.grid(row=2, column=0, columnspan=3, padx=(20, 20), pady=10, sticky="new")

        # Placeholder Frame for Error Text
        self.placeholder_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.placeholder_frame.grid(row=3, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.cancel_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="Cancel", command=self.quit_app)
        self.cancel_button.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="sw")

        self.confirm_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="View", command=self.view_records)
        self.confirm_button.grid(row=4, column=2, padx=(10, 10), pady=(10, 10), sticky="se")
    
    def find_record(self):
        with open(ADMINS_JSON_PATH, 'r') as file:
            data = json.load(file)
        for admin in data:
            if admin["username"] == self.username_entry.get().strip():
                return admin
        with open(LEKARI_JSON_PATH, 'r') as file:
            data = json.load(file)
        for lekar in data:
            if lekar["username"] == self.username_entry.get().strip():
                return lekar
        return None

    def view_records(self):
        record = self.find_record()
        if record == None:
            self.show_error_text()
        else:
            key = self.key_entry.get().strip()
            if self.validate_key(key):
                self.show_record(record, key)
            else:
                self.show_error_text()
    
    def validate_key(self, key_guess):
        with open(COMPANY_KEY_GPG_PATH, 'r') as file:
            key = file.read()
        if base64.b64encode(key_guess.encode("utf-8")) == key.encode("utf-8"):
            return True
        return False
    
    def show_record(self, record, key):
        print(record)

    def quit_app(self):
        self.destroy()
    
    def show_error_text(self):
        self.error_label = ctk.CTkLabel(master=self.placeholder_frame, text=self.ERROR_TEXT, text_color=self.ERROR_TEXT_COLOR)
        self.error_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

def start_session(master):
    app = AdminViewRecords(master)