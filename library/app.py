from tkinter import *
from action.catalogue_pgn import CataloguePgn


class Application:
    def __init__(self):
        self.root = Tk()

        self.panedwindow = PanedWindow(self.root)

        self.image_de_décoration = PhotoImage(file="—Pngtree—black and white chess board_5983396.png")

        self.frame1 = Frame(self.panedwindow, width=400, height=300, relief=RAISED)
        self.frame2 = Frame(self.panedwindow, width=400, height=300, relief=RAISED)

        self.panedwindow.add(self.frame1)
        self.panedwindow.add(self.frame2)

        self.titre = Label(self.frame2, text="Bienvenu au menu principal", font=("Helvetica", 60))

        self.bouton_ajouter_partie = Button(self.frame1, text="Ajouter partie", image=self.image_de_décoration, compound="top", command=self.protocole_ajout_partie)
        self.bouton_modifier_partie = Button(self.frame1, text="Modifier Partie", image=self.image_de_décoration, compound="top", command=Database.modifier_partie)
        self.bouton_supprimer_partie = Button(self.frame1, text="Supprimer Partie", image=self.image_de_décoration, compound="top", command=Database.supprimer_partie)
        self.bouton_quitter = Button(self.frame1, text="Quitter", bg="red", fg="white", command=self.root.destroy)

        self.texte_sous_le_titre = Label(self.frame2, text="Veuillez cliquer sur l'option que vous désirez à droite")
        self.message_avertissement = Label(self.frame2, text="", fg="red")

        self.panedwindow.pack(fill=BOTH, expand=True)
        self.titre.pack()

        self.bouton_ajouter_partie.place(relx=0.5, rely=0.4, anchor="center")
        self.bouton_modifier_partie.place(relx=0.5, rely=0.5, anchor="center")
        self.bouton_supprimer_partie.place(relx=0.5, rely=0.6, anchor="center")
        self.bouton_quitter.place(relx=1.0, rely=0.0, anchor="ne")

    def protocole_ajout_partie(self):
        self.titre.pack_forget()
        self.texte_sous_le_titre.pack_forget()

        self.bouton_ajouter_partie.config(state=DISABLED)
        self.bouton_modifier_partie.config(state=DISABLED)
        self.bouton_supprimer_partie.config(state=DISABLED)
        self.bouton_quitter.config(state=DISABLED)

        Label(self.frame2, text="Veuillez répondre à chaque entrée ci-dessous").pack()

        Label(self.frame2, text="Nom du site:").pack()
        self.input_nom_site = Entry(self.frame2)

        Label(self.frame2, text="Nom du joueur blanc:").pack()
        self.input_nom_joueur_blanc = Entry(self.frame2)

        Label(self.frame2, text="Nom du joueur noir:")
        self.input_nom_joueur_noir = Entry(self.frame2)

        Label(self.frame2, text="Date de la partie:").pack()
        self.input_date_partie = Entry(self.frame2)

        Label(self.frame2, text="Elo du joueur blanc:").pack()
        self.input_elo_blanc = Entry(self.frame2)

        Label(self.frame2, text="Elo du joueur noir:").pack()
        self.input_elo_noir = Entry(self.frame2)

        Label(self.frame2, text="Type de partie:").pack()
        self.input_type_partie = Entry(self.frame2)

        Label(self.frame2, text="Durée de la partie:").pack()
        self.input_duration_partie = Entry(self.frame2)

        Label(self.frame2, text="Résultat de la partie:").pack()
        self.input_resultat_partie = Entry(self.frame2)

        Button(self.frame2, text="Ajouter Partie", command=self.ecrire_infos_dans_fichier)
        Button(self.frame2, text="Retourner à la page d'accueil", command=self.retourner_page_accueil)

        self.input_nom_site.pack()
        self.input_nom_joueur_blanc.pack()
        self.input_nom_joueur_noir.pack()
        self.input_date_partie.pack()
        self.input_elo_blanc.pack()
        self.input_elo_noir.pack()
        self.input_type_partie.pack()
        self.input_duration_partie.pack()
        self.input_resultat_partie.pack()
        self.message_avertissement.pack()

    def retourner_page_accueil(self):
        for widget in self.frame2.winfo_children():
            widget.pack_forget()

        self.titre.pack()
        self.texte_sous_le_titre.pack()

    def ecrire_infos_dans_fichier(self):
        nom_site = self.input_nom_site.get()
        nom_joueur_blanc = self.input_nom_joueur_blanc.get()
        nom_joueur_noir = self.input_nom_joueur_noir.get()
        date_partie = self.input_date_partie.get()
        elo_blanc = self.input_elo_blanc.get()
        elo_noir = self.input_elo_noir.get()
        type_partie = self.input_type_partie.get()
        duration_partie = self.input_duration_partie.get()
        resultat_partie = self.input_resultat_partie.get()

        if not all([nom_site, nom_joueur_blanc, nom_joueur_noir, date_partie, elo_blanc, elo_noir, type_partie, duration_partie, resultat_partie]):
            self.message_avertissement.config(text="Veuillez remplir les informations demandées manquantes")
            return


        # j'ai trouvé avec chatgpt quelques lignes pour écrire les informations de la nouvelle partie ajoutée
        with open('action/data/chess.pgn', mode='a') as fichier_pgn:
            # Écrire les en-têtes
            fichier_pgn.write(f"[Event \"ch-UZB 1st League 2014\"]\n")
            fichier_pgn.write(f"[Site \"{nom_site}\"]\n")
            fichier_pgn.write(f"[Date \"{date_partie}\"]\n")
            fichier_pgn.write(f"[White \"{nom_joueur_blanc}\"]\n")
            fichier_pgn.write(f"[Black \"{nom_joueur_noir}\"]\n")
            fichier_pgn.write(f"[Result \"{resultat_partie}\"]\n")
            fichier_pgn.write(f"[WhiteElo \"{elo_blanc}\"]\n")
            fichier_pgn.write(f"[BlackElo \"{elo_noir}\"]\n")
            fichier_pgn.write(f"[Game Type \"{type_partie}\"]\n")
            fichier_pgn.write(f"[Game Duration \"{duration_partie}\"]\n")
            fichier_pgn.write("\n")

        self.input_nom_site.delete(0, END)
        self.input_nom_joueur_blanc.delete(0, END)
        self.input_nom_joueur_noir.delete(0, END)
        self.input_date_partie.delete(0, END)
        self.input_elo_blanc.delete(0, END)
        self.input_elo_noir.delete(0, END)
        self.input_type_partie.delete(0, END)
        self.input_duration_partie.delete(0, END)
        self.input_resultat_partie.delete(0, END)

        self.bouton_ajouter_partie.config(state=NORMAL)
        self.bouton_modifier_partie.config(state=NORMAL)
        self.bouton_supprimer_partie.config(state=NORMAL)
        self.bouton_quitter.config(state=NORMAL)

    def lancer_application(self):
        self.root.mainloop()
