#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("=== RECALCUL AVEC CARTE PRODUITS OPTIMISÉE ===")
print()

# Données de base optimisées
investissement_total = 2283656  # TND
ticket_moyen_optimise = 13.09   # TND (carte optimisée)
clients_jour_prevu = 200        # clients/jour
jours_ouverture = 360           # jours/an
marge_brute = 0.70             # 70% (améliorée)

# Calcul CA annuel
clients_annuels = clients_jour_prevu * jours_ouverture
ca_annuel = clients_annuels * ticket_moyen_optimise

print(f"DONNÉES DE BASE OPTIMISÉES:")
print(f"- Investissement total: {investissement_total:,.0f} TND")
print(f"- Ticket moyen (carte optimisée): {ticket_moyen_optimise:.2f} TND")
print(f"- Clients/jour prévus: {clients_jour_prevu}")
print(f"- Marge brute améliorée: {marge_brute*100:.0f}%")
print(f"- CA annuel An1: {ca_annuel:,.0f} TND")
print()

# Coûts variables (30% du CA)
cout_matieres = ca_annuel * (1 - marge_brute)
print(f"COÛTS VARIABLES OPTIMISÉS:")
print(f"- Coût matières (30%): {cout_matieres:,.0f} TND")
print(f"- Économie vs avant: {ca_annuel * 0.02:,.0f} TND (-2 points)")
print()

# Coûts fixes (identiques)
total_personnel = 449295       # TND/an
total_immobilier = 309600      # TND/an
royalties = ca_annuel * 0.06   # 6% du CA
total_autres = 135600          # TND/an
amortissement = 228366         # TND/an

total_couts_fixes = total_personnel + total_immobilier + royalties + total_autres + amortissement

print("COÛTS FIXES (inchangés):")
print(f"- Personnel: {total_personnel:,.0f} TND")
print(f"- Immobilier: {total_immobilier:,.0f} TND")
print(f"- Royalties (6%): {royalties:,.0f} TND")
print(f"- Autres charges: {total_autres:,.0f} TND")
print(f"- Amortissements: {amortissement:,.0f} TND")
print(f"- TOTAL COÛTS FIXES: {total_couts_fixes:,.0f} TND")
print()

# Résultat d'exploitation
marge_brute_montant = ca_annuel - cout_matieres
resultat_exploitation = marge_brute_montant - total_couts_fixes

print("COMPTE DE RÉSULTAT AN1 OPTIMISÉ:")
print(f"- Chiffre d'affaires: {ca_annuel:,.0f} TND")
print(f"- Coût matières: -{cout_matieres:,.0f} TND")
print(f"- Marge brute: {marge_brute_montant:,.0f} TND ({marge_brute*100:.0f}%)")
print(f"- Coûts fixes: -{total_couts_fixes:,.0f} TND")
print(f"- Résultat d'exploitation: {resultat_exploitation:,.0f} TND")
print(f"- Marge nette: {(resultat_exploitation/ca_annuel)*100:.1f}%")
print()

# Seuil de rentabilité
marge_unitaire = ticket_moyen_optimise * marge_brute
seuil_clients_jour = total_couts_fixes / (marge_unitaire * jours_ouverture)
seuil_ca_annuel = seuil_clients_jour * ticket_moyen_optimise * jours_ouverture

print("SEUIL DE RENTABILITÉ OPTIMISÉ:")
print(f"- Marge unitaire: {marge_unitaire:.2f} TND/client")
print(f"- Seuil clients/jour: {seuil_clients_jour:.0f} clients")
print(f"- Seuil CA annuel: {seuil_ca_annuel:,.0f} TND")
print(f"- Écart vs prévision: {seuil_clients_jour - clients_jour_prevu:.0f} clients/jour")
print()

# Analyse de viabilité
if seuil_clients_jour <= clients_jour_prevu:
    print("✅ PROJET VIABLE - Seuil atteignable")
    print(f"   Marge de sécurité: {clients_jour_prevu - seuil_clients_jour:.0f} clients/jour")
else:
    print("❌ PROJET NON VIABLE - Seuil trop élevé")
    print(f"   Besoin d'augmenter le trafic de {clients_jour_prevu} à {seuil_clients_jour:.0f} clients/jour")
    print(f"   Ou augmenter le ticket moyen de {ticket_moyen_optimise:.2f} à {(total_couts_fixes/(clients_jour_prevu * marge_brute * jours_ouverture)):.2f} TND")

print()

# Comparaison avec version précédente
print("COMPARAISON AVEC CARTE EXHAUSTIVE:")
ancien_ticket = 13.36
ancien_seuil = 361
amelioration_seuil = ancien_seuil - seuil_clients_jour
print(f"- Ancien ticket moyen: {ancien_ticket:.2f} TND")
print(f"- Nouveau ticket moyen: {ticket_moyen_optimise:.2f} TND")
print(f"- Ancien seuil: {ancien_seuil} clients/jour")
print(f"- Nouveau seuil: {seuil_clients_jour:.0f} clients/jour")
print(f"- Amélioration: -{amelioration_seuil:.0f} clients/jour ({-amelioration_seuil/ancien_seuil*100:.1f}%)")

print()
print("=== FIN DU CALCUL OPTIMISÉ ===")
