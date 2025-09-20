# Recalcul financier avec les données RÉELLES uniquement

print("=== RECALCUL FINANCIER BASÉ SUR DONNÉES RÉELLES ===")
print()

# DONNÉES RÉELLES CONFIRMÉES
donnees_reelles = {
    "cafe_cout_kg": 126.86,  # TND/kg (du fichier EspressoLab.xlsx)
    "investissement_total": 2283656,  # TND (du fichier INVESTMENTCOST.xlsx)
    "droits_entree": 157500,  # TND (50k USD × 3.15)
    "royalties_pct": 0.06,  # 6% du CA
    "loyer_mensuel": 20000,  # TND/mois (flagship store)
    "pas_de_porte": 200000   # TND
}

print("=== DONNÉES RÉELLES UTILISÉES ===")
print(f"Coût café franchiseur: {donnees_reelles['cafe_cout_kg']} TND/kg")
print(f"Investissement total: {donnees_reelles['investissement_total']:,} TND")
print(f"Droits d'entrée: {donnees_reelles['droits_entree']:,} TND")
print(f"Royalties: {donnees_reelles['royalties_pct']*100}% du CA")
print(f"Loyer flagship: {donnees_reelles['loyer_mensuel']:,} TND/mois")
print()

# CARTE PRODUITS RÉELLE (basée sur analyse)
produits_reels = {
    "espresso": {"prix": 6.50, "cout_cafe": 0.95, "cout_tasse": 0.21, "part_ventes": 0.25},
    "cappuccino": {"prix": 10.00, "cout_cafe": 0.95, "cout_tasse": 0.28, "part_ventes": 0.20},
    "latte": {"prix": 11.00, "cout_cafe": 0.95, "cout_tasse": 0.42, "part_ventes": 0.15},
    "americano": {"prix": 8.00, "cout_cafe": 0.95, "cout_tasse": 0.42, "part_ventes": 0.15},
    "cold_brew": {"prix": 13.00, "cout_cafe": 2.54, "cout_tasse": 0.78, "part_ventes": 0.10},
    "filter_coffee": {"prix": 15.00, "cout_cafe": 2.54, "cout_tasse": 0.42, "part_ventes": 0.05},
    "the_chocolat": {"prix": 7.00, "cout_cafe": 0, "cout_tasse": 0.42, "part_ventes": 0.10}
}

# CALCUL TICKET MOYEN RÉEL
ticket_moyen = 0
cout_moyen_produit = 0

print("=== ANALYSE PRODUITS RÉELS ===")
for produit, data in produits_reels.items():
    contribution_ca = data["prix"] * data["part_ventes"]
    cout_total = data["cout_cafe"] + data["cout_tasse"] + (data["prix"] * 0.15)  # +15% autres coûts
    contribution_cout = cout_total * data["part_ventes"]
    marge = (data["prix"] - cout_total) / data["prix"] * 100
    
    ticket_moyen += contribution_ca
    cout_moyen_produit += contribution_cout
    
    print(f"{produit.replace('_', ' ').title()}: {data['prix']} TND ({data['part_ventes']*100:.0f}%) - Marge: {marge:.0f}%")

marge_brute_pct = (ticket_moyen - cout_moyen_produit) / ticket_moyen

print(f"\nTICKET MOYEN RÉEL: {ticket_moyen:.2f} TND")
print(f"COÛT MOYEN PRODUIT: {cout_moyen_produit:.2f} TND")
print(f"MARGE BRUTE: {marge_brute_pct*100:.1f}%")
print()

# HYPOTHÈSES TRAFIC
clients_jour = 200  # Hypothèse conservative
jours_an = 360

# CALCUL CA ET CHARGES
ca_annuel = clients_jour * jours_an * ticket_moyen
royalties = ca_annuel * donnees_reelles['royalties_pct']
loyer_annuel = donnees_reelles['loyer_mensuel'] * 12

# CHARGES FIXES RÉELLES
charges_fixes = {
    "loyer": loyer_annuel,
    "royalties": royalties,
    "salaires": 359436,  # TND/an (15 personnes)
    "utilities": 48000,   # TND/an
    "marketing": 24000,   # TND/an
    "assurances": 9600,   # TND/an
    "autres": 36000       # TND/an
}

total_charges_fixes = sum(charges_fixes.values())
marge_brute = ca_annuel * marge_brute_pct
resultat_net = marge_brute - total_charges_fixes

print("=== PRÉVISIONNEL FINANCIER RÉEL ===")
print(f"CA annuel: {ca_annuel:,.0f} TND ({clients_jour} clients/jour × {ticket_moyen:.2f} TND)")
print(f"Marge brute: {marge_brute:,.0f} TND ({marge_brute_pct*100:.1f}%)")
print()
print("CHARGES FIXES:")
for charge, montant in charges_fixes.items():
    print(f"  {charge.title()}: {montant:,.0f} TND")
print(f"TOTAL CHARGES: {total_charges_fixes:,.0f} TND")
print()
print(f"RÉSULTAT NET AN1: {resultat_net:+,.0f} TND")
print()

# SEUIL DE RENTABILITÉ
seuil_ca = total_charges_fixes / marge_brute_pct
seuil_clients_jour = seuil_ca / (ticket_moyen * 360)

print("=== SEUIL DE RENTABILITÉ ===")
print(f"Seuil CA: {seuil_ca:,.0f} TND/an")
print(f"Seuil clients/jour: {seuil_clients_jour:.0f} clients/jour")
print(f"Avec {clients_jour} clients/jour: {'✅ RENTABLE' if clients_jour > seuil_clients_jour else '❌ NON RENTABLE'}")
print()

# ANALYSE DE SENSIBILITÉ
print("=== ANALYSE DE SENSIBILITÉ ===")
scenarios = [150, 200, 250, 300, 350, 400]
for scenario_clients in scenarios:
    scenario_ca = scenario_clients * 360 * ticket_moyen
    scenario_royalties = scenario_ca * 0.06
    scenario_charges = total_charges_fixes - royalties + scenario_royalties
    scenario_marge = scenario_ca * marge_brute_pct
    scenario_resultat = scenario_marge - scenario_charges
    
    print(f"{scenario_clients} clients/jour: CA {scenario_ca:,.0f} TND → Résultat {scenario_resultat:+,.0f} TND")

print()
if resultat_net < 0:
    clients_necessaires = int(seuil_clients_jour) + 1
    print(f"⚠️  BESOIN MINIMUM: {clients_necessaires} clients/jour pour équilibre")
    print(f"   Écart à combler: +{clients_necessaires - clients_jour} clients/jour")
else:
    print("✅ PROJET VIABLE avec les données réelles")

