from tkinter import *

import mainMenu
import CreateAccount


class TkWindow:
    def __init__(self):
        self.master = Tk()  # Makes the window
        self.master.wm_title("School Planner")
        self.master.config(background="#FFFFFF")

        # Master window dimensions
        app_width = 1000
        app_height = 500

        screen_width = self.master.winfo_screenwidth()  # Get screen width
        screen_height = self.master.winfo_screenheight()  # Get screen height

        x = int((screen_width / 2) - (app_width / 2))  # X coordinate to center application
        y = int((screen_height / 2) - (app_height / 2))  # Y coordinate to center application

        self.dimensions = f'{app_width}x{app_height}+{x}+{y}'

        self.master.geometry(self.dimensions)  # Set master geometry

        container = Frame(self.master, width=app_width, height=app_height, relief='raised', borderwidth=5)

        # self.currentFrame = Frames.main(self.master)

        self.frames = {}
        for F in (mainMenu.MainMenu, CreateAccount.CreateAccount):
            page_name = F.__name__
            frame = F(master=container.master, controller=self)
            self.frames[page_name] = frame

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def getRoot(self):
        return self.master
