from tkinter import *
from tkinter import Entry
from tkinter.ttk import Combobox


import chess
from action.partie import Partie
from action.catalogue_pgn import CataloguePgn


class Application:
    def __init__(self):
        self.root = Tk()

        self.panedwindow = PanedWindow(self.root)

        self.frame1 = Frame(self.panedwindow, width=300, height=300, relief=RAISED, background="lightgrey")
        self.frame2 = Frame(self.panedwindow, width=400, height=300, relief=RAISED)

        self.panedwindow.add(self.frame1, height=800)
        self.panedwindow.add(self.frame2, height=800)

        self.titre = Label(self.frame2, text="Bienvenue au menu principal", font=("Helvetica", 50))
        self.texte_sous_le_titre = Label(self.frame2, text="Veuillez cliquer sur l'option que vous désirez à gauche")
        self.titre.grid(column=0, row=0, columnspan=2)
        self.texte_sous_le_titre.grid(column=0, row=1, columnspan=2)

        self.message_avertissement = Label(self.frame2, text="", fg="red")
        self.message_avertissement.grid(column=0, row=2, columnspan=2)

        self.bouton_ajouter_partie = Button(self.frame1, text="Ajouter partie", compound="top", command=self.protocole_ajout_partie)
        self.bouton_modifier_partie = Button(self.frame1, text="Modifier Partie", compound="top", command=self.protocole_modifier_partie)
        self.bouton_supprimer_partie = Button(self.frame1, text="Supprimer Partie", compound="top", command=self.protocole_supprimer_partie)
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
        ctpWidget = 0


        lblTitre = Label(self.frame2, text="Veuillez répondre à chaque entrée ci-dessous")
        lblTitre.grid(column=0, row=ctpWidget, padx=10, pady=10, sticky=W)
        self.message_avertissement.grid(column=0, row=ctpWidget+1, columnspan=2)

        ctpWidget += 4
        self.input_evenement, ctpWidget = self.ajouterEntry(self.frame2, "Évenement:", ctpWidget)
        self.input_nom_joueur_blanc, ctpWidget = self.ajouterEntry(self.frame2, "Nom du joueur blanc:", ctpWidget)
        self.input_nom_joueur_noir, ctpWidget = self.ajouterEntry(self.frame2, "Nom du joueur noir:", ctpWidget)
        self.input_date_partie, ctpWidget = self.ajouterEntry(self.frame2, "Date de la partie:", ctpWidget)
        self.input_elo_blanc, ctpWidget = self.ajouterEntry(self.frame2, "Elo du joueur blanc:", ctpWidget)
        self.input_elo_noir, ctpWidget = self.ajouterEntry(self.frame2, "Elo du joueur noir:", ctpWidget)

        lbl_type_partie = Label(self.frame2, text="Type de partie:")
        n = StringVar()
        self.input_type_partie = Combobox(self.frame2, width=17, textvariable=n, state='readonly')
        self.input_type_partie['values'] = ('Classique',
                                            'Rapide')
        lbl_type_partie.grid(column=0, row=ctpWidget)
        self.input_type_partie.grid(column=1, row=ctpWidget)
        ctpWidget += 1

        self.input_duration_partie, ctpWidget = self.ajouterEntry(self.frame2, "Durée de la partie:", ctpWidget)
        self.input_resultat_partie, ctpWidget = self.ajouterEntry(self.frame2, "Résultat de la partie:", ctpWidget)
        self.input_nom_ouverture, ctpWidget = self.ajouterEntry(self.frame2, "Nom ouverture:", ctpWidget)
        self.input_deplacements, ctpWidget = self.ajouterEntry(self.frame2, "Déplacements:", ctpWidget)

        but_ajouter_partie = Button(self.frame2, text="Ajouter Partie", command=self.ecrire_infos_dans_fichier)
        but_ajouter_partie.grid(column=0, row=ctpWidget, padx=10, pady=10, sticky=W)
        but_retourner_accueil = Button(self.frame2, text="Retourner à la page d'accueil", command=self.retourner_page_accueil)
        but_retourner_accueil.grid(column=1, row=ctpWidget, padx=10, pady=10, sticky=W)

    def ajouterEntry(self, frame: Frame, titre: str, rangee: int, value="") -> tuple[Entry, int]:
        lbl = Label(frame, text=titre)
        input = Entry(frame)
        lbl.grid(column=0, row=rangee)
        input.grid(column=1, row=rangee)
        if len(value) > 0:
            input.insert(0, value)
        rangee += 1

        return input, rangee

    def protocole_modifier_partie(self):
        self.titre.grid_forget()
        self.texte_sous_le_titre.grid_forget()

        self.bouton_ajouter_partie.config(state=DISABLED)
        self.bouton_modifier_partie.config(state=DISABLED)
        self.bouton_supprimer_partie.config(state=DISABLED)

        lblTitre = Label(self.frame2, text="Veuillez sélectionner un évenement")
        lblTitre.grid(column=0, row=0, padx=10, pady=10, sticky=W)
        self.message_avertissement.grid(column=0, row=2, columnspan=2)

        lbl_evenement = Label(self.frame2, text="Évenement:")
        self.input_evenement = Combobox(self.frame2, width=17, state='readonly')
        self.input_evenement['values'] = (self.mon_catalogue.obtenir_parties())
        lbl_evenement.grid(column=0, row=4)
        self.input_evenement.grid(column=1, row=4)

        but_afficher_partie = Button(self.frame2, text="Afficher Partie", command=self.select_evenement)
        but_afficher_partie.grid(column=2, row=4, padx=10, pady=10, sticky=W)

    def select_evenement(self):
        partie = self.mon_catalogue.obtenir_une_partie(self.input_evenement.get())
        lisTypePartie = 'Classique', 'Rapide'

        if partie:
            ctpWidget = 6
            self.input_nom_joueur_blanc, ctpWidget = self.ajouterEntry(self.frame2, "Nom du joueur blanc:", ctpWidget,
                                                                       partie.Nom_joueur_white)
            self.input_nom_joueur_noir, ctpWidget = self.ajouterEntry(self.frame2, "Nom du joueur noir:", ctpWidget,
                                                                      partie.Nom_joueur_black)
            self.input_date_partie, ctpWidget = self.ajouterEntry(self.frame2, "Date de la partie:", ctpWidget,
                                                                  partie.Date_partie)
            self.input_elo_blanc, ctpWidget = self.ajouterEntry(self.frame2, "Elo du joueur blanc:", ctpWidget,
                                                                partie.Niveau_joueur_white)
            self.input_elo_noir, ctpWidget = self.ajouterEntry(self.frame2, "Elo du joueur noir:", ctpWidget,
                                                               partie.Niveau_joueur_black)

            lbl_type_partie = Label(self.frame2, text="Type de partie:")

            self.input_type_partie = Combobox(self.frame2, width=17, state='readonly')
            self.input_type_partie['values'] = lisTypePartie
            self.input_type_partie.current(lisTypePartie.index(partie.Type_partie))
            lbl_type_partie.grid(column=0, row=ctpWidget)
            self.input_type_partie.grid(column=1, row=ctpWidget)
            ctpWidget += 1

            self.input_duration_partie, ctpWidget = self.ajouterEntry(self.frame2, "Durée de la partie:", ctpWidget,
                                                                      partie.Duree_partie)
            self.input_resultat_partie, ctpWidget = self.ajouterEntry(self.frame2, "Résultat de la partie:", ctpWidget,
                                                                      partie.Resultat_partie)
            self.input_nom_ouverture, ctpWidget = self.ajouterEntry(self.frame2, "Nom ouverture:", ctpWidget,
                                                                    partie.Nom_ouverture)
            self.input_deplacements, ctpWidget = self.ajouterEntry(self.frame2, "Déplacements:", ctpWidget,
                                                                   self.merge_deplacements(partie))

            but_modifier_partie = Button(self.frame2, text="Modifier Partie", command=self.modifier_infos_dans_fichier)
            but_modifier_partie.grid(column=0, row=ctpWidget, padx=10, pady=10, sticky=W)
            but_retourner_accueil = Button(self.frame2, text="Retourner à la page d'accueil", command=self.retourner_page_accueil)
            but_retourner_accueil.grid(column=1, row=ctpWidget, padx=10, pady=10, sticky=W)

    def merge_deplacements(self, partie: Partie):
        board = chess.Board()

        resultat = ""
        for deplacement in partie.deplacement:
            resultat += board.san(deplacement) + " "

        return resultat

    def retourner_page_accueil(self):
        for widget in self.frame2.winfo_children():
            widget.grid_forget()

        self.titre.grid(column=0, row=0, columnspan=2)
        self.texte_sous_le_titre.grid(column=0, row=1, columnspan=2)

        self.bouton_ajouter_partie.config(state=NORMAL)
        self.bouton_modifier_partie.config(state=NORMAL)
        self.bouton_supprimer_partie.config(state=NORMAL)

    def modifier_infos_dans_fichier(self):
        partie = self.mon_catalogue.obtenir_une_partie(self.input_evenement.get())

        if partie:
            partie.Nom_joueur_white = self.input_nom_joueur_blanc.get()
            partie.Nom_joueur_black = self.input_nom_joueur_noir.get()
            partie.Niveau_joueur_white = self.input_elo_blanc.get()
            partie.Niveau_joueur_black = self.input_elo_noir.get()
            partie.Date_partie = self.input_date_partie.get()
            partie.Type_partie = self.input_type_partie.get()
            partie.Duree_partie = self.input_duration_partie.get()
            partie.Resultat_partie = self.input_resultat_partie.get()
            partie.Nom_ouverture = self.input_nom_ouverture.get()
            deplacements = self.input_deplacements.get().split()

            board = chess.Board()
            partie.deplacement = []

            for deplacement in deplacements:
                try:
                    move_complet = board.push_san(deplacement)
                    partie.ajouter_deplacement(move_complet)
                except chess.InvalidMoveError:
                    self.message_avertissement.config(text="Déplacement invalide")
                    return

            self.mon_catalogue.ecrire()

    def ecrire_infos_dans_fichier(self):
        evenement = self.input_evenement.get()
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

        if not all([evenement, nom_joueur_blanc, nom_joueur_noir, date_partie, elo_blanc, elo_noir, type_partie, duration_partie, resultat_partie, nom_ouverture]):
            self.message_avertissement.config(text="Veuillez remplir les informations demandées manquantes")
            return
        elif self.mon_catalogue.obtenir_une_partie(evenement):
            self.message_avertissement.config(text="Ce nom d'évènement existe déjà.")
            return

        nouv_partie = Partie()
        nouv_partie.Evenement = evenement
        nouv_partie.Nom_joueur_black = nom_joueur_noir
        nouv_partie.Nom_joueur_white = nom_joueur_blanc
        nouv_partie.Date_partie = nom_joueur_noir
        nouv_partie.Niveau_joueur_white = elo_blanc
        nouv_partie.Niveau_joueur_black = elo_noir
        nouv_partie.Type_partie = type_partie
        nouv_partie.Duree_partie = duration_partie
        nouv_partie.Resultat_partie = resultat_partie
        nouv_partie.Nom_ouverture = nom_ouverture

        board = chess.Board()
        for deplacement in deplacements:
            try:
                move_complet = board.push_san(deplacement)
                nouv_partie.ajouter_deplacement(move_complet)
            except chess.InvalidMoveError:
                self.message_avertissement.config(text="Déplacement invalide")
                return

        self.mon_catalogue.ajouter_partie(nouv_partie)
        self.mon_catalogue.ecrire()

        self.message_avertissement.config(text="")

        self.input_evenement.delete(0, END)
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

    def protocole_supprimer_partie(self):
        self.titre.grid_forget()
        self.texte_sous_le_titre.grid_forget()

        self.bouton_ajouter_partie.config(state=DISABLED)
        self.bouton_modifier_partie.config(state=DISABLED)
        self.bouton_supprimer_partie.config(state=DISABLED)

        lblTitre = Label(self.frame2, text="Veuillez sélectionner un évenement")
        lblTitre.grid(column=0, row=0, padx=10, pady=10, sticky=W)
        self.message_avertissement.grid(column=0, row=2, columnspan=2)

        lbl_evenement = Label(self.frame2, text="Évenement:")
        self.input_evenement = Combobox(self.frame2, width=17, state='readonly')
        self.input_evenement['values'] = (self.mon_catalogue.obtenir_parties())
        lbl_evenement.grid(column=0, row=4)
        self.input_evenement.grid(column=1, row=4)

        but_afficher_partie = Button(self.frame2, text="Selectionner Partie", command=self.afficher_informations_supprimer_partie)
        but_afficher_partie.grid(column=2, row=4, padx=10, pady=10, sticky=W)

    def afficher_informations_supprimer_partie(self):
        partie = self.mon_catalogue.obtenir_une_partie(self.input_evenement.get())

        if partie:

            but_supprimer_partie = Button(self.frame2, text="Supprimer Partie", command=self.supprimer_infos_dans_fichier)
            but_supprimer_partie.grid(column=0, row=5, padx=10, pady=10, sticky=W)
            but_retourner_accueil = Button(self.frame2, text="Retourner à la page d'accueil",
                                           command=self.retourner_page_accueil)
            but_retourner_accueil.grid(column=1, row=5, padx=10, pady=10, sticky=W)

    def supprimer_infos_dans_fichier(self):
        partie = self.mon_catalogue.obtenir_une_partie(self.input_evenement.get())

        if partie:
            self.mon_catalogue.supprimer_partie(partie)
            self.mon_catalogue.ecrire()
            self.avertissement = Label(self.frame2, text="Partie supprimée avec succès!")
            self.avertissement.grid(column=0, row=1, padx=10, pady=10)
        else:
            self.avertissement = Label(self.frame2, text="Partie non trouvée.")
            self.avertissement.grid(column=0, row=1, padx=10, pady=10)

    def lancer_application(self):
        self.root.mainloop()
