import customtkinter as ctk
from config import ADMINS_JSON_PATH, LEKARI_JSON_PATH
import json
from gui.AdminViewFind import start_session

class AdminView(ctk.CTkToplevel):
    WINDOW_WIDTH=800
    WINDOW_HEIGHT=500

    def __init__(self, app, user):
        super().__init__(app.app)
        self.app = app
        self.user = user

        self.title("AdminView")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        # Grid Configuration - 5x6
        self.grid_columnconfigure((0, 1, 2, 3, 5), weight=0)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(1, weight=1);
        self.grid_rowconfigure((0, 2), weight=0)
 
        self.initialize_sidebar()

        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=1, rowspan=2, columnspan=5, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Admini")
        self.tabview.add("Lekari")

        self.tabview.tab("Admini").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Lekari").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Admini").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Lekari").grid_rowconfigure(0, weight=1)

        self.tab_label_admini = ctk.CTkLabel(master=self.tabview.tab("Admini"), text="Click search to start!")
        self.tab_label_admini.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.tab_label_lekari = ctk.CTkLabel(master=self.tabview.tab("Lekari"), text="Click search to start!")
        self.tab_label_lekari.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.search_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="Search", command=self.search_users)
        self.search_button.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="sw")

        self.find_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="Find", command=self.view_records)
        self.find_button.grid(row=2, column=2, padx=(10, 10), pady=(10, 10), sticky="sw")

        self.add_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="Add")
        self.add_button.grid(row=2, column=3, padx=(10, 10), pady=(10, 10), sticky="sw")

        self.logout_button = ctk.CTkButton(master=self, corner_radius=15, width=10, text="Logout", command=self.logout)
        self.logout_button.grid(row=2, column=5, padx=(10, 10), pady=(10, 10), sticky="se")
    
    def initialize_sidebar(self):
        self.sidebar = ctk.CTkFrame(self)
        self.sidebar.grid(row=0, column=0, rowspan=6, sticky="nsw")
        self.sidebar.grid_rowconfigure((0, 1, 3, 4, 5), weight=0)
        self.sidebar.grid_rowconfigure(2, weight=1)

        self.welcome_label = ctk.CTkLabel(master=self.sidebar, text="logged in as:")
        self.welcome_label.grid(row=0, column=0, padx=(5, 10), pady=(5, 5))

        self.title_frame = ctk.CTkFrame(master=self.sidebar)
        self.title_frame.grid(row=1, column=0, padx=20, pady=20)
        self.user_label = ctk.CTkLabel(master=self.title_frame, text=self.user.username, font=ctk.CTkFont(size=20, weight="bold"))
        self.user_label.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.change_password = ctk.CTkButton(master=self.sidebar, corner_radius=15, text="change password")
        self.change_password.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="sw")

        self.appearance_label = ctk.CTkLabel(master=self.sidebar, text="Change Appearance Mode")
        self.appearance_label.grid(row=4, column=0, padx=5, pady=(20, 5), sticky="s")

        self.appearance = ctk.CTkOptionMenu(master=self.sidebar, values=["Dark", "Light", "System"], command=self.change_appearance)
        self.appearance.grid(row=5, column=0, padx=(5, 15), pady=(5, 20), sticky="s")    
    
    def change_appearance(self, new_appearance: str):
        ctk.set_appearance_mode(new_appearance)
    
    def logout(self):
        self.app.restore_login()
        self.destroy()

    def quit_app(self):
        self.app.app.destroy()
    
    def search_users(self):
        if self.tabview.get() == "Admini":
            out = ""
            with open(ADMINS_JSON_PATH, 'r') as file:
                data = json.load(file)
            for admin in data:
                out += admin["username"] + "\n"
            if out == "":
                out = "Nothing found."
            self.tab_label_admini.configure(text=out)
        elif self.tabview.get() == "Lekari":
            out = ""
            with open(LEKARI_JSON_PATH, 'r') as file:
                data = json.load(file)
            for lekar in data:
                out += lekar["username"] + "\n"
            if out == "":
                out = "Nothing found."
            self.tab_label_lekari.configure(text=out)
        else:
            self.tab_label_admini.configure(text=out)
            self.tab_label_lekari.configure(text=out)
    def view_records(self):
        start_session(self)

def setup():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

def start_admin_session(app, user, validated=False):
    if validated:
        setup()
        app.login_window.withdraw()
        AdminView(app, user)
    else:
        return