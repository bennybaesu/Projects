from tkinter import *

import Fonts
import FrameSwitch
import CreateAccount


def switch_frame(self, frame_class):
    new_frame = frame_class(self)
    if self._frame is not None:
        self._frame.destroy()
    self._frame = new_frame
    self._frame.pack()


class MainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.root = master
        self.root.title("Benjamin's School Planner")
        # TODO: get an icon and find the path of it
        # master.iconbitmap('HERE SHOULD GO THE FILE PATH TO THE ICON')

        # Master window dimensions
        app_width = 1000
        app_height = 500

        screen_width = master.winfo_screenwidth()  # Get screen width
        screen_height = master.winfo_screenheight()  # Get screen height

        x = int((screen_width / 2) - (app_width / 2))  # X coordinate to center application
        y = int((screen_height / 2) - (app_height / 2))  # Y coordinate to center application

        master.geometry(f'{app_width}x{app_height}+{x}+{y}')  # Set master geometry

        # Set and display welcome message
        welcome_label = Label(self.root, text='Welcome to the School Planner', font=Fonts.welcomeFont())
        welcome_label.pack()

        # Set and display username prompt
        username_label = Label(self.root, text='Username', font=Fonts.loginFont())
        username_label.place(relx=0.4, rely=0.4, anchor='center')
        username_entry = Entry(self.root)
        username_entry.place(relx=0.55, rely=0.4, anchor='center')

        # Set and display username prompt
        password_label = Label(self.root, text='Password', font=Fonts.loginFont())
        password_label.place(relx=0.4, rely=0.5, anchor='center')

        password_entry = Entry(self.root, show="\u2022")
        password_entry.place(relx=0.55, rely=0.5, anchor='center')

        # Login button command:
        def login():
            print("Logged in Successfully")

        # Login button creation:
        login_button = Button(text='Login',
                                 command=lambda: FrameSwitch.SampleApp.switch_frame(self.root,
                                                                                    CreateAccount.CreateAccount),
                                 bg='Gray', fg='Black', font=Fonts.loginFont())
        login_button.place(relx=0.5, rely=0.62, anchor='center')

        # 'Show Password' Checkbox creation
        checkboxVar = IntVar()

        def showPassword():
            if checkboxVar.get() == 1:
                password_entry.config(show="")
                password_entry.update()
            elif checkboxVar.get() == 0:
                password_entry.config(show="\u2022")

        show_password_checkbox = Checkbutton(master,
                                                text="Show Password",
                                                font=Fonts.showPasswordFont(),
                                                variable=checkboxVar,
                                                command=showPassword)
        show_password_checkbox.place(relx=0.5, rely=0.7, anchor='center')
