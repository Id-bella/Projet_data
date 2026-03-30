# utils.py
import unicodedata
import pandas as pd

# Normalisation des codes département
def normaliser_code_dep(serie):
    return (
        serie.astype(str)
        .str.strip()
        .str.upper()
        .str.replace(".0", "", regex=False)
        .str.replace(r"\s+", "", regex=True)
        .str.replace(r"[^0-9A-Z]", "", regex=True)
    )


def normaliser_texte(s):
    """Supprime les accents et met en minuscules"""
    return ''.join(
        c for c in unicodedata.normalize('NFD', s.lower())
        if unicodedata.category(c) != 'Mn'
    )

# Filtre candidat
def chercher_candidat(nom, score_departements):
    """
    Recherche flexible d'un candidat dans le DataFrame.
    Insensible à la casse et aux accents.
    Ex: 'zemmour', 'Eric Zemmour', 'ZEMMOUR' fonctionnent tous.
    """
    candidats_uniques = score_departements["candidat"].unique()
    candidat_trouve = [
        c for c in candidats_uniques
        if normaliser_texte(nom) in normaliser_texte(c)
    ]
    if not candidat_trouve:
        raise ValueError(f"Aucun candidat trouvé pour '{nom}'")
    return candidat_trouve[0]

