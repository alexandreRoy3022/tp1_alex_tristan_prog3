from abc import ABC

from action.catalogue import Catalogue

import chess.pgn


class CataloguePgn(Catalogue, ABC):
    def __init__(self):
        super().__init__()

    def lire(self, nom_fichier):
        f = open(nom_fichier)

        result = {}
        i = 0
        while True:
            i += 1
            game = chess.pgn.read_game(f)
            if game is None:
                break

            headers = dict(game.headers)

            headers["moves"] = game.board().variation_san(game.mainline_moves())
            #[liste_deplacement.append(move) for move in game.mainline_moves()]

            result["Game{}".format(i)] = headers

    def ajouter_nom_joueurs(self, headers):
        self.nom_joueurs = headers["Black"] + headers["White"]

    def ajouter_date_partie(self, headers):
        self.date_partie = headers["Date"]

    def ajouter_niveau_joueurs(self, headers):
        self.niveau_joueurs = headers["BlackElo"] + headers["WhiteElo"]

    def ajouter_type_partie(self, headers):
        self.type_partie = headers["Event"]

    def ajouter_duree_partie(self, headers):
        self.duree_partie = headers["Time"]

    def ajouter_resultat_partie(self, headers):
        self.resultat_partie = headers["Result"]

    def ajouter_nom_ouverture_partie(self, headers):
        self.nom_ouverture_partie = headers["ECO"]

    def ajouter_deplacement(self):
        pass