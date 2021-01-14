from tkinter import *

import mainMenu

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

        self.mainMenu = mainMenu.MainMenu(self.master)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def start(self):
        #self.switch_frame(self.mainMenu)
        self.master.mainloop()

