#!/bin/bash

# Script d'automatisation des commits pour l'étude Espressolab
# Usage: ./auto_commit.sh "chapitre" "description"
# Exemple: ./auto_commit.sh "Chapitre 1" "Ajout section présentation franchiseur"

# Vérification des paramètres
if [ $# -lt 2 ]; then
    echo "Usage: $0 <chapitre> <description>"
    echo "Exemple: $0 'Chapitre 1' 'Ajout section présentation franchiseur'"
    exit 1
fi

CHAPITRE="$1"
DESCRIPTION="$2"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

# Message de commit standardisé
COMMIT_MESSAGE="$CHAPITRE: $DESCRIPTION - $TIMESTAMP"

echo "🔄 Préparation du commit..."
echo "📝 Message: $COMMIT_MESSAGE"

# Ajout de tous les fichiers modifiés
echo "📁 Ajout des fichiers modifiés..."
git add .

# Vérification des changements
if git diff --cached --quiet; then
    echo "⚠️  Aucun changement détecté. Abandon du commit."
    exit 0
fi

# Affichage des fichiers modifiés
echo "📋 Fichiers à commiter:"
git diff --cached --name-only

# Commit avec le message standardisé
echo "💾 Création du commit..."
git commit -m "$COMMIT_MESSAGE"

if [ $? -eq 0 ]; then
    echo "✅ Commit créé avec succès!"
    
    # Push vers la branche develop
    echo "🚀 Push vers la branche develop..."
    git push origin develop
    
    if [ $? -eq 0 ]; then
        echo "✅ Push réussi vers develop!"
        
        # Demander si on veut aussi pusher vers main
        read -p "🤔 Voulez-vous aussi pusher vers main? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "🚀 Push vers la branche main..."
            git push origin main
            if [ $? -eq 0 ]; then
                echo "✅ Push réussi vers main!"
            else
                echo "❌ Erreur lors du push vers main"
            fi
        fi
    else
        echo "❌ Erreur lors du push vers develop"
        exit 1
    fi
else
    echo "❌ Erreur lors de la création du commit"
    exit 1
fi

echo "🎉 Opération terminée avec succès!"
