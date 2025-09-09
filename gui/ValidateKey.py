import customtkinter as ctk
from config import COMPANY_KEY_GPG_PATH
from bcrypt import checkpw
import base64

class ValidateKey(ctk.CTkToplevel):
    WINDOW_WIDTH = 350
    WINDOW_HEIGHT = 100
    def __init__(self, master):
        super().__init__(master)

        self.isValid = None
        self.key = None

        self.title("Key Validation")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.attributes("-topmost", True)

        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 2), weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.key_entry = ctk.CTkEntry(master=self, placeholder_text="enter company key", show="#")
        self.key_entry.grid(row=0, column=0, columnspan=3, padx=(20, 20), pady=10, sticky="new")

        self.cancel_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="sw")

        self.confirm_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="Ok", command=self.confirm)
        self.confirm_button.grid(row=2, column=2, padx=(10, 10), pady=(10, 10), sticky="se")

    def confirm(self):
        key = self.key_entry.get()
        
        if key != "":
            with open(COMPANY_KEY_GPG_PATH, 'r') as file:
                key_hash = file.read()
            if base64.b64encode(key.encode("utf-8")) == key_hash.encode("utf-8"):
                self.isValid = True
                self.key = key
            else:
                self.isValid = False
        else:
            self.isValid = False
        self.withdraw()
        self.master.allow_action()
    
    def cancel(self):
        self.isValid = False
        self.withdraw()
        self.master.allow_action()