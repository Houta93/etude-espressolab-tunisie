# Calcul impact prix café franchiseur sur prévisionnels

# Données de base
prix_cafe_usd = 23  # $/kg
taux_change = 3.15  # TND/USD (approximatif)
prix_cafe_tnd = prix_cafe_usd * taux_change

print("=== ANALYSE IMPACT PRIX CAFÉ FRANCHISEUR ===")
print(f"Prix café franchiseur: {prix_cafe_usd}$/kg = {prix_cafe_tnd:.2f} TND/kg")
print()

# Consommation estimée par boisson
consommations = {
    "Espresso": 7,  # grammes
    "Double Espresso": 14,
    "Americano": 7,
    "Cappuccino": 7,
    "Latte": 14,
    "Flat White": 14,
    "Cortado": 7,
    "Macchiato": 7,
    "Mocha": 14,
    "Turkish Coffee": 10,
    "Filter Coffee (V60, Chemex, etc.)": 15,
    "Cold Brew": 20,
    "Iced Latte": 14
}

print("=== COÛT CAFÉ PAR BOISSON ===")
for boisson, grammes in consommations.items():
    cout_cafe = (grammes / 1000) * prix_cafe_tnd
    print(f"{boisson}: {grammes}g = {cout_cafe:.3f} TND")

print()

# Estimation consommation totale
# Hypothèses: 70% du CA en boissons, mix produits
ca_boissons_an1 = 936660 * 0.70  # 655,662 TND
ticket_moyen_boisson = 10  # TND
nb_boissons_an1 = ca_boissons_an1 / ticket_moyen_boisson

# Mix estimé des boissons (en % du volume)
mix_boissons = {
    "Espresso/Americano": 0.25,  # 7g
    "Cappuccino/Cortado": 0.30,  # 7g  
    "Latte/Flat White": 0.25,    # 14g
    "Filter Coffee": 0.10,        # 15g
    "Cold Brew/Iced": 0.10       # 17g moyenne
}

print("=== CONSOMMATION TOTALE CAFÉ AN 1 ===")
consommation_totale_kg = 0
for categorie, pourcentage in mix_boissons.items():
    if "Espresso/Americano" in categorie:
        grammes_moy = 7
    elif "Cappuccino/Cortado" in categorie:
        grammes_moy = 7
    elif "Latte/Flat White" in categorie:
        grammes_moy = 14
    elif "Filter Coffee" in categorie:
        grammes_moy = 15
    else:  # Cold Brew/Iced
        grammes_moy = 17
    
    nb_boissons_cat = nb_boissons_an1 * pourcentage
    kg_categorie = (nb_boissons_cat * grammes_moy) / 1000
    consommation_totale_kg += kg_categorie
    
    print(f"{categorie}: {nb_boissons_cat:.0f} boissons × {grammes_moy}g = {kg_categorie:.1f} kg")

print(f"\nCONSOMMATION TOTALE: {consommation_totale_kg:.1f} kg/an")
print(f"COÛT CAFÉ TOTAL: {consommation_totale_kg * prix_cafe_tnd:.0f} TND/an")

# Impact sur les marges
cout_cafe_actuel_estime = consommation_totale_kg * 40  # Estimation prix local
cout_cafe_franchiseur = consommation_totale_kg * prix_cafe_tnd
surcoût = cout_cafe_franchiseur - cout_cafe_actuel_estime

print(f"\n=== IMPACT FINANCIER ===")
print(f"Coût café estimé local: {cout_cafe_actuel_estime:.0f} TND/an")
print(f"Coût café franchiseur: {cout_cafe_franchiseur:.0f} TND/an")
print(f"SURCOÛT: {surcoût:.0f} TND/an")
print(f"Impact sur marge: {(surcoût/936660)*100:.2f}% du CA")

# Impact sur résultat
resultat_an1_actuel = -191743
nouveau_resultat = resultat_an1_actuel - surcoût
print(f"\nRésultat An1 actuel: {resultat_an1_actuel:.0f} TND")
print(f"Nouveau résultat An1: {nouveau_resultat:.0f} TND")
print(f"Dégradation: {surcoût:.0f} TND")

