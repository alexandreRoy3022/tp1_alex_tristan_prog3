
from tkinter import *

from action.db import Database
from action.partie import Partie


class Application:
    def __init__(self):
        self.root = Tk()
        self.panedwindow = PanedWindow()
        self.frame1 = Frame(self.panedwindow, width=400, height=300, relief=RAISED)
        self.frame2 = Frame(self.panedwindow, width=400, height=300, relief=RAISED)
        self.panedwindow.add(self.frame1)
        self.panedwindow.add(self.frame2)
        self.titre = Label(self.frame2, text="Bienvenu au menu principal", font=("Helvetica", 60))
        self.bouton_ajouter_partie = Button(self.frame1, text="Ajouter partie", command=Database.ajouter_partie)
        self.bouton_modifier_partie = Button(self.frame1, text="Modifier Partie", command=Database.modifier_partie)
        self.bouton_supprimer_partie = Button(self.frame1, text="Supprimer Partie", command=Database.supprimer_partie)
        self.panedwindow.pack(fill=BOTH, expand=True)
        self.frame1.pack()
        self.frame2.pack()
        self.titre.pack()
        self.bouton_ajouter_partie.pack()
        self.bouton_modifier_partie.pack()
        self.bouton_supprimer_partie.pack()



root.mainloop()
