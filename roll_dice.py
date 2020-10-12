from tkinter import *
from tkinter import ttk
import random

class GUI:
    def __init__(self, master=None):
        master.geometry('640x480')
        master.resizable(False, False)
        menubar = Menu(master)
        master.config(menu = menubar)
        file = Menu(menubar)
        window = Menu(menubar)

        menubar.add_cascade(menu = file, label = 'File')
        menubar.add_cascade(menu = window, label = 'Window')

        file.add_command(label = 'Open')
        file.add_command(label = 'Save')
        res = Menu(window)
        window.add_cascade(window = res, label = 'Resolution')
        res.add_command(label = '480x360', command = lambda e: self.change_resolution('1'))
        res.add_command(label = '640x480', command = lambda e: self.change_resolution('2'))
        res.add_command(label = '1280x720', command = lambda e: self.change_resolution('3'))
        res.add_command(label = '1600x900', command = lambda e: self.change_resolution('4'))
        colour = Menu(window)
        window.add_cascade(window = colour, label = "Background Colour")
        colour.add_command(label = 'First')
        colour.add_command(label = 'Second')
        colour.add_command(label = 'Third')
        colour.add_command(label = 'Custom')

        #functionality of menu

    
    
    def rolldice(self, range):
        return random.randrange(range)
    def change_resolution(self, res):
        if res == '1':
            master.geometry('480x360')
        elif res == '2':
            master.geometry('640x480')
        elif res == '3':
            master.geometry('1280x720')
        elif res == '4':
            master.geometry('1600x900')


def main():            
    
    root = Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__": main()