class Partie:
    def __init__(self):
        self.nom_joueur_black = None
        self.nom_joueur_white = None
        self.date_partie = None
        self.niveau_joueur_black = None
        self.niveau_joueur_white = None
        self.type_partie = None
        self.duree_partie = None
        self.resultat_partie = None
        self.nom_ouverture = None
        self.deplacements = []

    @property
    def Nom_joueur_black(self):
        return self.nom_joueur_black

    @Nom_joueur_black.setter
    def Nom_joueur_black(self, nom_joueur_black):
        self.nom_joueur_black = nom_joueur_black

    @property
    def Nom_joueur_white(self):
        return self.nom_joueur_white

    @Nom_joueur_white.setter
    def Nom_joueur_white(self, nom_joueur_white):
        self.nom_joueur_white = nom_joueur_white

    @property
    def Date_partie(self):
        return self.date_partie

    @Date_partie.setter
    def Date_partie(self, date_partie):
        self.date_partie = date_partie

    @property
    def Niveau_joueur_black(self):
        return self.niveau_joueur_black

    @Niveau_joueur_black.setter
    def Niveau_joueur_black(self, niveau_joueur_black):
        self.niveau_joueur_black = niveau_joueur_black

    @property
    def Niveau_joueur_white(self):
        return self.niveau_joueur_white

    @Niveau_joueur_white.setter
    def Niveau_joueur_white(self, niveau_joueur_white):
        self.niveau_joueur_white = niveau_joueur_white

    @property
    def Type_partie(self):
        return self.type_partie

    @Type_partie.setter
    def Type_partie(self, type_partie):
        self.type_partie = type_partie

    @property
    def Duree_partie(self):
        return self.duree_partie

    @Duree_partie.setter
    def Duree_partie(self, duree_partie):
        self.duree_partie = duree_partie

    @property
    def Resultat_partie(self):
        return self.resultat_partie

    @Resultat_partie.setter
    def Resultat_partie(self, resultat_partie):
        self.resultat_partie = resultat_partie

    @property
    def Nom_ouverture(self):
        return self.nom_ouverture

    @Nom_ouverture.setter
    def Nom_ouverture(self, nom_ouverture_utilisee):
        self.nom_ouverture = nom_ouverture_utilisee

    def ajouter_deplacement(self, deplacement):
        self.deplacements.append(deplacement)

    def modifier_deplacement(self, no_ancien_deplacement, nouveau_deplacement):
        self.deplacements[no_ancien_deplacement] = nouveau_deplacement

    def supprimer_deplacement(self, no_deplacement):
        self.deplacements.remove(self.deplacements[no_deplacement])