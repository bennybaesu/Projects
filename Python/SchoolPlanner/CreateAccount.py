from tkinter import *

import Fonts


class CreateAccount(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        #master.title("Create Account")
        master.config(bg='blue')

        # Master window dimensions
        app_width = 1000
        app_height = 500

        #screen_width = master.winfo_screenwidth()  # Get screen width
        #screen_height = master.winfo_screenheight()  # Get screen height

        #x = int((screen_width / 2) - (app_width / 2))  # X coordinate to center application
        #y = int((screen_height / 2) - (app_height / 2))  # Y coordinate to center application

        #master.geometry(f'{app_width}x{app_height}+{x}+{y}')  # Set master geometry


        welcome_label = Label(master, text='We made it to create account', font=Fonts.welcomeFont())
        ##welcome_label.pack()