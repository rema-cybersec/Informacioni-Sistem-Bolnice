import customtkinter as ctk
from gui.views.View import View
from utils.Utils import setup_appearance_mode

class LekarView(View):
    def __init__(self, app, user):
        self.lekar = user
        super().__init__(app, user)


def start_lekar_session(app, user, validated=False):
    if validated:
        setup_appearance_mode(ctk)
        app.login_window.withdraw()
        LekarView(app, user)
    else:
        return