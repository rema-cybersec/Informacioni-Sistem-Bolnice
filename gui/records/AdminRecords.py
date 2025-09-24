import customtkinter as ctk
from gui.records.Records import Records
from utils.Utils import update_admin_record, delete_admin_record

class AdminRecords(Records):
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 300
    def __init__(self, master, admin):
        self.admin = admin
        self.key_obj = None
        super().__init__(master, admin)

        self.title("Admin Records")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

    
    def initialize_information_frame(self):
        self.information_frame = ctk.CTkFrame(master=self)
        self.information_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.information_frame.grid_columnconfigure(0, weight=0)
        self.information_frame.grid_columnconfigure(1, weight=1)
        self.information_frame.grid_rowconfigure(0, weight=1)

        self.initialize_left_frame()
        self.initialize_right_frame()
    
    def initialize_left_frame(self):
        self.left_frame = ctk.CTkFrame(master=self.information_frame)
        self.left_frame.grid(row=0, column=0, sticky="nsw", padx=(20, 20), pady=(20, 20))

        self.left_frame.grid_rowconfigure((0, 1), weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        self.username_label = ctk.CTkLabel(master=self.left_frame, text="username:")
        self.username_label.grid(row=0, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.password_label = ctk.CTkLabel(master=self.left_frame, text="password:")
        self.password_label.grid(row=1, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))
    
    def initialize_right_frame(self):
        self.right_frame = ctk.CTkFrame(master=self.information_frame)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.right_frame.grid_rowconfigure((0, 1), weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        self.username_data = ctk.CTkLabel(master=self.right_frame, text=self.admin["username"])
        self.username_data.grid(row=0, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.password_data = ctk.CTkEntry(master=self.right_frame, placeholder_text="change password", show="*")
        self.password_data.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))
    
    def initialize_button_frame(self):
        self.bottom_frame = ctk.CTkFrame(master=self)
        self.bottom_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure((1, 2), weight=0)

        self.delete_record_button = ctk.CTkButton(master=self.bottom_frame, text="Delete Record", corner_radius=15, command=self.delete_record)
        self.delete_record_button.grid(row=0, column=2, sticky="nse", padx=(20, 20), pady=(20, 20))

        self.update_record_button = ctk.CTkButton(master=self.bottom_frame, text="Update Record", corner_radius=15, command=self.alter_record)
        self.update_record_button.grid(row=0, column=1, sticky="nse", padx=(20, 20), pady=(20, 20))
    
    def quit_app(self):
        self.destroy()

    def delete_record(self):
        self.action="delete"
        self.check_key_protocol()
    
    def alter_record(self):
        self.action="update"
        self.check_key_protocol()

    def allow_action(self):
        if self.key_obj.isValid:
            if self.action == "update":
                update_admin_record(self)
            elif self.action == "delete":
                delete_admin_record(self)
        self.action="other"


def start_session(master, admin):
    AdminRecords(master, admin)


