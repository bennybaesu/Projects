import tkinter as tk

import Fonts
import CreateAccount
import tk_window

def sample2(master):
    frame = tk.Frame(master)
    quitButton = tk.Button(frame, text='Quit', width=25)
    quitButton.pack()
    frame.pack()
    return frame



class Demo2:
    def __init__(self, master):
        tk.Frame.__init__(master)
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = tk_window.App(self.newWindow)
        self.master.destroy()


class MainMenu(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.root = master
        self.root.title("Benjamin's School Planner")
        # TODO: get an icon and find the path of it
        # master.iconbitmap('HERE SHOULD GO THE FILE PATH TO THE ICON')

        # Master window dimensions
        app_width = 1000
        app_height = 500

        #screen_width = master.winfo_screenwidth()  # Get screen width
        #screen_height = master.winfo_screenheight()  # Get screen height

        #x = int((screen_width / 2) - (app_width / 2))  # X coordinate to center application
        #y = int((screen_height / 2) - (app_height / 2))  # Y coordinate to center application

        #master.geometry(f'{app_width}x{app_height}+{x}+{y}')  # Set master geometry

        # Set and display welcome message
        welcome_label = tk.Label(self.root, text='Welcome to the School Planner', font=Fonts.welcomeFont())
        #welcome_label.pack()

        # Set and display username prompt
        username_label = tk.Label(self.root, text='Username', font=Fonts.loginFont())
        username_label.place(relx=0.4, rely=0.4, anchor='center')
        username_entry = tk.Entry(self.root)
        username_entry.place(relx=0.55, rely=0.4, anchor='center')

        # Set and display username prompt
        password_label = tk.Label(self.root, text='Password', font=Fonts.loginFont())
        password_label.place(relx=0.4, rely=0.5, anchor='center')

        password_entry = tk.Entry(self.root, show="\u2022")
        password_entry.place(relx=0.55, rely=0.5, anchor='center')

        # Login button command:
        def login():
            print("Logged in Successfully")

        # Login button creation:
        login_button = tk.Button(text='Login',
                              command=lambda: login(),
                              bg='Gray', fg='Black', font=Fonts.loginFont())
        login_button.place(relx=0.5, rely=0.62, anchor='center')

        # 'Show Password' Checkbox creation
        checkboxVar = tk.IntVar()

        def showPassword():
            if checkboxVar.get() == 1:
                password_entry.config(show="")
                password_entry.update()
            elif checkboxVar.get() == 0:
                password_entry.config(show="\u2022")

        show_password_checkbox = tk.Checkbutton(master,
                                             text="Show Password",
                                             font=Fonts.showPasswordFont(),
                                             variable=checkboxVar,
                                             command=showPassword)
        show_password_checkbox.place(relx=0.5, rely=0.7, anchor='center')

        # Create Account button creation:
        create_account_button = tk.Button(text='Create Account',
                              command=lambda: controller.show_frame("CreateAccount"),
                              bg='Gray', fg='Black', font=Fonts.createAccountFont())
        create_account_button.place(relx=0.5, rely=0.7, anchor='center')
