
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned.pack(fill=tk.BOTH, expand=1)

frame1 = ttk.Frame(paned, width=400, height=300, relief=tk.RAISED)
frame2 = ttk.Frame(paned, width=400, height=300, relief=tk.RAISED)

paned.add(frame1)
paned.add(frame2)

label = tk.Label(frame2, text="Bienvenu au menu principal", width=100)
label.pack()

root.mainloop()
