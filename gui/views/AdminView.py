from gui.views.View import View
from utils.Utils import setup_appearance_mode
import customtkinter as ctk

class AdminView(View):
    def __init__(self, app, user):
        super().__init__(app, user)
        
        self.title("AdminView")

    def initialize_sidebar(self):
        self.sidebar = ctk.CTkFrame(self)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.grid_rowconfigure((0, 1, 3, 4, 5), weight=0)
        self.sidebar.grid_rowconfigure(2, weight=1)

        self.welcome_label = ctk.CTkLabel(master=self.sidebar, text="logged in as:")
        self.welcome_label.grid(row=0, column=0, padx=(5, 10), pady=(5, 5), sticky="new")

        self.title_frame = ctk.CTkFrame(master=self.sidebar)
        self.title_frame.grid(row=1, column=0, padx=20, pady=20, sticky="new")

        self.user_label = ctk.CTkLabel(master=self.title_frame, text=self.user["username"], font=ctk.CTkFont(size=20, weight="bold"))
        self.user_label.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="nsew")

        self.change_password = ctk.CTkButton(master=self.sidebar, corner_radius=15, text="change password", command=self.edit_password)
        self.change_password.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="sew")

        self.appearance_label = ctk.CTkLabel(master=self.sidebar, text="Change Appearance Mode")
        self.appearance_label.grid(row=4, column=0, padx=5, pady=(20, 5), sticky="sew")

        self.appearance = ctk.CTkOptionMenu(master=self.sidebar, values=["Dark", "Light", "System"], command=self.change_appearance)
        self.appearance.grid(row=5, column=0, padx=(5, 15), pady=(5, 20), sticky="sew")

def start_admin_session(app, user, validated=False):
    if validated:
        setup_appearance_mode(ctk)
        app.login_window.withdraw()
        AdminView(app, user)
    else:
        return