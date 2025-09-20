# Analyse impact ajustements tarifaires et coûts franchise

print("=== ANALYSE AJUSTEMENTS FRANCHISE ESPRESSOLAB ===")
print()

# 1. AJUSTEMENT PRIX ESPRESSO
print("1. AJUSTEMENT PRIX ESPRESSO")
print("Prix initial prévu: 4,00 TND")
print("Prix souhaité: 6,50 TND")
print("Augmentation: +62,5%")
print()

# Impact sur autres prix (cohérence gamme)
prix_actuels = {
    "Espresso": 4.00,
    "Double Espresso": 6.00,
    "Americano": 4.80,
    "Cappuccino": 7.00,
    "Latte": 8.00,
    "Flat White": 7.50,
    "Cortado": 6.50,
    "Macchiato": 6.00
}

# Nouveau pricing avec espresso à 6,50 TND
facteur_augmentation = 6.50 / 4.00  # 1.625
print("NOUVEAUX PRIX SUGGÉRÉS (cohérence gamme):")
for produit, prix in prix_actuels.items():
    if produit == "Espresso":
        nouveau_prix = 6.50
    else:
        nouveau_prix = prix * facteur_augmentation
    print(f"{produit}: {prix:.2f} → {nouveau_prix:.2f} TND (+{((nouveau_prix/prix-1)*100):.1f}%)")

print()

# 2. DROITS D'ENTRÉE FRANCHISE
print("2. DROITS D'ENTRÉE FRANCHISE")
droits_entree_usd = 50000
taux_change = 3.15
droits_entree_tnd = droits_entree_usd * taux_change
print(f"Droits d'entrée: {droits_entree_usd}$ = {droits_entree_tnd:,.0f} TND")
print("MANQUANT dans l'investissement initial actuel!")
print()

# 3. ROYALTIES 6%
print("3. ROYALTIES FRANCHISEUR")
ca_an1 = 936660
royalties_an1 = ca_an1 * 0.06
print(f"CA An1: {ca_an1:,.0f} TND")
print(f"Royalties 6%: {royalties_an1:,.0f} TND/an = {royalties_an1/12:,.0f} TND/mois")
print("MANQUANT dans les charges fixes actuelles!")
print()

# 4. COÛTS TRAVAUX/ÉQUIPEMENTS FRANCHISEUR
print("4. COÛTS TRAVAUX/ÉQUIPEMENTS FRANCHISEUR")
print("Investissement actuel estimé: 332,000 USD")
print("Mais si TOUT fourni par franchiseur:")
print("- Mobilier: +30-40% vs standard")
print("- Équipements: +20-30% vs marché")
print("- Design/Aménagement: +25-35% vs local")
print("Estimation surcoût: +25-30% minimum")

cout_actuel_usd = 332000
surcout_franchiseur = cout_actuel_usd * 0.275  # 27.5% moyenne
nouveau_cout_usd = cout_actuel_usd + surcout_franchiseur
nouveau_cout_tnd = nouveau_cout_usd * taux_change

print(f"Coût estimé avec franchiseur: {nouveau_cout_usd:,.0f}$ = {nouveau_cout_tnd:,.0f} TND")
print(f"Surcoût: {surcout_franchiseur:,.0f}$ = {surcout_franchiseur * taux_change:,.0f} TND")
print()

# IMPACT TOTAL SUR INVESTISSEMENT
print("=== IMPACT TOTAL INVESTISSEMENT ===")
investissement_actuel = 1211836
droits_entree = 157500
surcout_travaux = surcout_franchiseur * taux_change
nouvel_investissement = investissement_actuel + droits_entree + surcout_travaux

print(f"Investissement actuel: {investissement_actuel:,.0f} TND")
print(f"+ Droits d'entrée: {droits_entree:,.0f} TND")
print(f"+ Surcoût travaux: {surcout_travaux:,.0f} TND")
print(f"NOUVEL INVESTISSEMENT: {nouvel_investissement:,.0f} TND")
print(f"Augmentation: +{((nouvel_investissement/investissement_actuel-1)*100):.1f}%")
print()

# IMPACT SUR CHARGES FIXES
print("=== IMPACT CHARGES FIXES ===")
charges_fixes_actuelles = 781836
nouvelles_royalties = royalties_an1
nouvelles_charges_fixes = charges_fixes_actuelles + nouvelles_royalties

print(f"Charges fixes actuelles: {charges_fixes_actuelles:,.0f} TND/an")
print(f"+ Royalties 6%: {nouvelles_royalties:,.0f} TND/an")
print(f"NOUVELLES CHARGES FIXES: {nouvelles_charges_fixes:,.0f} TND/an")
print(f"Augmentation: +{((nouvelles_charges_fixes/charges_fixes_actuelles-1)*100):.1f}%")
print()

# NOUVEAU SEUIL DE RENTABILITÉ
print("=== NOUVEAU SEUIL DE RENTABILITÉ ===")
marge_variable = 0.656  # Avec café franchiseur
nouveau_seuil_ca = nouvelles_charges_fixes / marge_variable
ticket_moyen_nouveau = 13 * facteur_augmentation  # Avec nouveaux prix
nouveau_seuil_clients = nouveau_seuil_ca / (ticket_moyen_nouveau * 360)

print(f"Nouvelles charges fixes: {nouvelles_charges_fixes:,.0f} TND")
print(f"Marge variable: {marge_variable:.1%}")
print(f"Nouveau seuil CA: {nouveau_seuil_ca:,.0f} TND")
print(f"Nouveau ticket moyen: {ticket_moyen_nouveau:.2f} TND")
print(f"NOUVEAU SEUIL: {nouveau_seuil_clients:.0f} clients/jour")
print()

print("=== RÉSUMÉ IMPACTS ===")
print(f"1. Investissement: +{((nouvel_investissement/investissement_actuel-1)*100):.1f}% ({nouvel_investissement-investissement_actuel:,.0f} TND)")
print(f"2. Charges fixes: +{((nouvelles_charges_fixes/charges_fixes_actuelles-1)*100):.1f}% ({nouvelles_royalties:,.0f} TND/an)")
print(f"3. Prix espresso: +62,5% (4,00 → 6,50 TND)")
print(f"4. Seuil rentabilité: {nouveau_seuil_clients:.0f} clients/jour")

