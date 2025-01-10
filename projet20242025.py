import re
import matplotlib.pyplot as plt

def extraire_noms_especes(filepath):
    """Extrait tous les noms d'espèces uniques du fichier mirna.txt."""
    noms_especes = set()  # Utiliser un set pour éviter les doublons
    with open(filepath, 'r') as file:
        for line in file:
            # Utilisation d'une expression régulière pour détecter les noms d'espèces
            match = re.search(r'([A-Z][a-z]+ [a-z]+)', line)
            if match:
                noms_especes.add(match.group(1))  # Ajout du nom d'espèce trouvé
    return sorted(noms_especes)  # Retourne les noms triés par ordre alphabétique

def enregistrer_noms_especes(noms_especes, output_filepath):
    """Enregistre les noms d'espèces dans un fichier texte."""
    with open(output_filepath, 'w') as file:
        for espece in noms_especes:
            file.write(espece + '\n')

# Chemin des fichiers
fichier_mirna = 'mirna.txt'
fichier_output = 'species.txt'

# Extraction et enregistrement des noms d'espèces
noms_especes = extraire_noms_especes(fichier_mirna)
enregistrer_noms_especes(noms_especes, fichier_output)

print(f"Extraction terminée. Les noms d'espèces ont été enregistrés dans '{fichier_output}'.")

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
    sequences_total = {'Total':[]}
    for line in mirna_data:
        # Extraire les noms d'espèces et les séquences
        match = re.search(r'([A-Z][a-z]+ [a-z]+).*?([ACGU]{2,})', line)
        if match:
            espece, sequence = match.group(1), match.group(2)
            if espece in sequences:
                sequences[espece].append(sequence)
                sequences_total['Total'].append(sequence)
    return sequences, sequences_total

def calculer_pourcentages(sequence):
    """Calcule le pourcentage de A, C, G, U dans une séquence."""
    total = len(sequence)
    if total == 0:
        return {'A': 0, 'C': 0, 'G': 0, 'U': 0}
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

def generer_camembert(data, titre):
    """Génère un graphique en camembert pour les pourcentages donnés."""
    if sum(data.values()) == 0:
        print(f"Aucune donnée pour {titre}.")
        return
    labels = list(data.keys())
    sizes = list(data.values())
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(titre)
    plt.show()

def generer_tous_les_camemberts(resultats):
    """Génère des camemberts pour chaque espèce."""
    for espece, data in resultats.items():
        generer_camembert(data, f'Composition des bases - {espece}')

def generer_camembert_global(sequences):
    """Génère un camembert global pour toutes les espèces."""
    joint_sequence = ''.join(seq for seqs in sequences.values() for seq in seqs)
    data = calculer_pourcentages(joint_sequence)
    generer_camembert(data, 'Composition des bases - Global')

def main():
    # Chemins des fichiers
    species_file = 'species.txt'
    mirna_file = 'mirna.txt'

    # Lecture des fichiers
    species = lire_fichier_species(species_file)
    print(f"Espèces trouvées dans species.txt : {species}")

    mirna_data = lire_fichier_mirna(mirna_file)
    print(f"Nombre de lignes dans mirna.txt : {len(mirna_data)}")

    # Extraction des séquences
    sequences, sequences_total = extraire_sequences(mirna_data, species)
    for espece, seqs in sequences.items():
        print(f"{espece} : {len(seqs)} séquences extraites")
    print("Longueur total =", len(sequences_total))

    # Calcul des pourcentages
    resultats = calculer_pourcentages_par_espece(sequences)
    for espece, pourcentages in resultats.items():
        print(f"{espece} : {pourcentages}")
    print(calculer_pourcentages_par_espece(sequences_total))

    # Génération des camemberts
    generer_camembert_global(sequences)
    generer_tous_les_camemberts(resultats)
    

if __name__ == '__main__':
    main()

