import customtkinter as ctk
from config import ADMINS_JSON_PATH, LEKARI_JSON_PATH, COMPANY_KEY_GPG_PATH
import json

class AdminViewRecords(ctk.CTkToplevel):
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400

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

        self.cancel_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="Cancel", command=self.quit_app)
        self.cancel_button.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="sw")

        self.confirm_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="View")
        self.confirm_button.grid(row=4, column=2, padx=(10, 10), pady=(10, 10), sticky="se")
    

    def quit_app(self):
        self.destroy()

def start_session(master):
    app = AdminViewRecords(master)