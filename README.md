# scalable-architecture
Schoolar projet. Scalable architecture laboratory as a first usage of independent micro-services.

(French)
## Problème:
- Charge augmente
- Code source devient dure à gérer
Solution:
- Scalability:
    - Verticale (Plus de CPU, RAM, DISK, ..)
        - double le hard ne double pas la charge
        - Il y a une limite
        - Coute cher
        - Software conçu pour le hardware (Parallèle, GPU, ..)
    - Horizontale (Plus de serveur)
        - Nécessite de paralléliser les taches
        - Multithread (plusieurs thread dans un coeur), multitask (plusieurs processeur), load balancing (pls pc)
        - Mais les tâches doivent être indépendante! Besoin du résulat d'un autre tâche prose problème

## Système 3 tiers:
- Client
- Serveur
- DB

## Micro services:
- Serveur découpé en plusieurs sous programme
- Gérer par des équipes différentes
- Déployés sur des serveur physique différents
- Redondance de service fort utilisé (Load Balancing)

## Communication par API:
- Rest (GET,POST,...) sur des endpoints multiples (URL)
- GraphQL sur une seul endpoint, avec un string (genre JSON) qui contient la requête

## Sécurisation des API
- Un des services gère des "token" sous forme de string pour l'authentification
- JSON web token => le token sauve de l'information (genre nom, fonction, autorisation)
    Token signé par une clé privée donc ne peut être modifier

# Projet
Réaliser un service pour qu'ensemble former un Twitter like
Dans le langage souhaité

Plusieurs type de services:
- USER qui gère les utilisateur et fournit un token
- POST qui gère les post des utilisateur
- COMMENT qui s'occupe de la partie commentaire des POST

Utiliser Swagger pour document API
