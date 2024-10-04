
import tkinter as tk
from tkinter import Label, Button, PanedWindow, Frame

from action.db import Database

class Application:
    root = tk.Tk()
    paned = PanedWindow(root, orient=tk.HORIZONTAL)
    paned.pack(fill=tk.BOTH, expand=1)

    frame1 = Frame(paned, width=400, height=300, relief=tk.RAISED)
    frame2 = Frame(paned, width=400, height=300, relief=tk.RAISED)

    paned.add(frame1)
    paned.add(frame2)

    label = Label(frame2, text="Bienvenu au menu principal", font=("Helvetica", 60))
    label.pack()


    bouton_ajouter_partie = Button(frame1, text="Ajouter partie", command=Database.ajouter_partie)
    bouton_ajouter_partie.pack()


    bouton_modifier_partie = Button(frame1, text="Modifier Partie", command=Database.modifier_partie)
    bouton_modifier_partie.pack()

    bouton_supprimer_partie = Button(frame1, text="Supprimer Partie", command=Database.supprimer_partie)
    bouton_supprimer_partie.pack()

root.mainloop()
