#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("=== OPTIMISATION POUR RENTABILITÉ AVEC INVESTISSEMENT RÉEL ===")
print()

# Données fixes (non négociables)
investissement_total = 2283656  # TND
marge_brute = 0.70             # 70%
jours_ouverture = 360          # jours/an

# Coûts fixes (non négociables)
total_personnel = 449295       # TND/an
total_immobilier = 309600      # TND/an
total_autres = 135600          # TND/an
amortissement = 228366         # TND/an

print("DONNÉES FIXES (NON NÉGOCIABLES):")
print(f"- Investissement: {investissement_total:,.0f} TND")
print(f"- Personnel: {total_personnel:,.0f} TND/an")
print(f"- Immobilier: {total_immobilier:,.0f} TND/an")
print(f"- Autres charges: {total_autres:,.0f} TND/an")
print(f"- Amortissements: {amortissement:,.0f} TND/an")
print()

# Scénarios d'optimisation
scenarios = [
    {"nom": "Scénario 1: Trafic Modéré", "clients_jour": 250, "ticket_base": 13.09},
    {"nom": "Scénario 2: Trafic Élevé", "clients_jour": 300, "ticket_base": 13.09},
    {"nom": "Scénario 3: Premium Modéré", "clients_jour": 200, "ticket_base": 16.00},
    {"nom": "Scénario 4: Premium Élevé", "clients_jour": 200, "ticket_base": 20.00},
    {"nom": "Scénario 5: Mixte Optimal", "clients_jour": 275, "ticket_base": 15.50},
]

print("ANALYSE DES SCÉNARIOS D'OPTIMISATION:")
print("=" * 80)

for scenario in scenarios:
    clients_jour = scenario["clients_jour"]
    ticket_moyen = scenario["ticket_base"]
    
    # Calculs
    clients_annuels = clients_jour * jours_ouverture
    ca_annuel = clients_annuels * ticket_moyen
    cout_matieres = ca_annuel * (1 - marge_brute)
    royalties = ca_annuel * 0.06
    
    total_couts_fixes = total_personnel + total_immobilier + royalties + total_autres + amortissement
    marge_brute_montant = ca_annuel - cout_matieres
    resultat = marge_brute_montant - total_couts_fixes
    marge_nette = (resultat/ca_annuel)*100 if ca_annuel > 0 else 0
    
    # Seuil de rentabilité
    marge_unitaire = ticket_moyen * marge_brute
    seuil_clients_jour = total_couts_fixes / (marge_unitaire * jours_ouverture)
    
    print(f"\n{scenario['nom']}:")
    print(f"  Clients/jour: {clients_jour} | Ticket: {ticket_moyen:.2f} TND")
    print(f"  CA annuel: {ca_annuel:,.0f} TND")
    print(f"  Coûts fixes: {total_couts_fixes:,.0f} TND")
    print(f"  Résultat: {resultat:,.0f} TND")
    print(f"  Marge nette: {marge_nette:.1f}%")
    print(f"  Seuil requis: {seuil_clients_jour:.0f} clients/jour")
    
    if resultat > 0:
        print(f"  ✅ RENTABLE - Excédent: {resultat:,.0f} TND")
    else:
        print(f"  ❌ DÉFICITAIRE - Manque: {-resultat:,.0f} TND")
    
    if clients_jour >= seuil_clients_jour:
        print(f"  ✅ SEUIL ATTEINT - Marge: {clients_jour - seuil_clients_jour:.0f} clients")
    else:
        print(f"  ❌ SEUIL NON ATTEINT - Manque: {seuil_clients_jour - clients_jour:.0f} clients")

print("\n" + "=" * 80)

# Calcul du scénario optimal pour équilibre
print("\nCALCUL DU SCÉNARIO D'ÉQUILIBRE:")

# Pour 200 clients/jour, quel ticket faut-il ?
clients_cible = 200
ca_equilibre = total_personnel + total_immobilier + total_autres + amortissement  # Sans royalties d'abord
ticket_equilibre_base = ca_equilibre / (clients_cible * jours_ouverture * marge_brute)

# Ajout des royalties (6% du CA)
ticket_equilibre_final = ticket_equilibre_base / (1 - 0.06)

print(f"Pour {clients_cible} clients/jour:")
print(f"- Ticket nécessaire pour équilibre: {ticket_equilibre_final:.2f} TND")
print(f"- Augmentation vs actuel (13.09): +{((ticket_equilibre_final/13.09)-1)*100:.1f}%")

# Pour ticket actuel, combien de clients faut-il ?
ticket_actuel = 13.09
marge_unitaire_actuelle = ticket_actuel * marge_brute
# Coûts fixes avec royalties moyennes
couts_fixes_moyens = total_personnel + total_immobilier + total_autres + amortissement + (ticket_actuel * 200 * 360 * 0.06)
clients_equilibre = couts_fixes_moyens / (marge_unitaire_actuelle * jours_ouverture)

print(f"\nPour ticket actuel ({ticket_actuel} TND):")
print(f"- Clients nécessaires pour équilibre: {clients_equilibre:.0f} clients/jour")
print(f"- Augmentation vs prévision (200): +{((clients_equilibre/200)-1)*100:.1f}%")

print("\n" + "=" * 80)
print("RECOMMANDATIONS STRATÉGIQUES:")

print("\n1. SCÉNARIO RÉALISTE RECOMMANDÉ:")
print("   - Clients/jour: 275 (objectif ambitieux mais atteignable)")
print("   - Ticket moyen: 15,50 TND (+18% vs actuel)")
print("   - Stratégie: Premium accessible + marketing agressif")

print("\n2. ACTIONS CONCRÈTES:")
print("   - Augmenter prix boissons signature: +20-25%")
print("   - Développer offre premium (filter coffee, spécialités)")
print("   - Marketing d'ouverture intensif")
print("   - Partenariats entreprises/bureaux")
print("   - Programme fidélité attractif")

print("\n3. PLAN DE MONTÉE EN CHARGE:")
print("   - Mois 1-3: 150 clients/jour (phase lancement)")
print("   - Mois 4-6: 200 clients/jour (phase croissance)")
print("   - Mois 7-12: 275 clients/jour (phase maturité)")

print("\n=== FIN DE L'ANALYSE D'OPTIMISATION ===")
