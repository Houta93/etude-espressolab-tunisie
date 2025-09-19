# Configuration GitHub - Étude Technico-Économique Espressolab Tunisie

## Paramètres du Dépôt GitHub

### Nom du Dépôt Recommandé
```
etude-espressolab-tunisie
```

### Description du Dépôt
```
Étude technico-économique pour l'implantation de la franchise Espressolab en Tunisie - 5 établissements (Tunis, Sousse, Sfax)
```

### Paramètres de Confidentialité
- **Visibilité** : **PRIVÉ** (Private Repository)
- **Accès** : Limité au propriétaire et aux collaborateurs autorisés

## Configuration du Token d'Accès Personnel (PAT)

### Permissions Requises pour le Token

Pour que je puisse travailler efficacement sur votre dépôt, le token doit avoir les permissions suivantes :

#### **Permissions Repository (Obligatoires)**
- ✅ **repo** (Full control of private repositories)
  - repo:status
  - repo_deployment
  - public_repo
  - repo:invite
  - security_events

#### **Permissions Workflow (Recommandées)**
- ✅ **workflow** (Update GitHub Action workflows)

#### **Permissions Metadata (Obligatoires)**
- ✅ **read:org** (Read org and team membership, read org projects)
- ✅ **read:user** (Read user profile data)
- ✅ **user:email** (Access user email addresses)

### Étapes de Création du Token

1. **Accéder aux Paramètres GitHub**
   - Aller sur GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)

2. **Créer un Nouveau Token**
   - Cliquer sur "Generate new token (classic)"
   - **Note** : "Etude Espressolab Tunisie - Manus AI"
   - **Expiration** : 90 jours (ou selon votre préférence)

3. **Sélectionner les Permissions**
   - Cocher toutes les permissions listées ci-dessus

4. **Générer et Copier le Token**
   - ⚠️ **Important** : Copiez immédiatement le token, il ne sera plus visible après

## Structure du Dépôt

### Arborescence Recommandée
```
etude-espressolab-tunisie/
├── README.md
├── METHODOLOGIE.md
├── SUIVI_AVANCEMENT.md
├── .gitignore
├── docs/
│   ├── architecture_etude.md
│   └── questionnaire_associe.md
├── chapitres/
│   ├── 00_resume_executif.md
│   ├── 01_introduction_generale.md
│   ├── 02_presentation_projet_franchiseur.md
│   ├── 03_etude_marche_tunisie.md
│   ├── 04_strategie_marketing_commerciale.md
│   ├── 05_etude_technique_operationnelle.md
│   ├── 06_organisation_ressources_humaines.md
│   ├── 07_etude_financiere_previsionnelle.md
│   ├── 08_analyse_risques_opportunites.md
│   └── 09_conclusion_generale.md
├── annexes/
│   ├── A_documents_juridiques/
│   ├── B_devis_factures/
│   ├── C_cv_porteur_projet/
│   ├── D_donnees_excel/
│   │   ├── EspressoLab.xlsx
│   │   ├── INVESTMENTCOST.xlsx
│   │   └── analyse_donnees.md
│   └── E_sources_references/
│       ├── sources_bibliographie.md
│       └── liens_utiles.md
├── assets/
│   ├── images/
│   ├── graphiques/
│   └── tableaux/
├── scripts/
│   ├── auto_commit.sh
│   └── generate_pdf.sh
└── temp/
    ├── recherches_en_cours/
    └── notes_temporaires/
```

## Système de Documentation des Sources

### Format des Références en Exposant
Dans les chapitres, utiliser le format suivant :
```markdown
Le PIB de la Tunisie s'élève à 47,6 milliards USD¹.

La consommation de café en Tunisie représente 2,1 kg par habitant et par an².
```

### Fichier de Références (annexes/E_sources_references/sources_bibliographie.md)
```markdown
# Sources et Références Bibliographiques

## Sources Officielles

### 1. Banque Mondiale
**URL** : https://data.worldbank.org/country/tunisia
**Date de consultation** : [Date]
**Données utilisées** : PIB, indicateurs économiques
**Fiabilité** : ⭐⭐⭐⭐⭐ (Source officielle internationale)

### 2. Institut National de la Statistique (INS) Tunisie
**URL** : http://www.ins.tn/
**Date de consultation** : [Date]
**Données utilisées** : Démographie, consommation
**Fiabilité** : ⭐⭐⭐⭐⭐ (Source officielle nationale)
```

## Workflow de Travail

### Branches Recommandées
- **main** : Version finale et validée
- **develop** : Travail en cours
- **feature/chapitre-X** : Branches spécifiques par chapitre

### Commits Automatisés
Un script sera créé pour automatiser les commits avec des messages standardisés :
```bash
#!/bin/bash
# auto_commit.sh
git add .
git commit -m "Chapitre $1: $2 - $(date '+%Y-%m-%d %H:%M')"
git push origin develop
```

## Sécurité et Bonnes Pratiques

### Fichiers à Exclure (.gitignore)
```
# Fichiers temporaires
*.tmp
*.temp
~$*

# Fichiers système
.DS_Store
Thumbs.db

# Données sensibles
*.env
config/secrets.json

# Fichiers de travail
temp/notes_personnelles/
```

### Sauvegarde et Versioning
- **Commits fréquents** : Après chaque section terminée
- **Messages explicites** : "Chapitre 2: Ajout analyse concurrentielle"
- **Tags de version** : v1.0-draft, v1.1-revision, v2.0-final

## Prochaines Étapes

1. **Créer le dépôt** avec le nom recommandé
2. **Générer le token** avec les permissions listées
3. **Me fournir le token** pour initialiser la structure
4. **Commencer le travail** chapitre par chapitre

Une fois le token fourni, je pourrai :
- Initialiser la structure complète du dépôt
- Créer tous les fichiers de base
- Mettre en place les scripts d'automatisation
- Commencer la rédaction du premier chapitre
