import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from utils.Utils import count_admini, count_lekari, count_specijalizacije, count_krvne_grupe, count_godine_pacijenata, form_starosne_grupe

class Stats(ctk.CTkToplevel):
    WINDOW_WIDTH=300
    WINDOW_HEIGHT=300
    def __init__(self, master):
        self.role = master.role
        super().__init__(master)

        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.initialize_main_frame()
    
    def initialize_main_frame(self):
        self.tabview = ctk.CTkTabview(master=self)
        self.tabview.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        if self.role == "Admin":
            self.tabview.add("Raspodela")
            self.tabview.add("Specijalizacije")

            self.tabview.tab("Raspodela").grid_columnconfigure(0, weight=1)
            self.tabview.tab("Specijalizacije").grid_columnconfigure(0, weight=1)
            self.tabview.tab("Raspodela").grid_rowconfigure(0, weight=1)
            self.tabview.tab("Specijalizacije").grid_rowconfigure(0, weight=1)

            self.initialize_raspodela()
            self.initialize_specijalizacije()
        else:
            self.tabview.add("Krvne grupe")
            self.tabview.add("Starosne grupe")

            self.tabview.tab("Krvne grupe").grid_columnconfigure(0, weight=1)
            self.tabview.tab("Starosne grupe").grid_columnconfigure(0, weight=1)
            self.tabview.tab("Krvne grupe").grid_rowconfigure(0, weight=1)
            self.tabview.tab("Starosne grupe").grid_rowconfigure(0, weight=1)

            self.initialize_krvne_grupe()
            self.initialize_starosne_grupe()
    
    def initialize_raspodela(self):
        br_admina = count_admini()
        br_lekara = count_lekari()

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie([br_admina, br_lekara], labels=["Admini", "Lekari"], explode=(0, 0.1), shadow=True)
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self.tabview.tab("Raspodela"))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nswe")
    
    def initialize_specijalizacije(self):
        data = count_specijalizacije()
        labels = [item[0] for item in data]
        counts = [item[1] for item in data]

        fig, ax = plt.subplots()
        ax.bar(labels, counts, color="#3399ff")
        ax.set_title("Raspodela Lekara po Specijalizacijama")
        ax.set_ylabel("Broj Lekara")
        ax.set_xlabel("Specijalizacije")

        plt.setp(ax.get_xticklabels(), rotation=0, ha='center')

        canvas = FigureCanvasTkAgg(fig, master=self.tabview.tab("Specijalizacije"))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nswe")

    def initialize_krvne_grupe(self):
        data = count_krvne_grupe()
        labels = [item[0] for item in data]
        counts = [item[1] for item in data]

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(counts, labels=labels, shadow=True)
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self.tabview.tab("Krvne grupe"))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nswe")

    def initialize_starosne_grupe(self):
        data = form_starosne_grupe(count_godine_pacijenata())
        labels = [item for item in data[0]]
        counts = [item for item in data[1]]

        fig, ax = plt.subplots()
        ax.bar(labels, counts, color="#ac0265")
        ax.set_title("Raspodela Pacijenata po Starosnim Grupama")
        ax.set_ylabel("Broj Pacijenata")
        ax.set_xlabel("Starosne grupe")

        plt.setp(ax.get_xticklabels(), rotation=0, ha='center')

        canvas = FigureCanvasTkAgg(fig, master=self.tabview.tab("Starosne grupe"))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nswe")

    def quit_app(self):
        self.destroy()


def start_session(controller):
    Stats(controller)