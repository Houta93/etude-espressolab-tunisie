import pandas as pd
import numpy as np

print("=== VÉRIFICATION DÉTAILLÉE FICHIER INVESTMENTCOST.xlsx ===")
print()

# Lire le fichier Excel
try:
    # Essayer de lire toutes les feuilles
    excel_file = pd.ExcelFile('/home/ubuntu/upload/INVESTMENTCOST.xlsx')
    print("Feuilles disponibles:", excel_file.sheet_names)
    print()
    
    # Lire la première feuille
    df = pd.read_excel('/home/ubuntu/upload/INVESTMENTCOST.xlsx', sheet_name=0)
    print("=== CONTENU FEUILLE PRINCIPALE ===")
    print("Colonnes:", list(df.columns))
    print("Nombre de lignes:", len(df))
    print()
    
    # Afficher les premières lignes
    print("=== PREMIÈRES LIGNES ===")
    print(df.head(10))
    print()
    
    # Chercher des mots-clés liés aux coûts franchise
    print("=== RECHERCHE MOTS-CLÉS FRANCHISE ===")
    keywords = ['franchise', 'royalt', 'fee', 'droit', 'entrance', 'entry', 'initial']
    
    for keyword in keywords:
        found = False
        for col in df.columns:
            if df[col].dtype == 'object':  # Colonnes texte
                matches = df[col].astype(str).str.contains(keyword, case=False, na=False)
                if matches.any():
                    print(f"Mot-clé '{keyword}' trouvé dans colonne '{col}':")
                    print(df[matches][col].values)
                    found = True
        if not found:
            print(f"Mot-clé '{keyword}': Non trouvé")
    print()
    
    # Analyser les montants
    print("=== ANALYSE DES MONTANTS ===")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        print(f"Colonne '{col}':")
        print(f"  Min: {df[col].min()}")
        print(f"  Max: {df[col].max()}")
        print(f"  Somme: {df[col].sum()}")
        print()
    
    # Afficher tout le contenu si petit
    if len(df) <= 20:
        print("=== CONTENU COMPLET ===")
        print(df.to_string())
    
except Exception as e:
    print(f"Erreur lors de la lecture: {e}")

