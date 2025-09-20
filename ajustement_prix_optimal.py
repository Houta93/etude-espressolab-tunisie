# Ajustement des prix selon recommandation Option 1 + 2

print("=== AJUSTEMENT PRIX OPTIMAL ===")
print()

# PRIX ACTUELS (trop bas)
prix_actuels = {
    "espresso": 6.50,
    "cappuccino": 9.00,
    "latte": 10.00,
    "mocha": 12.00,
    "croissant": 4.50,
    "avocado_toast": 18.00,
    "caesar_salad": 22.00
}

# PRIX AJUSTÉS (+15-20%)
prix_ajustes = {
    "espresso": 6.50,  # Garde le prix demandé
    "cappuccino": 11.00,  # +22%
    "latte": 12.00,  # +20%
    "mocha": 14.00,  # +17%
    "cold_brew": 14.00,
    "frappe": 16.00,
    "croissant": 5.00,  # +11% (reste accessible)
    "muffin": 8.00,
    "avocado_toast": 20.00,  # +11%
    "caesar_salad": 25.00,  # +14%
    "pasta": 28.00,
    "cheesecake": 13.00
}

print("=== NOUVEAUX PRIX AJUSTÉS ===")
print("BOISSONS CHAUDES:")
print(f"  Espresso: {prix_ajustes['espresso']} TND (maintenu)")
print(f"  Cappuccino: {prix_actuels['cappuccino']} → {prix_ajustes['cappuccino']} TND (+{((prix_ajustes['cappuccino']/prix_actuels['cappuccino']-1)*100):.0f}%)")
print(f"  Latte: {prix_actuels['latte']} → {prix_ajustes['latte']} TND (+{((prix_ajustes['latte']/prix_actuels['latte']-1)*100):.0f}%)")
print(f"  Mocha: {prix_actuels['mocha']} → {prix_ajustes['mocha']} TND (+{((prix_ajustes['mocha']/prix_actuels['mocha']-1)*100):.0f}%)")
print()

# NOUVEAU MIX PRODUITS (Option 1)
# Augmenter la part des plats et boissons premium
nouveau_mix = {
    "boissons_chaudes": {"pct": 45, "prix_moyen": 11.0},  # Prix moyen augmenté
    "boissons_froides": {"pct": 20, "prix_moyen": 15.0},  # Prix moyen augmenté
    "food_petit_dej": {"pct": 15, "prix_moyen": 7.0},     # Légère hausse
    "plats_salades": {"pct": 15, "prix_moyen": 24.0},     # Part augmentée 10→15%
    "desserts": {"pct": 3, "prix_moyen": 11.0},           # Prix moyen augmenté
    "autres": {"pct": 2, "prix_moyen": 8.0}               # Prix moyen augmenté
}

nouveau_ticket_moyen = 0
print("=== NOUVEAU MIX PRODUITS OPTIMISÉ ===")
for cat, data in nouveau_mix.items():
    contribution = (data["pct"] / 100) * data["prix_moyen"]
    nouveau_ticket_moyen += contribution
    print(f"{cat.replace('_', ' ').title()}: {data['pct']}% × {data['prix_moyen']} = {contribution:.2f} TND")

print(f"\nNOUVEAU TICKET MOYEN: {nouveau_ticket_moyen:.2f} TND")
print()

# IMPACT SUR LA RENTABILITÉ
clients_jour = 200
jours_an = 360
charges_fixes = 1294767
marge_brute_pct = 0.65

nouveau_ca = clients_jour * jours_an * nouveau_ticket_moyen
nouvelle_marge_brute = nouveau_ca * marge_brute_pct
nouveau_resultat = nouvelle_marge_brute - charges_fixes

print("=== IMPACT FINANCIER ===")
print(f"Nouveau CA An1: {nouveau_ca:,.0f} TND")
print(f"Nouvelle marge brute: {nouvelle_marge_brute:,.0f} TND")
print(f"Nouveau résultat An1: {nouveau_resultat:+,.0f} TND")
print()

# NOUVEAU SEUIL DE RENTABILITÉ
seuil_ca = charges_fixes / marge_brute_pct
seuil_clients_jour = seuil_ca / (nouveau_ticket_moyen * 360)

print("=== NOUVEAU SEUIL DE RENTABILITÉ ===")
print(f"Seuil CA: {seuil_ca:,.0f} TND/an")
print(f"Seuil clients/jour: {seuil_clients_jour:.0f} clients/jour")
print(f"Avec {clients_jour} clients/jour prévus: {'✅ RENTABLE' if clients_jour > seuil_clients_jour else '❌ NON RENTABLE'}")
print()

if clients_jour > seuil_clients_jour:
    print("✅ PROJET VIABLE AVEC CES AJUSTEMENTS")
else:
    clients_necessaires = int(seuil_clients_jour) + 1
    print(f"❌ BESOIN DE {clients_necessaires} clients/jour minimum")
    print(f"   Écart à combler: +{clients_necessaires - clients_jour} clients/jour")

