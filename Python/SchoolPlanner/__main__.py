"""School Planner Application
    Author: Benjamin Baesu
    Language: Python 3
    2021"""
import tkinter as tk
import tk_window


def main():
    """This application begins the loop that is used later in 'TkWindow'"""
    root = tk.Tk()
    tk_window.App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
