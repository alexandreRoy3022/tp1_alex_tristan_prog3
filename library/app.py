from tkinter import *
from tkinter.ttk import Combobox

import chess

from action.partie import Partie
from action.catalogue import Catalogue
from action.catalogue_pgn import CataloguePgn


class Application:
    def __init__(self):
        self.protocole_modifier_partie = None
        self.root = Tk()

        self.panedwindow = PanedWindow(self.root)

        self.image_de_decoration = PhotoImage(file="../—Pngtree—black and white chess board_5983396.png")

        self.frame1 = Frame(self.panedwindow, width=400, height=300, relief=RAISED, background="lightgrey")
        self.frame2 = Frame(self.panedwindow, width=400, height=300, relief=RAISED)

        self.panedwindow.add(self.frame1)
        self.panedwindow.add(self.frame2)

        self.titre = Label(self.frame2, text="Bienvenu au menu principal", font=("Helvetica", 60))
        self.texte_sous_le_titre = Label(self.frame2, text="Veuillez cliquer sur l'option que vous désirez à gauche")
        self.titre.grid(column=0, row=0, columnspan=2)
        self.texte_sous_le_titre.grid(column=0, row=1, columnspan=2)

        self.message_avertissement = Label(self.frame2, text="", fg="red")
        self.message_avertissement.grid(column=0, row=2, columnspan=2)

        self.arriere_plan_frame_1 = Label(self.frame1, image=self.image_de_decoration)

        #self.bouton_ajouter_partie = Button(self.frame1, text="Ajouter partie", image=self.image_de_decoration, compound="top", command=self.protocole_ajout_partie)
        #self.bouton_modifier_partie = Button(self.frame1, text="Modifier Partie", image=self.image_de_decoration, compound="top", command=print("modifier"))
        #self.bouton_supprimer_partie = Button(self.frame1, text="Supprimer Partie", image=self.image_de_decoration, compound="top", command=print("supprimer"))
        #self.bouton_quitter = Button(self.frame1, text="Quitter", bg="red", fg="white", command=self.root.destroy)
        self.bouton_ajouter_partie = Button(self.frame1, text="Ajouter partie", compound="top", command=self.protocole_ajout_partie)
        self.bouton_modifier_partie = Button(self.frame1, text="Modifier Partie", compound="top", command=self.protocole_modifier_partie)
        self.bouton_supprimer_partie = Button(self.frame1, text="Supprimer Partie", compound="top", command=print("supprimer"))
        self.bouton_quitter = Button(self.frame1, text="Quitter", bg="red", fg="white", command=self.root.destroy)


        self.panedwindow.pack(fill=BOTH, expand=True)

        self.bouton_ajouter_partie.place(relx=0.5, rely=0.4, anchor="center")
        self.bouton_modifier_partie.place(relx=0.5, rely=0.5, anchor="center")
        self.bouton_supprimer_partie.place(relx=0.5, rely=0.6, anchor="center")
        self.bouton_quitter.place(relx=1.0, rely=0.0, anchor="ne")

        self.mon_catalogue = CataloguePgn()

        self.mon_catalogue.lire("..\\action\\data\\chess.pgn")

    def protocole_ajout_partie(self):
        self.titre.grid_forget()
        self.texte_sous_le_titre.grid_forget()

        self.bouton_ajouter_partie.config(state=DISABLED)
        self.bouton_modifier_partie.config(state=DISABLED)
        self.bouton_supprimer_partie.config(state=DISABLED)


        lblTitre = Label(self.frame2, text="Veuillez répondre à chaque entrée ci-dessous")
        lblTitre.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.message_avertissement.grid(column=0, row=2, columnspan=2)

        lbl_nom_joueur_blanc = Label(self.frame2, text="Nom du joueur blanc:")
        self.input_nom_joueur_blanc = Entry(self.frame2)
        lbl_nom_joueur_blanc.grid(column=0, row=4)
        self.input_nom_joueur_blanc.grid(column=1, row=4)

        lbl_nom_joueur_noir = Label(self.frame2, text="Nom du joueur noir:")
        self.input_nom_joueur_noir = Entry(self.frame2)
        lbl_nom_joueur_noir.grid(column=0, row=5)
        self.input_nom_joueur_noir.grid(column=1, row=5)

        lbl_date_partie = Label(self.frame2, text="Date de la partie:")
        self.input_date_partie = Entry(self.frame2)
        lbl_date_partie.grid(column=0, row=6)
        self.input_date_partie.grid(column=1, row=6)

        lbl_elo_blanc = Label(self.frame2, text="Elo du joueur blanc:")
        self.input_elo_blanc = Entry(self.frame2)
        lbl_elo_blanc.grid(column=0, row=7)
        self.input_elo_blanc.grid(column=1, row=7)

        lbl_elo_noir = Label(self.frame2, text="Elo du joueur noir:")
        self.input_elo_noir = Entry(self.frame2)
        lbl_elo_noir.grid(column=0, row=8)
        self.input_elo_noir.grid(column=1, row=8)

        lbl_type_partie = Label(self.frame2, text="Type de partie:")
        n = StringVar()
        self.input_type_partie = Combobox(self.frame2, width=17, textvariable=n)

        # Adding combobox drop down list
        self.input_type_partie['values'] = (' Type 1',
                                            ' Type 2')

        lbl_type_partie.grid(column=0, row=9)
        self.input_type_partie.grid(column=1, row=9)

        lbl_duration_partie = Label(self.frame2, text="Durée de la partie:")
        self.input_duration_partie = Entry(self.frame2)
        lbl_duration_partie.grid(column=0, row=10)
        self.input_duration_partie.grid(column=1, row=10)

        lbl_resultat_partie = Label(self.frame2, text="Résultat de la partie:")
        self.input_resultat_partie = Entry(self.frame2)
        lbl_resultat_partie.grid(column=0, row=11)
        self.input_resultat_partie.grid(column=1, row=11)

        lbl_nom_ouverture = Label(self.frame2, text="Nom ouverture:")
        self.input_nom_ouverture = Entry(self.frame2)
        lbl_nom_ouverture.grid(column=0, row=12)
        self.input_nom_ouverture.grid(column=1, row=12)

        lbl_deplacements = Label(self.frame2, text="Déplacements:")
        self.input_deplacements = Entry(self.frame2)
        lbl_deplacements.grid(column=0, row=13)
        self.input_deplacements.grid(column=1, row=13)

        but_ajouter_partie = Button(self.frame2, text="Ajouter Partie", command=self.ecrire_infos_dans_fichier)
        but_ajouter_partie.grid(column=0, row=14, padx=10, pady=10, sticky=W)
        but_retourner_accueil = Button(self.frame2, text="Retourner à la page d'accueil", command=self.retourner_page_accueil)
        but_retourner_accueil.grid(column=1, row=14, padx=10, pady=10, sticky=W)

    def retourner_page_accueil(self):
        for widget in self.frame2.winfo_children():
            widget.grid_forget()

        self.titre.grid(column=0, row=0, columnspan=2)
        self.texte_sous_le_titre.grid(column=0, row=1, columnspan=2)

        self.bouton_ajouter_partie.config(state=NORMAL)
        self.bouton_modifier_partie.config(state=NORMAL)
        self.bouton_supprimer_partie.config(state=NORMAL)

    def ecrire_infos_dans_fichier(self):
        nom_joueur_blanc = self.input_nom_joueur_blanc.get()
        nom_joueur_noir = self.input_nom_joueur_noir.get()
        date_partie = self.input_date_partie.get()
        elo_blanc = self.input_elo_blanc.get()
        elo_noir = self.input_elo_noir.get()
        type_partie = self.input_type_partie.get()
        duration_partie = self.input_duration_partie.get()
        resultat_partie = self.input_resultat_partie.get()
        nom_ouverture = self.input_nom_ouverture.get()
        deplacements = self.input_deplacements.get().split()

        if not all([nom_joueur_blanc, nom_joueur_noir, date_partie, elo_blanc, elo_noir, type_partie, duration_partie, resultat_partie]):
            self.message_avertissement.config(text="Veuillez remplir les informations demandées manquantes")
            return

        nouv_partie = Partie()
        nouv_partie.Nom_joueur_black = nom_joueur_noir
        nouv_partie.Nom_joueur_white = nom_joueur_blanc
        nouv_partie.date_partie = nom_joueur_noir
        nouv_partie.niveau_joueur_white = elo_blanc
        nouv_partie.niveau_joueur_black = elo_noir
        nouv_partie.type_partie = type_partie
        nouv_partie.duree_partie = duration_partie
        nouv_partie.resultat_partie = resultat_partie
        nouv_partie.nom_ouverture = nom_ouverture

        board = chess.Board()
        for deplacement in deplacements:
            move_complet = board.push_san(deplacement)
            nouv_partie.ajouter_deplacement(move_complet)

        self.mon_catalogue.ajouter_partie(nouv_partie)
        self.mon_catalogue.ecrire()

        self.input_nom_joueur_blanc.delete(0, END)
        self.input_nom_joueur_noir.delete(0, END)
        self.input_date_partie.delete(0, END)
        self.input_elo_blanc.delete(0, END)
        self.input_elo_noir.delete(0, END)
        self.input_type_partie.delete(0, END)
        self.input_duration_partie.delete(0, END)
        self.input_resultat_partie.delete(0, END)
        self.input_nom_ouverture.delete(0, END)
        self.input_deplacements.delete(0, END)

        self.bouton_ajouter_partie.config(state=NORMAL)
        self.bouton_modifier_partie.config(state=NORMAL)
        self.bouton_supprimer_partie.config(state=NORMAL)
        self.bouton_quitter.config(state=NORMAL)

    def lancer_application(self):
        self.root.mainloop()
