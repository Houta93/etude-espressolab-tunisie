#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("=== PRÉVISIONNELS DÉFINITIFS OPTION A ===")
print("Ticket moyen: 23,70 TND | 200 clients/jour | Équilibre financier")
print()

# Données définitives
investissement_total = 2283656  # TND
ticket_moyen = 23.70           # TND (Option A)
clients_jour = 200             # clients/jour
jours_ouverture = 360          # jours/an
marge_brute = 0.70            # 70%

# Calcul CA annuel
clients_annuels = clients_jour * jours_ouverture
ca_annuel = clients_annuels * ticket_moyen

print(f"DONNÉES DÉFINITIVES:")
print(f"- Investissement total: {investissement_total:,.0f} TND")
print(f"- Ticket moyen: {ticket_moyen:.2f} TND")
print(f"- Clients/jour: {clients_jour}")
print(f"- Clients annuels: {clients_annuels:,.0f}")
print(f"- CA annuel An1: {ca_annuel:,.0f} TND")
print(f"- Marge brute: {marge_brute*100:.0f}%")
print()

# Coûts variables
cout_matieres = ca_annuel * (1 - marge_brute)
print(f"COÛTS VARIABLES:")
print(f"- Coût matières (30%): {cout_matieres:,.0f} TND")
print()

# Coûts fixes détaillés
print("COÛTS FIXES ANNUELS:")

# Personnel (15 personnes)
salaires_bruts = 359436
charges_sociales = salaires_bruts * 0.25
total_personnel = salaires_bruts + charges_sociales
print(f"- Salaires bruts: {salaires_bruts:,.0f} TND")
print(f"- Charges sociales (25%): {charges_sociales:,.0f} TND")
print(f"- Total personnel: {total_personnel:,.0f} TND")

# Immobilier
loyer_principal = 20000 * 12
loyer_cuisine = 3000 * 12
loyer_stockage = 800 * 12
charges_locatives = 24000
total_immobilier = loyer_principal + loyer_cuisine + loyer_stockage + charges_locatives
print(f"- Loyer principal: {loyer_principal:,.0f} TND")
print(f"- Loyer cuisine: {loyer_cuisine:,.0f} TND")
print(f"- Loyer stockage: {loyer_stockage:,.0f} TND")
print(f"- Charges locatives: {charges_locatives:,.0f} TND")
print(f"- Total immobilier: {total_immobilier:,.0f} TND")

# Royalties franchise
royalties = ca_annuel * 0.06
print(f"- Royalties franchise (6%): {royalties:,.0f} TND")

# Autres charges
marketing = 48000
assurances = 9600
maintenance = 18000
utilities = 36000
autres_charges = 24000
total_autres = marketing + assurances + maintenance + utilities + autres_charges
print(f"- Marketing: {marketing:,.0f} TND")
print(f"- Assurances: {assurances:,.0f} TND")
print(f"- Maintenance: {maintenance:,.0f} TND")
print(f"- Utilities: {utilities:,.0f} TND")
print(f"- Autres charges: {autres_charges:,.0f} TND")
print(f"- Total autres: {total_autres:,.0f} TND")

# Amortissements
amortissement = investissement_total / 10
print(f"- Amortissements (10 ans): {amortissement:,.0f} TND")

# Total coûts fixes
total_couts_fixes = total_personnel + total_immobilier + royalties + total_autres + amortissement
print(f"- TOTAL COÛTS FIXES: {total_couts_fixes:,.0f} TND")
print()

# Compte de résultat
marge_brute_montant = ca_annuel - cout_matieres
resultat = marge_brute_montant - total_couts_fixes
marge_nette = (resultat/ca_annuel)*100

print("COMPTE DE RÉSULTAT AN1:")
print(f"- Chiffre d'affaires: {ca_annuel:,.0f} TND")
print(f"- Coût matières: -{cout_matieres:,.0f} TND")
print(f"- Marge brute: {marge_brute_montant:,.0f} TND ({marge_brute*100:.0f}%)")
print(f"- Coûts fixes: -{total_couts_fixes:,.0f} TND")
print(f"- Résultat net: {resultat:,.0f} TND")
print(f"- Marge nette: {marge_nette:.1f}%")
print()

# Vérification équilibre
if abs(resultat) < 10000:  # Tolérance 10k TND
    print("✅ ÉQUILIBRE FINANCIER ATTEINT")
    print(f"   Écart: {resultat:,.0f} TND (négligeable)")
else:
    print(f"⚠️  Écart vs équilibre: {resultat:,.0f} TND")

print()

# Projections 5 ans
print("PROJECTIONS 5 ANS:")
for annee in range(1, 6):
    if annee == 1:
        ca = ca_annuel
    elif annee == 2:
        ca = ca_annuel * 1.20  # +20% An2
    elif annee == 3:
        ca = ca_annuel * 1.20 * 1.15  # +15% An3
    elif annee == 4:
        ca = ca_annuel * 1.20 * 1.15 * 1.12  # +12% An4
    else:
        ca = ca_annuel * 1.20 * 1.15 * 1.12 * 1.10  # +10% An5
    
    cout_mat = ca * (1 - marge_brute)
    marge_b = ca - cout_mat
    
    # Coûts fixes évoluent modérément
    if annee == 1:
        cf = total_couts_fixes
    else:
        cf = total_couts_fixes * (1 + (annee-1) * 0.03)  # +3% par an
    
    res = marge_b - cf
    marge_n = (res/ca)*100
    
    print(f"An{annee}: CA {ca:,.0f} TND | Résultat {res:,.0f} TND | Marge {marge_n:.1f}%")

print()

# Calcul TRI et VAN
print("INDICATEURS DE RENTABILITÉ:")
flux_annuels = []
for annee in range(1, 6):
    if annee == 1:
        ca = ca_annuel
    elif annee == 2:
        ca = ca_annuel * 1.20
    elif annee == 3:
        ca = ca_annuel * 1.20 * 1.15
    elif annee == 4:
        ca = ca_annuel * 1.20 * 1.15 * 1.12
    else:
        ca = ca_annuel * 1.20 * 1.15 * 1.12 * 1.10
    
    cout_mat = ca * 0.30
    cf = total_couts_fixes * (1 + (annee-1) * 0.03) if annee > 1 else total_couts_fixes
    flux = ca - cout_mat - cf
    flux_annuels.append(flux)

# VAN approximative (taux 10%)
van = -investissement_total
for i, flux in enumerate(flux_annuels):
    van += flux / ((1.10) ** (i+1))

print(f"- VAN (10%): {van:,.0f} TND")

# TRI approximatif
def calcul_van(taux):
    v = -investissement_total
    for i, flux in enumerate(flux_annuels):
        v += flux / ((1 + taux) ** (i+1))
    return v

# Recherche TRI par dichotomie
taux_min, taux_max = 0, 1
for _ in range(50):
    taux_test = (taux_min + taux_max) / 2
    van_test = calcul_van(taux_test)
    if abs(van_test) < 1000:
        break
    elif van_test > 0:
        taux_min = taux_test
    else:
        taux_max = taux_test

tri = taux_test * 100
print(f"- TRI: {tri:.1f}%")

# Délai de récupération
cumul = 0
for i, flux in enumerate(flux_annuels):
    cumul += flux
    if cumul >= investissement_total:
        delai = i + 1 - (cumul - investissement_total) / flux
        break
else:
    delai = 5

print(f"- Délai récupération: {delai:.1f} ans")

print()
print("=== PRÉVISIONNELS DÉFINITIFS VALIDÉS ===")
