from abc import ABC
from wsgiref import headers

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
            une_partie.nom_joueur_black = headers["Black"]
            une_partie.nom_joueur_white = headers["White"]
            une_partie.niveau_joueur_black = headers["BlackElo"]
            une_partie.niveau_joueur_white = headers["WhiteElo"]
            une_partie.date_partie = headers["Date"]
            une_partie.type_partie = headers["Event"]
            une_partie.duree_partie = headers["Time"]
            une_partie.resultat_partie = headers["Result"]
            une_partie.nom_ouverture = headers["ECO"]

            headers["moves"] = game.board().variation_san(game.mainline_moves())

            for move in game.mainline_moves():
                une_partie.ajouter_deplacement(move)

            result["Game{}".format(i)] = headers

            self.ajouter_partie(une_partie)


    def ecrire(self):

        CptPartie = 0
        for une_partie in self.Parties:
            CptPartie += 1
            game = chess.pgn.Game()
            game.headers["Black"] = une_partie.nom_joueur_black
            game.headers["White"] = une_partie.nom_joueur_white
            game.headers["BlackElo"] = une_partie.niveau_joueur_black
            game.headers["WhiteElo"] = une_partie.niveau_joueur_white
            game.headers["Date"] = une_partie.date_partie
            game.headers["Event"] = une_partie.type_partie
            game.headers["Time"] = une_partie.duree_partie
            game.headers["Result"] = une_partie.resultat_partie
            game.headers["ECO"] = une_partie.nom_ouverture
            if len(une_partie.deplacements) == 0:
                break

            node = game.add_variation(une_partie.deplacements[0])

            for i in range (1 , len(une_partie.deplacements)):
                #node = game.add_variation(chess.Move.from_uci(une_partie.deplacements[i]))
                node = node.add_variation(une_partie.deplacements[i])


            if CptPartie == 1:
                print(game, file=open("..\\action\\data\\chess.pgn", "w"))
            else:
                print(game, file=open("..\\action\\data\\chess.pgn", "a"))

            print(" ", file=open("..\\action\\data\\chess.pgn", "a"))
