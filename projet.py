import re
import matplotlib.pyplot as plt

def lire_fichier_species(filepath):
    """Lit les noms d'espèces à partir d'un fichier."""
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

def lire_fichier_mirna(filepath):
    """Lit et retourne les lignes du fichier mirna."""
    with open(filepath, 'r') as file:
        return file.readlines()
