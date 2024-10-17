from abc import ABC
from action.catalogue import Catalogue
import chess.pgn
from action.partie import Partie


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

            une_partie = Partie()
            une_partie.Evenement = headers["Event"]
            une_partie.Nom_joueur_black = headers["Black"]
            une_partie.Nom_joueur_white = headers["White"]
            une_partie.Niveau_joueur_black = headers["BlackElo"]
            une_partie.Niveau_joueur_white = headers["WhiteElo"]
            une_partie.Date_partie = headers["Date"]
            une_partie.Type_partie = headers["Type"]
            une_partie.Duree_partie = headers["Time"]
            une_partie.Resultat_partie = headers["Result"]
            une_partie.Nom_ouverture = headers["ECO"]

            headers["moves"] = game.board().variation_san(game.mainline_moves())

            for move in game.mainline_moves():
                une_partie.ajouter_deplacement(move)

            result["Game{}".format(i)] = headers

            self.ajouter_partie(une_partie)


    def ecrire(self):

        CptPartie = 0
        for une_partie in self.toutes_parties:
            CptPartie += 1
            game = chess.pgn.Game()
            game.headers["Event"] = une_partie.Evenement
            game.headers["Black"] = une_partie.Nom_joueur_black
            game.headers["White"] = une_partie.Nom_joueur_white
            game.headers["BlackElo"] = une_partie.Niveau_joueur_black
            game.headers["WhiteElo"] = une_partie.Niveau_joueur_white
            game.headers["Date"] = une_partie.Date_partie
            game.headers["Type"] = une_partie.Type_partie
            game.headers["Time"] = une_partie.Duree_partie
            game.headers["Result"] = une_partie.Resultat_partie
            game.headers["ECO"] = une_partie.Nom_ouverture
            if len(une_partie.deplacement) == 0:
                break

            node = game.add_variation(une_partie.deplacement[0])

            for i in range(1, len(une_partie.deplacement)):
                node = node.add_variation(une_partie.deplacement[i])


            if CptPartie == 1:
                print(game, file=open("..\\action\\data\\chess.pgn", "w"))
            else:
                print(game, file=open("..\\action\\data\\chess.pgn", "a"))

            print(" ", file=open("..\\action\\data\\chess.pgn", "a"))
