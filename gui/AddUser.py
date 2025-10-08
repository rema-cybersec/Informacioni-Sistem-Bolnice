import customtkinter as ctk
from gui.ValidateKey import ValidateKey
from utils.Utils import add_admin_user, add_lekar_user, add_pacijent_user, add_dijagnoza


class AddUser(ctk.CTkToplevel):
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 700
    def __init__(self, master):
        self.role = master.role
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

        if self.role == "Admin":
            self.user_type = ctk.CTkOptionMenu(master=self.top_frame, values=["User Type", "Admin", "Lekar"], command=self.choose_user)
        else:
            self.user_type = ctk.CTkOptionMenu(master=self.top_frame, values=["Type", "Pacijent", "Dijagnoza"], command=self.choose_user)
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
        if self.role == "Admin":
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
        else:
            if user_type == "Type":
                self.clear_bottom_frame()
                return
            elif user_type == "Pacijent":
                self.clear_bottom_frame()
                self.instantiate_pacijent_user_frame()
                return
            else:
                self.clear_bottom_frame()
                self.instantiate_dijagnoza_frame()
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

    def instantiate_pacijent_user_frame(self):
        self.pacijent_user_frame = ctk.CTkFrame(master=self.bottom_frame)
        self.pacijent_user_frame.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.pacijent_user_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.pacijent_user_frame.grid_rowconfigure((0, 1), weight=0)

        self.jmbg_field = ctk.CTkEntry(master=self.pacijent_user_frame, placeholder_text="JMBG")
        self.jmbg_field.grid(row=0, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nswe")

        self.instantiate_pacijent_encrypted_frame()
    
    def instantiate_pacijent_encrypted_frame(self):
        self.pacijent_encrypted_frame = ctk.CTkFrame(master=self.pacijent_user_frame)
        self.pacijent_encrypted_frame.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.pacijent_encrypted_frame.grid_columnconfigure(0, weight=1)
        self.pacijent_encrypted_frame.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.pime_field = ctk.CTkEntry(master=self.pacijent_encrypted_frame, placeholder_text="ime")
        self.pime_field.grid(row=0, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nswe")

        self.pprz_field = ctk.CTkEntry(master=self.pacijent_encrypted_frame, placeholder_text="prezime")
        self.pprz_field.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nswe")

        self.bt_field = ctk.CTkEntry(master=self.pacijent_encrypted_frame, placeholder_text="krvni tip")
        self.bt_field.grid(row=2, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nswe")

        self.datrodj_frame = ctk.CTkFrame(master=self.pacijent_encrypted_frame)
        self.datrodj_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nswe")

        self.datrodj_frame.grid_rowconfigure((0, 1), weight=0)
        self.datrodj_frame.grid_columnconfigure((0, 1, 2), weight=0)

        self.l1 = ctk.CTkLabel(master=self.datrodj_frame, text="dan")
        self.l1.grid(row= 0, column=0, sticky="nswe")

        self.day_cb = ctk.CTkOptionMenu(master=self.datrodj_frame, values=[str(i) for i in range(1, 32)])
        self.day_cb.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nswe")

        self.l2 = ctk.CTkLabel(master=self.datrodj_frame, text="mesec")
        self.l2.grid(row= 0, column=1, sticky="nswe")

        self.month_cb = ctk.CTkOptionMenu(master=self.datrodj_frame, values=[str(i) for i in range(1, 13)])
        self.month_cb.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nswe")

        self.l3 = ctk.CTkLabel(master=self.datrodj_frame, text="godina")
        self.l3.grid(row= 0, column=2, sticky="nswe")

        self.year_cb = ctk.CTkOptionMenu(master=self.datrodj_frame, values=[str(i) for i in range(1942, 2026)])
        self.year_cb.grid(row=1, column=2, padx=(20, 20), pady=(20, 20), sticky="nswe")

    def instantiate_dijagnoza_frame(self):
        self.dijagnoza_frame = ctk.CTkFrame(master=self.bottom_frame)
        self.dijagnoza_frame.grid(row=1, column=0, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.dijagnoza_frame.grid_columnconfigure(0, weight=1)
        self.dijagnoza_frame.grid_rowconfigure((0, 1, 2, 3), weight=0)

        self.sifra_field = ctk.CTkEntry(master=self.dijagnoza_frame, placeholder_text="sifra dijagnoze")
        self.sifra_field.grid(row=0, column=0, sticky="nwe", padx=(20, 20), pady=(20, 20))

        self.naziv_field = ctk.CTkEntry(master=self.dijagnoza_frame, placeholder_text="naziv dijagnoze")
        self.naziv_field.grid(row=1, column=0, sticky="nwe", padx=(20, 20), pady=(20, 20))

        self.opis_field = ctk.CTkEntry(master=self.dijagnoza_frame, placeholder_text="opis dijagnoze")
        self.opis_field.grid(row=2, column=1, rowspan=2, sticky="swe", padx=(20, 20), pady=(20, 20))

    def instantiate_key_check(self):
        self.key_obj = ValidateKey(self)
    
    def cancel(self):
        self.destroy()
    
    def confirm(self):
        user_type = self.user_type.get()
        if self.role == "Admin":
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
            if user_type == "Type":
                self.action = "Other"
                return
            elif user_type == "Pacijent":
                self.action = "Other"
                if not (self.jmbg_field.get() == ""):
                    self.action = "Pacijent"
                    self.instantiate_key_check()
                return
            else:
                self.action = "Other"
                if not (self.sifra_field.get() == "" or self.naziv_field.get() == "" or self.opis_field.get() == "") :
                    self.action = "Dijagnoza"
                    self.instantiate_key_check()
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
            elif self.action == "Pacijent":
                add_pacijent_user(self, secret_key=secret_key)
            elif self.action == "Dijagnoza":
                add_dijagnoza(self)

    def clear_bottom_frame(self):
        for child in self.bottom_frame.winfo_children():
            child.destroy()
