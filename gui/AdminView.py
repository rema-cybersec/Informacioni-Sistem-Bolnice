from gui.View import View
import customtkinter as ctk

class AdminView(View):
    def __init__(self, app, user):
        super().__init__(app, user)



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