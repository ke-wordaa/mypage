from tkinter import * #import all the library of the tkinter module
import tkinter as tk
input_root = Tk()
input_root.geometry('800x600')
input_text = Entry(input_root,bd=1,highlightcolor='red').grid()
input_root.mainloop()