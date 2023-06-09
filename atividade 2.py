from tkinter import *
from tkinter import ttk
root = Tk()
root = ttk.Frame(root, padding=10)
root.grid()
ttk.Label(root, text="Ola mundo!").grid(column=0, row=0)
ttk.Button(root, text="Sair", command=root.destroy).grid(column=1, row=0)
root.mainloop()