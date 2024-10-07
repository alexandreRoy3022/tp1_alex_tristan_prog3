class Partie:
    def __init__(self):
        self.__nom_joueurs = None
        self.date_partie = None
        self.niveau_joueurs = None
        self.type_partie = None
        self.duree_partie = None
        self.resultat_partie = None
        self.nom_ouverture = None
        self.deplacements = []

    @property
    def nom_joueurs(self):
        return self.__nom_joueurs

    @nom_joueurs.setter
    def nom_joueurs(self, nom_joueurs):
        self.__nom_joueurs = nom_joueurs

    @property
    def date_partie(self):
        return self.date_partie

    @date_partie.setter
    def date_partie(self, date_partie):
        self.date_partie = date_partie

    @property
    def niveau_joueurs(self):
        return self.niveau_joueurs

    @niveau_joueurs.setter
    def niveau_joueurs(self, niveau_joueurs):
        self.niveau_joueurs = niveau_joueurs

    @property
    def type_partie(self):
        return self.type_partie

    @type_partie.setter
    def type_partie(self, type_partie):
        self.type_partie = type_partie

    @property
    def duree_partie(self):
        return self.duree_partie

    @duree_partie.setter
    def duree_partie(self, duree_partie):
        self.duree_partie = duree_partie

    @property
    def resultat_partie(self):
        return self.resultat_partie

    @resultat_partie.setter
    def resultat_partie(self, resultat_partie):
        self.resultat_partie = resultat_partie

    @property
    def nom_ouverture(self):
        return self.nom_ouverture

    @nom_ouverture.setter
    def nom_ouverture(self, nom_ouverture_utilisee):
        self.nom_ouverture = nom_ouverture_utilisee

    def ajouter_deplacement(self, deplacement):
        self.deplacements.append(deplacement)

    def modifier_deplacement(self, no_ancien_deplacement, nouveau_deplacement):
        self.deplacements[no_ancien_deplacement] = nouveau_deplacement

    def supprimer_deplacement(self, no_deplacement):
        self.deplacements.remove(self.deplacements[no_deplacement])