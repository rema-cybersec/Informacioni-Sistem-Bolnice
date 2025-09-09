import customtkinter as ctk
from config import ADMINS_JSON_PATH, LEKARI_JSON_PATH
import json
from gui.records.AdminRecords import start_session as start_admin_view
from gui.records.LekarRecords import start_session as start_lekar_view
from gui.AddUser import AddUser
from utils.Utils import get_admin_by_username, get_lekar_by_username

class AdminView(ctk.CTkToplevel):
    WINDOW_WIDTH=500
    WINDOW_HEIGHT=500

    def __init__(self, app, user):
        super().__init__(app.app)
        self.app = app
        self.user = user

        self.title("AdminView")
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        # Grid Configuration - 1x2
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
 
        self.initialize_sidebar()
        self.initialize_master_frame()
    
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
    
    def initialize_master_frame(self):
        self.master_frame = ctk.CTkFrame(master=self)
        self.master_frame.grid(row=0, column=1, sticky="nsew")

        self.master_frame.grid_rowconfigure(0, weight=1)
        self.master_frame.grid_rowconfigure(1, weight=0)
        self.master_frame.grid_columnconfigure(0, weight=1)

        self.initialize_users_frame()
        self.initialize_button_frame()
    
    def initialize_users_frame(self):
        self.users_frame = ctk.CTkFrame(master=self.master_frame)
        self.users_frame.grid(row=0, column=0, sticky="nsew")

        self.users_frame.grid_rowconfigure(0, weight=0)
        self.users_frame.grid_rowconfigure(1, weight=1)
        self.users_frame.grid_columnconfigure(0, weight=1)

        self.users_label = ctk.CTkLabel(master=self.users_frame, text="available user information:")
        self.users_label.grid(row=0, column=0, padx=10, pady=5, sticky="sw")

        self.tabview = ctk.CTkTabview(master=self.users_frame)
        self.tabview.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
   
        self.tabview.add("Admini")
        self.tabview.add("Lekari")

        self.tabview.tab("Admini").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Lekari").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Admini").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Lekari").grid_rowconfigure(0, weight=1)

        self.tab_label_admini = ctk.CTkLabel(master=self.tabview.tab("Admini"), text="Click search to start!")
        self.tab_label_admini.grid(row=0, column=0, padx=40, pady=20, sticky="nw")

        self.tab_label_lekari = ctk.CTkLabel(master=self.tabview.tab("Lekari"), text="Click search to start!")
        self.tab_label_lekari.grid(row=0, column=0, padx=40, pady=20, sticky="nw")
    
    def initialize_button_frame(self):
        self.button_frame = ctk.CTkFrame(master=self.master_frame)
        self.button_frame.grid(row=1, column=0, sticky="nsew")

        self.button_frame.grid_columnconfigure((0, 1, 2, 4), weight=0)
        self.button_frame.grid_columnconfigure(3, weight=1)
        self.button_frame.grid_rowconfigure(0, weight=1)

        self.search_button = ctk.CTkButton(master=self.button_frame, corner_radius=15, width=10, text="Search", command=self.search_users)
        self.search_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsw")

        self.find_button = ctk.CTkButton(master=self.button_frame, corner_radius=15, width=10, text="View", command=self.view_records)
        self.find_button.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsw")

        self.add_button = ctk.CTkButton(master=self.button_frame, corner_radius=15, width=10, text="Add", command=self.add_user)
        self.add_button.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="nsw")

        self.logout_button = ctk.CTkButton(master=self.button_frame, corner_radius=15, width=10, text="Logout", command=self.logout)
        self.logout_button.grid(row=0, column=4, padx=(10, 10), pady=(10, 10), sticky="nse")
    
    def change_appearance(self, new_appearance: str):
        ctk.set_appearance_mode(new_appearance)
    
    def logout(self):
        self.app.restore_login()
        self.destroy()

    def quit_app(self):
        self.app.app.destroy()
    
    def search_users(self):
        if self.tabview.get() == "Admini":
            self.initialize_choose_frame("Admini")
            with open(ADMINS_JSON_PATH, 'r') as file:
                data = json.load(file)
            out = []
            for admin in data:
                out.append(admin["username"])
            if len(out) == 0:
                self.choose_frame_admin.destroy()
            else:
                self.outbar_admin.configure(values=out)
        else:
            self.initialize_choose_frame("Lekari")
            with open(LEKARI_JSON_PATH, 'r') as file:
                data = json.load(file)
            out = []
            for lekar in data:
                out.append(lekar["username"])
            if len(out) == 0:
                self.choose_frame_lekar.destroy()
            else:
                self.outbar_lekar.configure(values=out)
    
    def initialize_choose_frame(self, tab):
        if tab == "Admini":
            self.choose_frame_admin = ctk.CTkFrame(master=self.tab_label_admini)
            self.choose_frame_admin.grid(row=0, column=0, sticky="new")

            self.choose_frame_admin.grid_rowconfigure(0, weight=0)
            self.choose_frame_admin.grid_columnconfigure(0, weight=1)

            self.outbar_admin = ctk.CTkOptionMenu(master=self.choose_frame_admin, values=["usernames"])
            self.outbar_admin.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew") 
        else:
            self.choose_frame_lekar = ctk.CTkFrame(master=self.tab_label_lekari)
            self.choose_frame_lekar.grid(row=0, column=0, sticky="new")

            self.choose_frame_lekar.grid_rowconfigure(0, weight=0)
            self.choose_frame_lekar.grid_columnconfigure(0, weight=1)

            self.outbar_lekar = ctk.CTkOptionMenu(master=self.choose_frame_lekar, values=["usernames"])
            self.outbar_lekar.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")  
    def view_records(self):
        if self.tabview.get() == "Admini":
            option = self.outbar_admin.get()
            if option != "usernames":
                admin = get_admin_by_username(option)
                if admin != None:
                    start_admin_view(self, admin)
        else:
            option = self.outbar_lekar.get()
            if option != "usernames":
                lekar = get_lekar_by_username(option)
                if lekar != None:
                    start_lekar_view(self, lekar)
    
    def edit_password(self):
        start_admin_view(self, self.user)
    
    def add_user(self):
        add_user_window = AddUser(self)

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