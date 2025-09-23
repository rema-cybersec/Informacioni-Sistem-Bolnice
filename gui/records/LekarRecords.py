import customtkinter as ctk
from gui.records.Records import Records
from gui.ValidateKey import ValidateKey
from utils.Utils import get_all_lekar_data, decrypt_data, get_lekar_by_username
import bcrypt
from json import dump
from config import LEKARI_JSON_PATH

class LekarRecords(Records):
    WINDOW_WIDTH = 750
    WINDOW_HEIGHT = 600
    def __init__(self, master, lekar):
        self.lekar = lekar
        super().__init__(master, lekar)

    def initialize_information_frame(self):
        self.information_frame = ctk.CTkFrame(master=self)
        self.information_frame.grid(row=0, column=0, sticky= "nsew", padx=0, pady=0)

        self.information_frame.grid_rowconfigure((0, 1), weight=1)
        self.information_frame.grid_columnconfigure(0, weight=1)

        self.initialize_top_frame()
        self.initialize_encrypted_frame()
    
    def initialize_top_frame(self):
        self.top_frame = ctk.CTkFrame(master=self.information_frame)
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.top_frame.grid_columnconfigure(0, weight=0)
        self.top_frame.grid_columnconfigure(1, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)

        self.initialize_left_frame()
        self.initialize_right_frame()
    
    def initialize_left_frame(self):
        self.left_frame = ctk.CTkFrame(master=self.top_frame)
        self.left_frame.grid(row=0, column=0, sticky="nsw", padx=(20, 20), pady=(20, 20))

        self.left_frame.grid_rowconfigure((0, 1), weight=1)
        self.left_frame.grid_columnconfigure(0, weight=0)

        self.username_label = ctk.CTkLabel(master=self.left_frame, text="username:")
        self.username_label.grid(row=0, column=0, sticky="nsww", padx=(20, 20), pady=(20, 20))

        self.password_label = ctk.CTkLabel(master=self.left_frame, text="password:")
        self.password_label.grid(row=1, column=0, sticky="nsww", padx=(20, 20), pady=(20, 20))
    
    def initialize_right_frame(self):
        self.right_frame = ctk.CTkFrame(master=self.top_frame)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.right_frame.grid_rowconfigure((0, 1), weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        self.username_data = ctk.CTkLabel(master=self.right_frame, text=self.lekar["username"])
        self.username_data.grid(row=0, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.password_data = ctk.CTkEntry(master=self.right_frame, placeholder_text="change password", show="*")
        self.password_data.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))
    
    def initialize_encrypted_frame(self):
        self.encrypted_frame = ctk.CTkFrame(master=self.information_frame)
        self.encrypted_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.encrypted_frame.grid_rowconfigure(0, weight=1)
        self.encrypted_frame.grid_columnconfigure(0, weight=0)
        self.encrypted_frame.grid_columnconfigure(1, weight=1)

        self.initialize_encrypted_left()
        self.initialize_encrypted_right()
    
    def initialize_encrypted_left(self):
        self.encrypted_left = ctk.CTkFrame(master=self.encrypted_frame)
        self.encrypted_left.grid(row=0, column=0, sticky="nsw", padx=(20, 20), pady=(20, 20))

        self.encrypted_left.grid_rowconfigure((0, 1, 2), weight=1)
        self.encrypted_left.grid_columnconfigure(0, weight=0)
        self.encrypted_left.grid_columnconfigure(1, weight=1)

        self.ime_label = ctk.CTkLabel(master=self.encrypted_left, text="ime:")
        self.ime_label.grid(row=0, column=0, sticky="nsw", padx=(20, 20), pady=(20, 20))

        self.prezime_label = ctk.CTkLabel(master=self.encrypted_left, text="prezime:")
        self.prezime_label.grid(row=1, column=0, sticky="nsw", padx=(20, 20), pady=(20, 20))

        self.prezime_label = ctk.CTkLabel(master=self.encrypted_left, text="specijalizacija:")
        self.prezime_label.grid(row=2, column=0, sticky="nsw", padx=(20, 20), pady=(20, 20))
    
    def initialize_encrypted_right(self):
        self.encrypted_right = ctk.CTkFrame(master=self.encrypted_frame)
        self.encrypted_right.grid(row=0, column=1, sticky="nsew", padx=(20, 20), pady=(20, 20))

        self.encrypted_right.grid_rowconfigure((0, 1, 2), weight=1)
        self.encrypted_right.grid_columnconfigure(0, weight=1)

        self.ime_data = ctk.CTkLabel(master=self.encrypted_right, text="encrypted")
        self.ime_data.grid(row=0, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.prezime_data = ctk.CTkLabel(master=self.encrypted_right, text="encrypted")
        self.prezime_data.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.spec_data = ctk.CTkLabel(master=self.encrypted_right, text="encrypted")
        self.spec_data.grid(row=2, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))
    
    def initialize_button_frame(self):
        self.button_frame = ctk.CTkFrame(master=self)
        self.button_frame.grid(row=1, column=0, sticky="sew", padx=(20, 20), pady=(20, 20))

        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure((0, 2, 3), weight=0)

        self.decrypt_record_button = ctk.CTkButton(master=self.button_frame, text="Decrypt Record", corner_radius=15, command=self.decrypt_record)
        self.decrypt_record_button.grid(row=0, column=0, sticky="nsw", padx=(20, 20), pady=(20, 20))

        self.delete_record_button = ctk.CTkButton(master=self.button_frame, text="Delete Record", corner_radius=15, command=self.delete_record)
        self.delete_record_button.grid(row=0, column=3, sticky="nse", padx=(20, 20), pady=(20, 20))

        self.update_record_button = ctk.CTkButton(master=self.button_frame, text="Update Record", corner_radius=15, command=self.alter_record)
        self.update_record_button.grid(row=0, column=2, sticky="nse", padx=(20, 20), pady=(20, 20))
    
    def quit_app(self):
        self.destroy()

    def instantiate_key_check(self):
        self.key_obj = ValidateKey(self)

    def delete_record(self):
        self.action="delete"
        self.instantiate_key_check()
    
    def alter_record(self):
        self.action="update"
        self.instantiate_key_check()

    def decrypt_record(self):
        self.action = "decrypt"
        self.instantiate_key_check()

    def allow_action(self):
        isValid = self.key_obj.isValid
        secret_key = self.key_obj.key
        self.key_obj.destroy()
        if isValid:
            if self.action == "update":
                self.update_lekar()
            elif self.action == "delete":
                self.delete_lekar()
            elif self.action == "decrypt":
                self.decrypt_lekar(secret_key)
        self.action="other"
    
    def decrypt_lekar(self, secret_key):
        data = get_lekar_by_username(self.username_data.cget("text"))
        decrypted_data = {}
        decrypted_data["ime"] = decrypt_data(data["encrypted_data"]["ime"], secret_key)
        decrypted_data["prezime"] = decrypt_data(data["encrypted_data"]["prezime"], secret_key)
        decrypted_data["specijalizacija"] = decrypt_data(data["encrypted_data"]["specijalizacija"], secret_key)
        self.show_decrypted_data(decrypted_data)
            
    def delete_lekar(self):
        data = get_all_lekar_data()
        altered_data = []
        for lekar in data:
            if lekar["username"] == self.username_data.cget("text"):
                continue
            altered_data.append(lekar)
        with open(LEKARI_JSON_PATH, 'w') as file:
            dump(altered_data, file)
        self.destroy()

    def update_lekar(self):
        data = get_all_lekar_data()
        altered_data = []
        for lekar in data:
            if lekar["username"] == self.username_data.cget("text"):
                salt = bcrypt.gensalt()
                lekar["password"] = bcrypt.hashpw(self.password_data.get().encode("utf-8"), salt).decode("utf-8")
            altered_data.append(lekar)
        with open(LEKARI_JSON_PATH, 'w') as file:
            dump(altered_data, file)
        self.destroy()
    
    def show_decrypted_data(self, decrypted_data):
        self.ime_data.configure(text=decrypted_data["ime"])
        self.prezime_data.configure(text=decrypted_data["prezime"])
        self.spec_data.configure(text=decrypted_data["specijalizacija"])



def start_session(master, lekar):
    LekarRecords(master, lekar)


