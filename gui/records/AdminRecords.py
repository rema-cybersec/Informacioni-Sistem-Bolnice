import customtkinter as ctk
from gui.ValidateKey import ValidateKey
from time import sleep
from utils.Utils import get_all_admin_data
import bcrypt
from json import dump
from config import ADMINS_JSON_PATH

class AdminRecords(ctk.CTkToplevel):
    WINDOW_WIDTH = 750
    WINDOW_HEIGHT = 350
    def __init__(self, master, admin):
        super().__init__(master)

        self.admin = admin

        self.title("Admin Records")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.initialize_top_frame()
        self.initialize_bottom_frame()

        self.fill_data()
    
    def initialize_top_frame(self):
        self.top_frame = ctk.CTkFrame(master=self)
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.top_frame.grid_columnconfigure((0, 1), weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)

        self.initialize_left_frame()
        self.initialize_right_frame()
    
    def initialize_left_frame(self):
        self.left_frame = ctk.CTkFrame(master=self.top_frame)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.left_frame.grid_rowconfigure((0, 1), weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        self.username_label = ctk.CTkLabel(master=self.left_frame, text="username:")
        self.username_label.grid(row=0, column=0, sticky="nsww", padx=(20, 20), pady=(20, 20))

        self.password_label = ctk.CTkLabel(master=self.left_frame, text="password:")
        self.password_label.grid(row=1, column=0, sticky="nsww", padx=(20, 20), pady=(20, 20))
    
    def initialize_right_frame(self):
        self.right_frame = ctk.CTkFrame(master=self.top_frame)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.right_frame.grid_rowconfigure((0, 1), weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        self.username_data = ctk.CTkLabel(master=self.right_frame, text="")
        self.username_data.grid(row=0, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.password_data = ctk.CTkEntry(master=self.right_frame, placeholder_text="", show="*")
        self.password_data.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))
    
    def initialize_bottom_frame(self):
        self.bottom_frame = ctk.CTkFrame(master=self)
        self.bottom_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure((1, 2), weight=0)

        self.delete_record_button = ctk.CTkButton(master=self.bottom_frame, text="Delete Record", corner_radius=15)
        self.delete_record_button.grid(row=0, column=2, sticky="nse", padx=(20, 20), pady=(20, 20))

        self.update_record_button = ctk.CTkButton(master=self.bottom_frame, text="Update Record", corner_radius=15, command=self.instantiate_key_check)
        self.update_record_button.grid(row=0, column=1, sticky="nse", padx=(20, 20), pady=(20, 20))

    def fill_data(self):
        self.username_data.configure(text=self.admin["username"])
        hash = ""
        for _ in self.admin["password"]:
            hash += "*"
        self.password_data.configure(placeholder_text=hash)
    
    def quit_app(self):
        self.destroy()

    def instantiate_key_check(self):
        self.key_obj = ValidateKey(self)

    def allow_update(self):
        isValid = self.key_obj.isValid
        self.key_obj.destroy()
        if isValid:
            self.update_record()
    
    def update_record(self):
        data = get_all_admin_data()
        altered_data = []
        for admin in data:
            if admin["username"] == self.username_data.cget("text"):
                salt = bcrypt.gensalt()
                admin["password"] = bcrypt.hashpw(self.password_data.get().encode("utf-8"), salt).decode("utf-8")
            altered_data.append(admin)
        with open(ADMINS_JSON_PATH, 'w') as file:
            dump(altered_data, file)



def start_session(master, admin):
    AdminRecords(master, admin)


