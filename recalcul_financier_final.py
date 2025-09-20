# Recalcul financier avec les nouveaux prix réalistes

print("=== RECALCUL FINANCIER AVEC NOUVEAUX PRIX ===")
print()

# ANCIENS PRIX (incohérents)
anciens_prix = {
    "ticket_moyen": 22.28,
    "espresso": 6.86,
    "cappuccino": 12.03,
    "croissant": 10.31
}

# NOUVEAUX PRIX (réalistes)
nouveaux_prix = {
    "espresso": 6.50,
    "cappuccino": 9.00,
    "latte": 10.00,
    "croissant": 4.50,
    "avocado_toast": 18.00,
    "caesar_salad": 22.00
}

print("=== COMPARAISON PRIX ===")
print(f"Espresso: {anciens_prix['espresso']} → {nouveaux_prix['espresso']} TND ({((nouveaux_prix['espresso']/anciens_prix['espresso']-1)*100):+.1f}%)")
print(f"Cappuccino: {anciens_prix['cappuccino']} → {nouveaux_prix['cappuccino']} TND ({((nouveaux_prix['cappuccino']/anciens_prix['cappuccino']-1)*100):+.1f}%)")
print(f"Croissant: {anciens_prix['croissant']} → {nouveaux_prix['croissant']} TND ({((nouveaux_prix['croissant']/anciens_prix['croissant']-1)*100):+.1f}%)")
print()

# NOUVEAU TICKET MOYEN CALCULÉ
# Répartition réaliste basée sur la nouvelle carte
repartition = {
    "boissons_chaudes": {"pct": 50, "prix_moyen": 9.5},  # Espresso à Mocha
    "boissons_froides": {"pct": 20, "prix_moyen": 12.0}, # Cold brew à Smoothie
    "food_petit_dej": {"pct": 15, "prix_moyen": 6.0},    # Croissant à Danish
    "plats_salades": {"pct": 10, "prix_moyen": 20.0},    # Sandwichs à Salades
    "desserts": {"pct": 3, "prix_moyen": 9.0},           # Cookies à Cheesecake
    "autres": {"pct": 2, "prix_moyen": 7.0}              # Thés, eaux
}

nouveau_ticket_moyen = 0
print("=== NOUVEAU TICKET MOYEN ===")
for cat, data in repartition.items():
    contribution = (data["pct"] / 100) * data["prix_moyen"]
    nouveau_ticket_moyen += contribution
    print(f"{cat.replace('_', ' ').title()}: {data['pct']}% × {data['prix_moyen']} = {contribution:.2f} TND")

print(f"\nNOUVEAU TICKET MOYEN: {nouveau_ticket_moyen:.2f} TND")
print(f"ANCIEN TICKET MOYEN: {anciens_prix['ticket_moyen']:.2f} TND")
print(f"ÉCART: {nouveau_ticket_moyen - anciens_prix['ticket_moyen']:+.2f} TND ({((nouveau_ticket_moyen/anciens_prix['ticket_moyen']-1)*100):+.1f}%)")
print()

# IMPACT SUR LE CA
clients_jour = 200
jours_an = 360

ancien_ca = clients_jour * jours_an * anciens_prix['ticket_moyen']
nouveau_ca = clients_jour * jours_an * nouveau_ticket_moyen

print("=== IMPACT SUR LE CHIFFRE D'AFFAIRES ===")
print(f"Ancien CA An1: {ancien_ca:,.0f} TND")
print(f"Nouveau CA An1: {nouveau_ca:,.0f} TND")
print(f"Écart CA: {nouveau_ca - ancien_ca:+,.0f} TND ({((nouveau_ca/ancien_ca-1)*100):+.1f}%)")
print()

# IMPACT SUR LA RENTABILITÉ
# Charges fixes restent identiques
charges_fixes = 1294767  # TND/an
marge_brute_pct = 0.656  # 65.6%

ancien_marge_brute = ancien_ca * marge_brute_pct
nouveau_marge_brute = nouveau_ca * marge_brute_pct

ancien_resultat = ancien_marge_brute - charges_fixes
nouveau_resultat = nouveau_marge_brute - charges_fixes

print("=== IMPACT SUR LA RENTABILITÉ ===")
print(f"Ancienne marge brute: {ancien_marge_brute:,.0f} TND")
print(f"Nouvelle marge brute: {nouveau_marge_brute:,.0f} TND")
print(f"Écart marge brute: {nouveau_marge_brute - ancien_marge_brute:+,.0f} TND")
print()
print(f"Ancien résultat An1: {ancien_resultat:+,.0f} TND")
print(f"Nouveau résultat An1: {nouveau_resultat:+,.0f} TND")
print(f"Écart résultat: {nouveau_resultat - ancien_resultat:+,.0f} TND")
print()

# NOUVEAU SEUIL DE RENTABILITÉ
seuil_ca = charges_fixes / marge_brute_pct
seuil_clients_jour = seuil_ca / (nouveau_ticket_moyen * 360)

print("=== NOUVEAU SEUIL DE RENTABILITÉ ===")
print(f"Seuil CA: {seuil_ca:,.0f} TND/an")
print(f"Seuil clients/jour: {seuil_clients_jour:.0f} clients/jour")
print(f"Avec {clients_jour} clients/jour prévus: {'✅ RENTABLE' if clients_jour > seuil_clients_jour else '❌ NON RENTABLE'}")

