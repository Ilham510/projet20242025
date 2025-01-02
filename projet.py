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

def extraire_sequences(mirna_data, species_list):
    """Extrait les séquences des espèces spécifiées."""
    sequences = {species: [] for species in species_list}
    for line in mirna_data:
        parts = line.split()
        if len(parts) < 9:  # Pour éviter les lignes mal formatées
            continue
        espece, sequence = parts[4], parts[8]
        if espece in sequences:
            sequences[espece].append(sequence)
    return sequences
