# Correction des prix pour cohérence avec ticket moyen 22,28 TND

print("=== ANALYSE DES PRIX COHÉRENTS ===")
print()

# Données de base
ticket_moyen = 22.28
ca_an1 = 1604160
clients_jour = 200
jours_an = 360

print(f"Ticket moyen cible: {ticket_moyen} TND")
print(f"CA An1: {ca_an1:,} TND")
print(f"Clients/jour: {clients_jour}")
print()

# Répartition par catégorie (plus réaliste)
categories = {
    "Boissons Chaudes": {"pct": 50, "prix_moyen": 8.5},
    "Boissons Froides": {"pct": 20, "prix_moyen": 12.0},
    "Food Petit Déj": {"pct": 15, "prix_moyen": 15.0},
    "Plats & Salades": {"pct": 10, "prix_moyen": 25.0},
    "Desserts": {"pct": 3, "prix_moyen": 18.0},
    "Snacks": {"pct": 2, "prix_moyen": 12.0}
}

print("=== PRIX COHÉRENTS PAR CATÉGORIE ===")
ticket_calcule = 0
for cat, data in categories.items():
    contribution = (data["pct"] / 100) * data["prix_moyen"]
    ticket_calcule += contribution
    print(f"{cat}: {data['pct']}% × {data['prix_moyen']} TND = {contribution:.2f} TND")

print(f"\nTicket moyen calculé: {ticket_calcule:.2f} TND")
print(f"Écart avec cible: {abs(ticket_calcule - ticket_moyen):.2f} TND")

print("\n=== GRILLE TARIFAIRE RÉALISTE ===")
print("\n** BOISSONS CHAUDES **")
print("Espresso: 6,50 TND (votre prix initial)")
print("Cappuccino: 8,50 TND")
print("Latte: 9,50 TND")
print("Mocha: 11,00 TND")

print("\n** BOISSONS FROIDES **")
print("Cold Brew: 10,00 TND")
print("Frappé: 12,00 TND")
print("Smoothie: 15,00 TND")

print("\n** FOOD PETIT DÉJEUNER **")
print("Croissant: 4,50 TND (vs 10,31 TND incohérent)")
print("Pain au chocolat: 5,00 TND")
print("Muffin: 6,50 TND")
print("Avocado Toast: 18,00 TND")

print("\n** PLATS & SALADES **")
print("Salade César: 22,00 TND")
print("Buddha Bowl: 28,00 TND")
print("Sandwich Club: 16,00 TND")

