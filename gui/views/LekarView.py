import customtkinter as ctk
from gui.views.View import View
from utils.Utils import setup_appearance_mode
from utils.Utils import get_pacijent_by_jmbg, get_dijagnoza_by_sifra
from gui.records.DijagnozaRecords import start_session as start_dijagnoza_view
from gui.records.PacijentRecords import start_session as start_pacijent_view

class LekarView(View):
    def __init__(self, app, user):
        self.lekar = user
        super().__init__(app, user)
    
    def initialize_users_frame(self):
        super().initialize_users_frame()
        self.tabview.add("Pacijenti")
        self.tabview.add("Dijagnoze")

        self.tabview.tab("Pacijenti").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Dijagnoze").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Pacijenti").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Dijagnoze").grid_rowconfigure(0, weight=1)

        self.tab_label_pacijenti = ctk.CTkLabel(master=self.tabview.tab("Pacijenti"), text="Click search to start!")
        self.tab_label_pacijenti.grid(row=0, column=0, padx=40, pady=20, sticky="nw")

        self.tab_label_dijagnoze = ctk.CTkLabel(master=self.tabview.tab("Dijagnoze"), text="Click search to start!")
        self.tab_label_dijagnoze.grid(row=0, column=0, padx=40, pady=20, sticky="nw")

    def initialize_sidebar(self):
        super().initialize_sidebar()
    
    def initialize_choose_frame(self, tab):
        if tab == "Pacijenti":
            self.choose_frame_pacijent = ctk.CTkFrame(master=self.tab_label_pacijenti)
            self.choose_frame_pacijent.grid(row=0, column=0, sticky="new")

            self.choose_frame_pacijent.grid_rowconfigure(0, weight=0)
            self.choose_frame_pacijent.grid_columnconfigure(0, weight=1)

            self.outbar_pname = ctk.CTkOptionMenu(master=self.choose_frame_pacijent, values=["names"])
            self.outbar_pname.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew") 
        else:
            self.choose_frame_dijagnoza = ctk.CTkFrame(master=self.tab_label_dijagnoze)
            self.choose_frame_dijagnoza.grid(row=0, column=0, sticky="new")

            self.choose_frame_dijagnoza.grid_rowconfigure(0, weight=0)
            self.choose_frame_dijagnoza.grid_columnconfigure(0, weight=1)

            self.outbar_dijagnoza = ctk.CTkOptionMenu(master=self.choose_frame_dijagnoza, values=["sifra"])
            self.outbar_dijagnoza.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def view_records(self):
        if self.tabview.get() == "Pacijenti":
            option = self.outbar_pacijent.get()
            if option != "usernames":
                pacijent = get_pacijent_by_jmbg(option)
                if pacijent != None:
                    start_pacijent_view(self, pacijent)
        else:
            option = self.outbar_dijagnoza.get()
            if option != "sifre":
                dijagnoza = get_dijagnoza_by_sifra(option)
                if dijagnoza != None:
                    start_dijagnoza_view(self, dijagnoza)  

def start_lekar_session(app, user, validated=False):
    if validated:
        setup_appearance_mode(ctk)
        app.login_window.withdraw()
        LekarView(app, user)
    else:
        return