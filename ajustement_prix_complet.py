# Calcul ajustement tarifaire nécessaire avec investissement réel

print("=== AJUSTEMENT TARIFAIRE AVEC INVESTISSEMENT RÉEL ===")
print()

# Données de base
investissement_initial = 1211836  # TND
investissement_reel = 2283656     # TND
augmentation_invest = (investissement_reel / investissement_initial - 1) * 100

print(f"Investissement initial estimé: {investissement_initial:,.0f} TND")
print(f"Investissement réel (fichier): {investissement_reel:,.0f} TND")
print(f"Augmentation: +{augmentation_invest:.1f}%")
print()

# Impact sur les charges fixes (amortissements)
duree_amortissement = 5  # ans
amortissement_initial = investissement_initial / duree_amortissement
amortissement_reel = investissement_reel / duree_amortissement
surcoût_amortissement = amortissement_reel - amortissement_initial

print(f"Amortissement initial: {amortissement_initial:,.0f} TND/an")
print(f"Amortissement réel: {amortissement_reel:,.0f} TND/an")
print(f"Surcoût amortissement: +{surcoût_amortissement:,.0f} TND/an")
print()

# Charges fixes totales révisées
charges_fixes_base = 781836  # TND/an
royalties = 56200           # TND/an (6% du CA estimé)
charges_fixes_totales = charges_fixes_base + royalties + surcoût_amortissement

print(f"Charges fixes base: {charges_fixes_base:,.0f} TND/an")
print(f"+ Royalties 6%: {royalties:,.0f} TND/an")
print(f"+ Surcoût amortissement: {surcoût_amortissement:,.0f} TND/an")
print(f"CHARGES FIXES TOTALES: {charges_fixes_totales:,.0f} TND/an")
print()

# Calcul nouveau seuil de rentabilité
marge_variable = 0.656  # 65.6% avec café franchiseur
nouveau_seuil_ca = charges_fixes_totales / marge_variable

print(f"Marge variable: {marge_variable:.1%}")
print(f"NOUVEAU SEUIL CA: {nouveau_seuil_ca:,.0f} TND/an")
print()

# Calcul ticket moyen nécessaire
clients_jour_cible = 200  # Objectif réaliste
jours_ouverture = 360
clients_annuels = clients_jour_cible * jours_ouverture
ticket_moyen_necessaire = nouveau_seuil_ca / clients_annuels

print(f"Objectif clients: {clients_jour_cible} clients/jour")
print(f"Clients annuels: {clients_annuels:,.0f}")
print(f"TICKET MOYEN NÉCESSAIRE: {ticket_moyen_necessaire:.2f} TND")
print()

# Comparaison avec pricing actuel
ticket_actuel_espresso_6_50 = 21.12  # TND calculé précédemment
augmentation_ticket_necessaire = (ticket_moyen_necessaire / ticket_actuel_espresso_6_50 - 1) * 100

print(f"Ticket moyen avec espresso 6,50 TND: {ticket_actuel_espresso_6_50:.2f} TND")
print(f"Ticket moyen nécessaire: {ticket_moyen_necessaire:.2f} TND")
print(f"AUGMENTATION NÉCESSAIRE: +{augmentation_ticket_necessaire:.1f}%")
print()

# Nouveau pricing suggéré
print("=== NOUVEAU PRICING SUGGÉRÉ ===")
facteur_augmentation = ticket_moyen_necessaire / ticket_actuel_espresso_6_50

prix_actuels = {
    "Espresso": 6.50,
    "Double Espresso": 9.75,
    "Americano": 7.80,
    "Cappuccino": 11.40,
    "Latte": 13.00,
    "Flat White": 12.20,
    "Cortado": 10.56,
    "Macchiato": 9.75,
    "Mocha": 15.44,
    "V60 Pour Over": 14.63,
    "Cold Brew": 11.38,
    "Croissant": 9.75,
    "Avocado Toast": 21.13,
    "Salade César": 27.63,
    "Buddha Bowl": 32.50
}

print("BOISSONS:")
for produit, prix in prix_actuels.items():
    if any(x in produit for x in ["Espresso", "Americano", "Cappuccino", "Latte", "Flat", "Cortado", "Macchiato", "Mocha", "V60", "Cold"]):
        nouveau_prix = prix * facteur_augmentation
        print(f"{produit}: {prix:.2f} → {nouveau_prix:.2f} TND (+{((nouveau_prix/prix-1)*100):.1f}%)")

print("\nFOOD:")
for produit, prix in prix_actuels.items():
    if any(x in produit for x in ["Croissant", "Avocado", "Salade", "Buddha"]):
        nouveau_prix = prix * facteur_augmentation
        print(f"{produit}: {prix:.2f} → {nouveau_prix:.2f} TND (+{((nouveau_prix/prix-1)*100):.1f}%)")

print()

# Analyse concurrentielle
print("=== ANALYSE CONCURRENTIELLE ===")
nouveau_prix_espresso = 6.50 * facteur_augmentation
nouveau_prix_cappuccino = 11.40 * facteur_augmentation
nouveau_prix_latte = 13.00 * facteur_augmentation

print(f"Espresso Espressolab: {nouveau_prix_espresso:.2f} TND")
print(f"Cappuccino Espressolab: {nouveau_prix_cappuccino:.2f} TND")
print(f"Latte Espressolab: {nouveau_prix_latte:.2f} TND")
print()
print("Comparaison concurrence:")
print("Starbucks Tunisie (estimé): 9-18 TND")
print("Costa Coffee (estimé): 8-16 TND")
print("Cafés locaux premium: 5-8 TND")
print()

# Évaluation acceptabilité
if nouveau_prix_espresso > 12:
    print("⚠️  ATTENTION: Prix espresso > 12 TND peut être trop élevé pour le marché tunisien")
elif nouveau_prix_espresso > 10:
    print("⚠️  PRUDENCE: Prix espresso > 10 TND nécessite positionnement ultra-premium")
else:
    print("✅ Prix espresso acceptable pour le marché tunisien")

print()
print("=== RECOMMANDATIONS ===")
print(f"1. Ticket moyen cible: {ticket_moyen_necessaire:.2f} TND")
print(f"2. Espresso recommandé: {nouveau_prix_espresso:.2f} TND")
print(f"3. Positionnement: Ultra-premium nécessaire")
print(f"4. Alternative: Réduire les coûts d'investissement")

