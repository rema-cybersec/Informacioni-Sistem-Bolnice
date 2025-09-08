import customtkinter as ctk

class AdminRecords(ctk.CTkToplevel):
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 250
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
        self.top_frame.grid(row=0, column=0, sticky="nsew")

        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure((0, 1), weight=1)

        self.initialize_username_frame()
        self.initialize_password_frame()
    
    def initialize_username_frame(self):
        self.username_frame = ctk.CTkFrame(master=self.top_frame)
        self.username_frame.grid(row=0, column=0, sticky="nsew")

        self.username_frame.grid_rowconfigure(0, weight=1)
        self.username_frame.grid_columnconfigure((0, 1), weight=1)

        self.username_label = ctk.CTkLabel(master=self.username_frame, text="username:")
        self.username_label.grid(row=0, column=0, sticky="nswe")

        self.username_data = ctk.CTkLabel(master=self.username_frame, text="")
        self.username_data.grid(row=0, column=1, columnspan=2, sticky="nswe")
    
    def initialize_password_frame(self):
        self.password_frame = ctk.CTkFrame(master=self.top_frame)
        self.password_frame.grid(row=1, column=0, sticky="nsew")

        self.password_frame.grid_rowconfigure(0, weight=1)
        self.password_frame.grid_columnconfigure((0, 1), weight=1)

        self.password_label = ctk.CTkLabel(master=self.password_frame, text="username:")
        self.password_label.grid(row=0, column=0, sticky="nswe")

        self.password_data = ctk.CTkLabel(master=self.password_frame, text="")
        self.password_data.grid(row=0, column=1, columnspan=2, sticky="nswe")
    
    def initialize_bottom_frame(self):
        self.bottom_frame = ctk.CTkFrame(master=self)
        self.bottom_frame.grid(row=1, column=0, sticky="nsew")

        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure((1, 2), weight=0)

        self.delete_record_button = ctk.CTkButton(master=self.bottom_frame, text="Delete Record", corner_radius=15)
        self.delete_record_button.grid(row=0, column=2, sticky="nse")

        self.update_record_button = ctk.CTkButton(master=self.bottom_frame, text="Update Record", corner_radius=15)
        self.update_record_button.grid(row=0, column=1, sticky="nse")

    def fill_data(self):
        self.username_data.configure(text=self.admin["username"])
        self.password_data.configure(text=self.admin["password"])
    
    def quit_app(self):
        self.destroy()


def start_session(master, admin):
    AdminRecords(master, admin)


