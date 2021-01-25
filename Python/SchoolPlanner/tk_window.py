"""Author: Benjamin Baesu.
TkWindow acts as the initialization zone for the GUI.
The class below holds the window information and acts as a zone
to switch between frames."""
import tkinter as tk
import mainMenu


class App:
    """This class acts as the initial point of entry of the GUI.
    It holds window dimension information, as well as information about
    each frame."""
    def __init__(self, master):
        """Application Constructor"""
        self.master = master

        # Master window dimensions
        app_width = 1000
        app_height = 500
        screen_width = master.winfo_screenwidth()  # Get screen width
        screen_height = master.winfo_screenheight()  # Get screen height
        x = int((screen_width / 2) - (app_width / 2))  # X coordinate to center application
        y = int((screen_height / 2) - (app_height / 2))  # Y coordinate to center application
        self.master.geometry(f'{app_width}x{app_height}+{x}+{y}')  # Set master geometry

        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text='New Window', width=25, command=lambda: self.raise_frame(mainMenu.sample2(self.master)))
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        """Creates a new Top Level window"""
        new_window = tk.Toplevel(self.master)
        mainMenu.Demo2(new_window)

    def raise_frame(self, fr):
        self.frame.pack_forget()
        self.frame = fr
        #self.frame.pack_forget()



