from abc import abstractmethod



from action.partie import Partie



class Catalogue:
    def __init__(self):
        self.parties = []

    @property
    def Parties(self):
        return self.parties

    def obtenir_parties(self) -> []:
        parties = []
        for partie in self.parties:
            parties.append(partie.Evenement)

        return parties

    def obtenir_une_partie(self, evenement) :
        parties = []
        for partie in self.parties:
            if partie.Evenement == evenement:
                return partie

        return None

    def ajouter_partie(self, partie: Partie):
        self.parties.append(partie)

    def supprimer_partie(self, no_partie):
        self.parties.remove(self.parties[no_partie])

    @abstractmethod
    def lire(self, nom_fichier):
        pass

    @abstractmethod
    def sauvegarder(self):
        pass

