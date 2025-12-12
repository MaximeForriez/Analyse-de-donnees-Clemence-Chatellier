import pandas as pd
import numpy as np

import pandas as pd

# Lecture du fichier
data = pd.read_csv(
    r"C:\Users\Clémence CHATELLIER\Desktop\ANALYSE DE DONNEES\src\data\island-index.csv",
    low_memory=False
)

# Sélection de la colonne avec majuscule
surfaces = data["Surface (km²)"]

# Définir les bornes et les étiquettes
bornes = [0, 10, 25, 50, 100, 2500, 5000, 10000, float('inf')]
labels = ["0–10", "10–25", "25–50", "50–100", "100–2500", "2500–5000", "5000–10000", "≥10000"]

# Catégoriser
categories = pd.cut(surfaces, bins=bornes, labels=labels, right=False)

# Compter les valeurs
compte = categories.value_counts().sort_index()

# Afficher le résultat
print(compte)
import pandas as pd

# 1. Lire le fichier CSV
data = pd.read_csv(
    r"C:\Users\Clémence CHATELLIER\Desktop\ANALYSE DE DONNEES\src\data\island-index.csv",
    low_memory=False
)

# 2. Vérifier les colonnes disponibles
print("Colonnes disponibles :", data.columns)

# 3. Extraire la colonne 'Surface (km²)' et convertir en numérique
surfaces = pd.to_numeric(data['Surface (km²)'], errors='coerce')
