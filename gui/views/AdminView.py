from gui.views.View import View
from utils.Utils import setup_appearance_mode
from utils.Utils import get_admin_by_username, get_lekar_by_username
from utils.Utils import get_all_admin_data, get_all_lekar_data
from gui.records.AdminRecords import start_session as start_admin_view
from gui.records.LekarRecords import start_session as start_lekar_view
import customtkinter as ctk

class AdminView(View):
    def __init__(self, app, user):
        self.role = "Admin"
        super().__init__(app, user)
        
        self.title("AdminView")

    def initialize_sidebar(self):
        super().initialize_sidebar()

        self.change_password = ctk.CTkButton(master=self.sidebar, corner_radius=15, text="change password", command=self.edit_password)
        self.change_password.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="sew")
    
    def initialize_users_frame(self):
        super().initialize_users_frame()
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
    def search_users(self):
        if self.tabview.get() == "Admini":
            self.initialize_choose_frame("Admini")
            data = get_all_admin_data()
            out = []
            for admin in data:
                out.append(admin["username"])
            if len(out) == 0:
                self.choose_frame_admin.destroy()
            else:
                self.outbar_admin.configure(values=out)
        else:
            self.initialize_choose_frame("Lekari")
            data = get_all_lekar_data()
            out = []
            for lekar in data:
                out.append(lekar["username"])
            if len(out) == 0:
                self.choose_frame_lekar.destroy()
            else:
                self.outbar_lekar.configure(values=out)

def start_admin_session(app, user, validated=False):
    if validated:
        setup_appearance_mode(ctk)
        app.login_window.withdraw()
        AdminView(app, user)
    else:
        return