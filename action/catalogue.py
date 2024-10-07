from abc import abstractclassmethod, abstractmethod



from action.partie import Partie



class Catalogue:
    def __init__(self):
        self.parties = []

    def ajouter_partie(self, partie: Partie):
        self.parties.append(partie)

    def supprimer_partie(self, no_partie):
        self.parties.remove(self.parties[no_partie])

    @abstractmethod
    def lire(self, nom_fichier):
        pass

    @abstractmethod
    def sauvegarder(cls):
        pass

