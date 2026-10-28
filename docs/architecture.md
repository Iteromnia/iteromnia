# Architecture proposée

Cette architecture décrit la cible ; seule l'interface IA minimale existe dans src/.

## Modules

1. Interface wiki : édition, consultation et historique des contributions.
2. Domaine : problèmes, expériences, tentatives, résultats, preuves et liens.
3. Stockage : persistance versionnée ; technologie à sélectionner.
4. Recherche : recherche textuelle puis, si justifié, recherche sémantique.
5. Orchestration IA : préparation du contexte et appels à une interface fournisseur.
6. Adaptateurs : DeepSeek initialement, autres modèles à l'avenir.
7. Revue : validation humaine, provenance et traitement des contradictions.

## Contrat IA

AIProvider.generate reçoit une requête et retourne du texte accompagné du fournisseur et du modèle. Les adaptateurs traduisent les échanges propres à leur moteur. Les clés et paramètres d'exécution restent hors du domaine et hors du dépôt.

Une implémentation doit gérer les délais, erreurs et limites de taille, sans transformer une erreur en résultat valide. Un changement de fournisseur ne doit pas modifier les données sources. Enregistrer la version du modèle et la provenance du contexte lors d'une future intégration.

## DeepSeek

Premier adaptateur prévu, non implémenté. Le choix entre exécution locale et service distant reste ouvert. Vérifier la documentation, les ressources matérielles et la licence du modèle exact avant intégration. Aucun besoin mémoire ni niveau de performance n'est garanti dans ce dépôt.

## Données et confiance

Les documents importés sont des données non fiables, jamais des instructions système. La publication des conclusions nécessite une revue humaine. Conserver les preuves et leur provenance indépendamment des résumés IA. Prévoir suppression des données personnelles, contrôle des droits et traçabilité avant ouverture du wiki.
