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

def calculer_pourcentages(sequence):
    """Calcule le pourcentage de A, C, G, U dans une séquence."""
    total = len(sequence)
    return {
        'A': sequence.count('A') / total * 100,
        'C': sequence.count('C') / total * 100,
        'G': sequence.count('G') / total * 100,
        'U': sequence.count('U') / total * 100
    }

def calculer_pourcentages_par_espece(sequences):
    """Calcule les pourcentages pour chaque espèce."""
    resultats = {}
    for espece, seqs in sequences.items():
        joint_sequence = ''.join(seqs)
        resultats[espece] = calculer_pourcentages(joint_sequence)
    return resultats

