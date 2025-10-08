import customtkinter as ctk
from gui.views.View import View
from utils.Utils import setup_appearance_mode
from utils.Utils import get_pacijent_by_jmbg, get_dijagnoza_by_sifra
from utils.Utils import get_all_dijagnoze_data, get_all_pacijenti_data, is_valid_jmbg
from gui.records.DijagnozaRecords import start_session as start_dijagnoza_view
from gui.records.PacijentRecords import start_session as start_pacijent_view
import base64

class LekarView(View):
    def __init__(self, app, user):
        self.lekar = user
        self.role = "Lekar"
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

        self.initialize_choose_frame("Pacijenti")

    def initialize_sidebar(self):
        super().initialize_sidebar()
    
    def initialize_choose_frame(self, tab):
        if tab == "Pacijenti":
            self.choose_frame_pacijent = ctk.CTkFrame(master=self.tab_label_pacijenti)
            self.choose_frame_pacijent.grid(row=0, column=0, sticky="new")

            self.choose_frame_pacijent.grid_rowconfigure(0, weight=0)
            self.choose_frame_pacijent.grid_columnconfigure(0, weight=1)

            self.outbar_jmbg = ctk.CTkEntry(master=self.choose_frame_pacijent, placeholder_text="jmbg pacijenta")
            self.outbar_jmbg.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew") 
        else:
            self.choose_frame_dijagnoza = ctk.CTkFrame(master=self.tab_label_dijagnoze)
            self.choose_frame_dijagnoza.grid(row=0, column=0, sticky="new")

            self.choose_frame_dijagnoza.grid_rowconfigure(0, weight=0)
            self.choose_frame_dijagnoza.grid_columnconfigure(0, weight=1)

            self.outbar_dijagnoza = ctk.CTkOptionMenu(master=self.choose_frame_dijagnoza, values=["sifra"])
            self.outbar_dijagnoza.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def view_records(self):
        if self.tabview.get() == "Pacijenti":
            option = self.outbar_jmbg.get()
            if is_valid_jmbg(option):
                pacijent = get_pacijent_by_jmbg(option)
                if pacijent != None:
                    start_pacijent_view(self, pacijent)
        else:
            option = self.outbar_dijagnoza.get()
            if option != "sifre":
                dijagnoza = get_dijagnoza_by_sifra(option)
                if dijagnoza != None:
                    start_dijagnoza_view(self, dijagnoza)  
    
    def search_users(self):
        if self.tabview.get() == "Pacijenti":
            if is_valid_jmbg(self.outbar_jmbg.get()):
                data = get_all_pacijenti_data()
                sample = base64.b64encode(self.outbar_jmbg.get().encode("utf-8"))
                for pacijent in data:
                    if pacijent["jmbg"].encode("utf-8") == sample:
                        start_pacijent_view(self, pacijent)
                        return
                self.outbar_jmbg.configure(placeholder_text = "Pacijent not found.")
            else:
                self.outbar_jmbg.configure(placeholder_text = "Invalid JMBG.")
        else:
            self.initialize_choose_frame("Dijagnoze")
            data = get_all_dijagnoze_data()
            out = []
            for dijagnoza in data:
                out.append(dijagnoza["sifra"])
            if len(out) == 0:
                self.choose_frame_dijagnoza.destroy()
            else:
                self.outbar_dijagnoza.configure(values=out)

def start_lekar_session(app, user, validated=False):
    if validated:
        setup_appearance_mode(ctk)
        app.login_window.withdraw()
        LekarView(app, user)
    else:
        return