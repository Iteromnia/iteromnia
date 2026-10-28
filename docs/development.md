# Développement

Le squelette utilise uniquement la bibliothèque standard Python et vise Python 3.10 ou ultérieur. Il ne lance aucun modèle et ne nécessite aucune clé.

Depuis la racine du dépôt :

```sh
python3 -m compileall -q src
PYTHONPATH=src python3 -c "from iteromnia.ai import AIProvider, AIRequest, AIResponse"
```

Les adaptateurs futurs implémenteront AIProvider. Ajouter une configuration explicite du fournisseur, du modèle et du point d'accès lors de leur implémentation. Ne pas télécharger ni exécuter automatiquement un modèle lors de l'import d'un module.
