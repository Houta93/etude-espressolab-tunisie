#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("=== RECALCUL FINANCIER COMPLET AVEC NOUVELLE CARTE PRODUITS ===")
print()

# Données de base
investissement_total = 2283656  # TND
ticket_moyen_nouveau = 13.36   # TND (calculé avec nouvelle carte)
clients_jour_prevu = 200       # clients/jour
jours_ouverture = 360          # jours/an
marge_brute = 0.68            # 68%

# Calcul CA annuel
clients_annuels = clients_jour_prevu * jours_ouverture
ca_annuel = clients_annuels * ticket_moyen_nouveau

print(f"DONNÉES DE BASE:")
print(f"- Investissement total: {investissement_total:,.0f} TND")
print(f"- Ticket moyen (nouvelle carte): {ticket_moyen_nouveau:.2f} TND")
print(f"- Clients/jour prévus: {clients_jour_prevu}")
print(f"- Jours d'ouverture: {jours_ouverture}")
print(f"- Clients annuels: {clients_annuels:,.0f}")
print(f"- CA annuel An1: {ca_annuel:,.0f} TND")
print()

# Coûts variables (32% du CA)
cout_matieres = ca_annuel * (1 - marge_brute)
print(f"COÛTS VARIABLES:")
print(f"- Coût matières (32%): {cout_matieres:,.0f} TND")
print()

# Coûts fixes détaillés
print("COÛTS FIXES ANNUELS:")

# Personnel (15 personnes)
salaires_bruts = 359436  # TND/an
charges_sociales = salaires_bruts * 0.25
total_personnel = salaires_bruts + charges_sociales
print(f"- Salaires bruts: {salaires_bruts:,.0f} TND")
print(f"- Charges sociales (25%): {charges_sociales:,.0f} TND")
print(f"- Total personnel: {total_personnel:,.0f} TND")

# Loyers et charges
loyer_principal = 20000 * 12  # 20k TND/mois
loyer_cuisine = 3000 * 12     # 3k TND/mois  
loyer_stockage = 800 * 12     # 800 TND/mois
charges_locatives = 24000     # TND/an
total_immobilier = loyer_principal + loyer_cuisine + loyer_stockage + charges_locatives
print(f"- Loyer principal (20k/mois): {loyer_principal:,.0f} TND")
print(f"- Loyer cuisine centrale: {loyer_cuisine:,.0f} TND")
print(f"- Loyer stockage: {loyer_stockage:,.0f} TND")
print(f"- Charges locatives: {charges_locatives:,.0f} TND")
print(f"- Total immobilier: {total_immobilier:,.0f} TND")

# Royalties franchise (6% du CA)
royalties = ca_annuel * 0.06
print(f"- Royalties franchise (6%): {royalties:,.0f} TND")

# Autres charges d'exploitation
marketing = 48000      # TND/an
assurances = 9600      # TND/an
maintenance = 18000    # TND/an
utilities = 36000      # TND/an (électricité, eau, internet)
autres_charges = 24000 # TND/an
total_autres = marketing + assurances + maintenance + utilities + autres_charges
print(f"- Marketing: {marketing:,.0f} TND")
print(f"- Assurances: {assurances:,.0f} TND")
print(f"- Maintenance: {maintenance:,.0f} TND")
print(f"- Utilities: {utilities:,.0f} TND")
print(f"- Autres charges: {autres_charges:,.0f} TND")
print(f"- Total autres charges: {total_autres:,.0f} TND")

# Amortissements
amortissement_annuel = investissement_total / 10  # 10 ans
print(f"- Amortissements (10 ans): {amortissement_annuel:,.0f} TND")

# Total coûts fixes
total_couts_fixes = total_personnel + total_immobilier + royalties + total_autres + amortissement_annuel
print(f"- TOTAL COÛTS FIXES: {total_couts_fixes:,.0f} TND")
print()

# Résultat d'exploitation
marge_brute_montant = ca_annuel - cout_matieres
resultat_exploitation = marge_brute_montant - total_couts_fixes

print("COMPTE DE RÉSULTAT AN1:")
print(f"- Chiffre d'affaires: {ca_annuel:,.0f} TND")
print(f"- Coût matières: -{cout_matieres:,.0f} TND")
print(f"- Marge brute: {marge_brute_montant:,.0f} TND ({marge_brute*100:.1f}%)")
print(f"- Coûts fixes: -{total_couts_fixes:,.0f} TND")
print(f"- Résultat d'exploitation: {resultat_exploitation:,.0f} TND")
print(f"- Marge nette: {(resultat_exploitation/ca_annuel)*100:.1f}%")
print()

# Seuil de rentabilité
marge_unitaire = ticket_moyen_nouveau * marge_brute
seuil_clients_jour = total_couts_fixes / (marge_unitaire * jours_ouverture)
seuil_ca_annuel = seuil_clients_jour * ticket_moyen_nouveau * jours_ouverture

print("SEUIL DE RENTABILITÉ:")
print(f"- Marge unitaire: {marge_unitaire:.2f} TND/client")
print(f"- Seuil clients/jour: {seuil_clients_jour:.0f} clients")
print(f"- Seuil CA annuel: {seuil_ca_annuel:,.0f} TND")
print(f"- Écart vs prévision: {seuil_clients_jour - clients_jour_prevu:.0f} clients/jour")
print()

# Analyse de viabilité
if seuil_clients_jour <= clients_jour_prevu:
    print("✅ PROJET VIABLE - Seuil atteignable")
else:
    print("❌ PROJET NON VIABLE - Seuil trop élevé")
    print(f"   Besoin d'augmenter le trafic de {clients_jour_prevu} à {seuil_clients_jour:.0f} clients/jour")
    print(f"   Ou augmenter le ticket moyen de {ticket_moyen_nouveau:.2f} à {(total_couts_fixes/(clients_jour_prevu * marge_brute * jours_ouverture)):.2f} TND")

print()

# Projections 5 ans
print("PROJECTIONS 5 ANS:")
for annee in range(1, 6):
    if annee == 1:
        ca = ca_annuel
        croissance = 0
    elif annee == 2:
        croissance = 0.25  # +25% An2
        ca = ca_annuel * (1 + croissance)
    elif annee == 3:
        croissance = 0.15  # +15% An3
        ca = ca_annuel * 1.25 * (1 + croissance)
    elif annee == 4:
        croissance = 0.12  # +12% An4
        ca = ca_annuel * 1.25 * 1.15 * (1 + croissance)
    else:
        croissance = 0.10  # +10% An5
        ca = ca_annuel * 1.25 * 1.15 * 1.12 * (1 + croissance)
    
    cout_mat = ca * (1 - marge_brute)
    marge_b = ca - cout_mat
    
    # Coûts fixes évoluent moins vite
    if annee == 1:
        cf = total_couts_fixes
    else:
        cf = total_couts_fixes * (1 + (annee-1) * 0.03)  # +3% par an
    
    resultat = marge_b - cf
    marge_nette = (resultat/ca)*100
    
    print(f"An{annee}: CA {ca:,.0f} TND | Résultat {resultat:,.0f} TND | Marge {marge_nette:.1f}%")

print()
print("=== FIN DU CALCUL ===")
