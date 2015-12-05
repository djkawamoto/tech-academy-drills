#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
# jobJournal.py

import tkinter
from tkinter import ttk
from tkinter import messagebox as mb
# import os as os
# import datetime
# import csv

'''
Don't forget to set the default values of the comboboxes!!!
Rewrite to include proper use of classes and separate GUI setup from init function.
check the linda example using pack and grid together.
'''


class MainApp:

    def __init__(self, master):
        master.title("DAILY JOB JOURNAL")
        self.style = ttk.Style()

        # self.frame_content = ttk.Frame(master)
        # self.frame_content.grid()

        # job label
        ttk.Label(master, text="Job #:").grid(row=0, column=0, sticky="W")
        # job text entry box
        self.job = ttk.Entry(master)
        self.job.grid(row=1, column=0)

        # project label
        ttk.Label(master, text="Project:").grid(row=0, column=1, sticky="W")
        # project text entry box
        self.project = ttk.Entry(master)
        self.project.grid(row=1, column=1, columnspan=2)

        # start label
        ttk.Label(master, text="Start").grid(row=2, column=0, sticky="W")
        # start combobox
        self.start = ttk.Combobox(master)
        self.start.grid(row=3, column=0)

        # stop label
        ttk.Label(master, text="Stop").grid(row=2, column=1, sticky="W")
        # stop combobox
        self.stop = ttk.Combobox(master)
        self.stop.grid(row=3, column=1)

        # notes label
        ttk.Label(master, text="Notes:").grid(row=4, column=0, sticky="W")
        # notes text entry box
        self.notes = ttk.Entry(master)
        # , rowspan = 5, columnspan = 3)
        self.notes.grid()#row=5, column=0, rowspan=5, columnspan=3 sd)

        # submit button
        submit_button = ttk.Button(master, text="Submit").grid(row=3, column=2)
        # submit_button.grid(master, row=3, column=2) #, text="Submit"

    def submit(self):
        # write to CSV
        # clear form
        date_submitted = 'THE DATE NEEDS TO BE CHANGED'  # Get value of date combobox
        mb.showinfo(title='Success!', message='Your entry for ' +
                    date_submitted + ' has been submitted.')

    def clear(self):
        self.notes.delete(1.0, 'end')


def main():
    root = tkinter.Tk()
    MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    # root = Tk()
    # mainapp = MainApp(root)
    # root.mainloop()