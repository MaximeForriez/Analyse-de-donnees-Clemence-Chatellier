import os
import pandas as pd
import matplotlib.pyplot as plt

# 🔹 Chemin du fichier CSV
fichier = r"C:\Users\Clémence CHATELLIER\Downloads\resultats-elections-presidentielles-2022-1er-tour.csv"

# 🔹 Lecture du CSV
df = pd.read_csv(fichier, sep=",", quotechar='"', encoding="utf-8-sig", engine="python")

# 🔹 Infos sur le DataFrame
print("Lecture réussie !")
print("Nombre de lignes :", len(df))
print("Nombre de colonnes :", len(df.columns))
print("\nColonnes détectées :", df.columns.tolist())
print("\nAperçu du tableau :")
print(df.head())

# 🔹 Types de données
print("\nTypes des colonnes :")
for col in df.columns:
    print(f"{col} → {df[col].dtype}")

# 🔹 Somme des colonnes quantitatives
colonnes_quantitatives = [
    "Inscrits", "Abstentions", "Votants", "Blancs", "Nuls", "Exprimés",
    "Voix", "Voix.1", "Voix.2", "Voix.3", "Voix.4", "Voix.5",
    "Voix.6", "Voix.7", "Voix.8", "Voix.9", "Voix.10", "Voix.11"
]

sommes_valides = []
for col in colonnes_quantitatives:
    if col in df.columns:
        total = df[col].sum()
        sommes_valides.append((col, total))

df_sommes = pd.DataFrame(sommes_valides, columns=["Colonne", "Somme"])
print("\nSomme des colonnes quantitatives :")
print(df_sommes)
#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023
import pandas as pd
import numpy as np
import os
import pandas as pd

# Chargement du fichier CSV
import os

import pandas as pd

df = pd.read_csv(r"C:\Users\Clémence CHATELLIER\Downloads\resultats-elections-presidentielles-2022-1er-tour.csv")


# Affichage pour vérifier les colonnes
print("Colonnes du fichier :")
print(df.columns)

# Sélection des colonnes quantitatives (numériques)
quant_cols = df.select_dtypes(include=["number"])

print("\nColonnes quantitatives sélectionnées :")
print(quant_cols.columns)

# Calculs statistiques, arrondis à 2 décimales
# Calculs statistiques, arrondis à 2 décimales
moyennes = quant_cols.mean().round(2)
medians = quant_cols.median().round(2)
modes = quant_cols.mode().iloc[0].round(2)  # mode() peut renvoyer plusieurs lignes
ecart_type = quant_cols.std().round(2)
ecart_absolu = (quant_cols - quant_cols.mean()).abs().mean().round(2)
etendue = (quant_cols.max() - quant_cols.min()).round(2)

# Affichage des résultats
print("\n=== Moyennes ===")
print(moyennes)

print("\n=== Médianes ===")
print(medians)

print("\n=== Modes ===")
print(modes)

print("\n=== Écart-type ===")
print(ecart_type)

print("\n=== Écart absolu moyen ===")
print(ecart_absolu)

print("\n=== Étendue ===")
print(etendue)


# Affichage des résultats
print("\n=== Moyennes ===")
print(moyennes)

print("\n=== Médianes ===")
print(medians)

print("\n=== Modes ===")
print(modes)

print("\n=== Écart-type ===")
print(ecart_type)

print("\n=== Écart absolu moyen ===")
print(ecart_absolu)

print("\n=== Étendue ===")
print(etendue)

# Regrouper toutes les statistiques dans un DataFrame
stats = pd.DataFrame({
    "Moyenne": moyennes,
    "Médiane": medians,
    "Mode": modes,
    "Écart-type": ecart_type,
    "Écart absolu moyen": ecart_absolu,
    "Étendue": etendue
})

# ✅ Affichage propre dans le terminal
print("\n==============================")
print("📊 Liste des paramètres statistiques :")
print("==============================")
print(stats)

# (optionnel) Sauvegarde dans un CSV
stats.to_csv("statistiques_elections.csv", index=True, encoding='utf-8')
print("\n✅ Fichier 'statistiques_elections.csv' créé avec succès !")
# Colonnes quantitatives
colonnes_quantitatives = ['Inscrits', 'Abstentions', 'Votants', 'Blancs', 'Nuls',
                          'Exprimés', 'Voix', 'Voix.1', 'Voix.2', 'Voix.3', 'Voix.4',
                          'Voix.5', 'Voix.6', 'Voix.7', 'Voix.8', 'Voix.9', 'Voix.10', 'Voix.11']

# Création d'un DataFrame pour stocker DIQ et DID
ecart_quartile = pd.DataFrame(index=colonnes_quantitatives, columns=['DIQ', 'DID'])

for col in colonnes_quantitatives:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    ecart_quartile.loc[col, 'DIQ'] = q3 - q1  # Distance interquartile
    
    d1 = df[col].quantile(0.1)
    d9 = df[col].quantile(0.9)
    ecart_quartile.loc[col, 'DID'] = d9 - d1  # Distance interdécile

print("\n=== Distance interquartile (DIQ) et interdécile (DID) ===")
print(ecart_quartile)
import matplotlib.pyplot as plt
import os

# Créer le dossier "img" s'il n'existe pas
os.makedirs("img", exist_ok=True)

# Liste des colonnes quantitatives
colonnes_quantitatives = ['Inscrits', 'Abstentions', 'Votants', 'Blancs', 'Nuls',
                          'Exprimés', 'Voix', 'Voix.1', 'Voix.2', 'Voix.3', 'Voix.4',
                          'Voix.5', 'Voix.6', 'Voix.7', 'Voix.8', 'Voix.9', 'Voix.10', 'Voix.11']

# Boucle pour créer, afficher et sauvegarder chaque boîte à moustaches
for col in colonnes_quantitatives:
    plt.figure(figsize=(6,4))
    plt.boxplot(df[col].dropna())
    plt.title(f'Boîte à moustaches de {col}')
    plt.ylabel(col)
    
    # Afficher la figure
    plt.show()
    
    # Sauvegarder l'image dans le dossier "img"
    plt.savefig(f'img/boxplot_{col}.png')
    plt.close()  # ferme la figure pour éviter l'affichage multiple
import os

# Chemin du dossier img
chemin_img = os.path.join(os.getcwd(), 'img')
print("Dossier img :", chemin_img)

# Liste des fichiers dans ce dossier
print("Fichiers :", os.listdir(chemin_img))
