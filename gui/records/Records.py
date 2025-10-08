import customtkinter as ctk
from gui.ValidateKey import ValidateKey

class Records(ctk.CTkToplevel):
    def __init__(self, master, user):
        super().__init__(master)
        self.key_obj = None
        self.role = master.role

        self.user = user
        self.keyValidated = False

        self.title("Records")
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.initialize_information_frame()
        self.initialize_button_frame()

    def initialize_information_frame(self):
        pass

    def initialize_button_frame(self):
        pass

    def allow_action(self):
        pass

    def quit_app(self):
        self.destroy()

    def instantiate_key_check(self):
        if self.key_obj != None:
            self.key_obj.destroy()
        self.key_obj = ValidateKey(self)

    def check_key_protocol(self):
        if self.key_obj != None and self.key_obj.isValid == True:
            self.key_obj.allow_noauth()
        else:
            self.instantiate_key_check()
        