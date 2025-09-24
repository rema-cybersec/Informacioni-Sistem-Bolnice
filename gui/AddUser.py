import customtkinter as ctk
from gui.ValidateKey import ValidateKey
from utils.Utils import add_admin_user, add_lekar_user


class AddUser(ctk.CTkToplevel):
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 700
    def __init__(self, master):
        super().__init__(master)

        self.title("Add User")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.attributes("-topmost", True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 2), weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.instantiate_top_frame()
        self.instantiate_bottom_frame()
        self.instantiate_button_frame()


    def instantiate_top_frame(self):
        self.top_frame = ctk.CTkFrame(master=self)
        self.top_frame.grid(row=0, column=0, sticky="new", padx=(20, 20), pady=(20, 20))

        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=0)

        self.user_type = ctk.CTkOptionMenu(master=self.top_frame, values=["User Type", "Admin", "Lekar"], command=self.choose_user)
        self.user_type.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
    
    def instantiate_bottom_frame(self):
        self.bottom_frame = ctk.CTkFrame(master=self)
        self.bottom_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=0)

    def instantiate_button_frame(self):
        self.button_frame = ctk.CTkFrame(master=self)
        self.button_frame.grid(row=2, column=0, sticky="sew", padx=(20, 20), pady=(20, 20))

        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure((0, 2), weight=0)

        self.cancel_button = ctk.CTkButton(master=self.button_frame, text="Cancel", corner_radius=15, command=self.cancel)
        self.cancel_button.grid(row=0, column=0, sticky="nsw", padx=(20, 20), pady=(20, 20))

        self.confirm_button = ctk.CTkButton(master=self.button_frame, text="Ok", corner_radius=15, command=self.confirm)
        self.confirm_button.grid(row=0, column=2, sticky="nse", padx=(20, 20), pady=(20, 20))
    
    def choose_user(self, user_type: str):
        if user_type == "User Type":
            self.clear_bottom_frame()
            return
        elif user_type == "Admin":
            self.clear_bottom_frame()
            self.instantiate_admin_user_frame()
            return
        else:
            self.clear_bottom_frame()
            self.instantiate_lekar_user_frame()
            return
    
    def instantiate_admin_user_frame(self):
        self.admin_user_frame = ctk.CTkFrame(master=self.bottom_frame)
        self.admin_user_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.admin_user_frame.grid_columnconfigure(0, weight=1)
        self.admin_user_frame.grid_rowconfigure((0, 1), weight=0)

        self.admin_username_data = ctk.CTkEntry(master=self.admin_user_frame, placeholder_text="username")
        self.admin_username_data.grid(row=0, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.admin_password_data = ctk.CTkEntry(master=self.admin_user_frame, placeholder_text="password", show="*")
        self.admin_password_data.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))
    
    def instantiate_lekar_user_frame(self):
        self.lekar_user_frame = ctk.CTkFrame(master=self.bottom_frame)
        self.lekar_user_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.lekar_user_frame.grid_columnconfigure(0, weight=1)
        self.lekar_user_frame.grid_rowconfigure((0, 1, 2), weight=0)

        self.lekar_username_data = ctk.CTkEntry(master=self.lekar_user_frame, placeholder_text="username")
        self.lekar_username_data.grid(row=0, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.lekar_password_data = ctk.CTkEntry(master=self.lekar_user_frame, placeholder_text="password", show="*")
        self.lekar_password_data.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.instantiate_lekar_encrypted_frame()

    def instantiate_lekar_encrypted_frame(self):
        self.lekar_encrypted_frame = ctk.CTkFrame(master=self.lekar_user_frame)
        self.lekar_encrypted_frame.grid(row=2, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.lekar_encrypted_frame.grid_columnconfigure(0, weight=1)
        self.lekar_encrypted_frame.grid_rowconfigure((0, 1), weight=0)
        self.lekar_encrypted_frame.grid_rowconfigure(2, weight=1)

        self.lekar_ime_entry = ctk.CTkEntry(master=self.lekar_encrypted_frame, placeholder_text="ime")
        self.lekar_ime_entry.grid(row=0, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.lekar_prezime_entry = ctk.CTkEntry(master=self.lekar_encrypted_frame, placeholder_text="prezime")
        self.lekar_prezime_entry.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.lekar_spec_entry = ctk.CTkEntry(master=self.lekar_encrypted_frame, placeholder_text="specijalizacija")
        self.lekar_spec_entry.grid(row=2, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

    def instantiate_key_check(self):
        self.key_obj = ValidateKey(self)
    
    def cancel(self):
        self.destroy()
    
    def confirm(self):
        user_type = self.user_type.get()
        if user_type == "User Type":
            self.action = "Other"
            return
        elif user_type == "Admin":
            self.action = "Other"
            if not (self.admin_username_data.get() == "" or self.admin_password_data.get() == ""):
                self.action="Admin"
                self.instantiate_key_check()
            return
        elif user_type == "Lekar":
            self.action = "Other"
            if not (self.lekar_username_data.get() == "" or self.lekar_password_data.get() == ""):
                self.action = "Lekar"
                self.instantiate_key_check()
            return
        else:
            self.action = "Other"
            return

    def allow_action(self):
        isValid = self.key_obj.isValid
        secret_key = self.key_obj.key
        self.key_obj.destroy()
        if isValid:
            if self.action == "Admin":
                add_admin_user(self)
                return
            elif self.action == "Lekar":
                add_lekar_user(self, secret_key=secret_key)
                return

    def clear_bottom_frame(self):
        for child in self.bottom_frame.winfo_children():
            child.destroy()
