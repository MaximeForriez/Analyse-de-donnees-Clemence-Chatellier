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

# 🔹 Création des dossiers pour graphiques
dossier_bars = r"C:\Users\Clémence CHATELLIER\Desktop\graphs_elections"
dossier_camemberts = r"C:\Users\Clémence CHATELLIER\Desktop\camemberts_elections"
os.makedirs(dossier_bars, exist_ok=True)
os.makedirs(dossier_camemberts, exist_ok=True)

# 🔹 Graphiques en barres pour inscrits/votants
for i, row in df.iterrows():
    departement = row["Libellé du département"]
    plt.figure(figsize=(5,4))
    plt.bar(["Inscrits", "Votants"], [row["Inscrits"], row["Votants"]], color=["skyblue", "lightgreen"])
    plt.title(f"Département : {departement}")
    plt.ylabel("Nombre d'électeurs")
    nom_fichier = os.path.join(dossier_bars, f"{departement.replace('/', '-')}.png")
    plt.tight_layout()
    plt.savefig(nom_fichier)
    plt.close()

print(f"Graphiques en barres enregistrés dans : {dossier_bars}")

# 🔹 Camemberts pour chaque département
for i, row in df.iterrows():
    departement = row["Libellé du département"]
    valeurs = [row["Abstentions"], row["Blancs"], row["Nuls"], row["Exprimés"]]
    labels = ["Abstentions", "Blancs", "Nuls", "Exprimés"]
    couleurs = ["gold", "lightcoral", "lightskyblue", "lightgreen"]
    
    plt.figure(figsize=(6,6))
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=90, colors=couleurs)
    plt.title(f"Répartition des votes - {departement}")
    
    departement_safe = departement.replace("/", "-").replace(" ", "_")
    nom_fichier = os.path.join(dossier_camemberts, f"{departement_safe}.png")
    plt.savefig(nom_fichier)
    plt.close()

print("Tous les camemberts ont été créés et sauvegardés dans :", dossier_camemberts)
import matplotlib.pyplot as plt

# 🔹 Données : nombre d'inscrits par département
inscrits = df["Inscrits"]

# 🔹 Création de l'histogramme
plt.figure(figsize=(10,6))
plt.hist(inscrits, bins=20, color="skyblue", edgecolor="black")  # 20 classes par exemple
plt.title("Distribution du nombre d'inscrits par département (1er tour 2022)")
plt.xlabel("Nombre d'inscrits")
plt.ylabel("Nombre de départements")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

#  Affichage à l'écran
plt.show()

# (Optionnel) Sauvegarde du graphique
plt.savefig(r"C:\Users\Clémence CHATELLIER\Desktop\histogramme_inscrits.png")
import os
import matplotlib.pyplot as plt

#  Dossier pour enregistrer les camemberts par département
dossier_voix_dept = r"C:\Users\Clémence CHATELLIER\Desktop\camemberts_voix_departements"
os.makedirs(dossier_voix_dept, exist_ok=True)

#  Boucle sur chaque département
for index, row in df.iterrows():
    departement = row["Libellé du département"]
    
    # On récupère toutes les colonnes "Voix" pour les candidats
    colonnes_voix = [col for col in df.columns if col.startswith("Voix")]
    valeurs = [row[col] for col in colonnes_voix]
    
    # Labels = noms des candidats correspondants (supposons colonnes "Nom", "Nom.1", …)
    colonnes_noms = [col for col in df.columns if col.startswith("Nom")]
    labels = [row[col] for col in colonnes_noms]
    
    # Création du camembert
    plt.figure(figsize=(6,6))
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Répartition des voix - {departement}")
    plt.tight_layout()
    
    # Nom sûr pour le fichier
    departement_safe = departement.replace("/", "-").replace(" ", "_")
    plt.savefig(os.path.join(dossier_voix_dept, f"{departement_safe}.png"))
    plt.close()

print("Camemberts par département créés et sauvegardés !")

import matplotlib.pyplot as plt

# 🔹 Colonnes des voix des candidats
colonnes_voix = [col for col in df.columns if col.startswith("Voix")]

# 🔹 Colonnes des noms des candidats correspondants
colonnes_noms = [col for col in df.columns if col.startswith("Nom")]

# 🔹 Somme des voix par candidat pour toute la France
valeurs_france = [df[col].sum() for col in colonnes_voix]

# 🔹 Noms des candidats (on prend la première ligne pour chaque colonne "Nom")
labels_france = [df[col].iloc[0] for col in colonnes_noms]

# 🔹 Création du camembert
plt.figure(figsize=(8,8))
plt.pie(valeurs_france, labels=labels_france, autopct='%1.1f%%', startangle=90)
plt.title("Répartition des voix - France entière")
plt.tight_layout()

# 🔹 Affichage et sauvegarde
plt.show()
plt.savefig(r"C:\Users\Clémence CHATELLIER\Desktop\camemberts_voix_france.png")
plt.close()
