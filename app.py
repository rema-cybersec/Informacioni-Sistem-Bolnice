import gui.Login as login
import customtkinter as ctk

class App:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.withdraw()
        login.setup()
        self.login_window = login.LoginWindow(self.app)

    def restore_login(self):
        self.login_window.deiconify()
    
    def run(self):
        self.app.mainloop()


def main():
   app = App()
   app.run()


if __name__ == "__main__":
    main()