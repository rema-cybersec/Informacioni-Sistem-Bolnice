import gui.login as login

def main():
    login.setup()
    app = login.LoginWindow()
    app.mainloop()


if __name__ == "__main__":
    main()