from action.catalogue_pgn import CataloguePgn

if __name__ == '__main__':
    nom_fichier = "data\chess.pgn"
    catalogue = CataloguePgn()
    catalogue.lire(nom_fichier)