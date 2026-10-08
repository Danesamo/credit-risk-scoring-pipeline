---
name: cloture-session
description: Clôture d'une session de travail sur la V2 du projet de scoring crédit : repère tout ce qui s'est passé, détermine quel document de docs/v2 mettre à jour grâce à la table de routage, fait valider la liste par Daniela, applique, contrôle la cohérence et donne la commande de commit. À utiliser quand Daniela tape /cloture-session, dit « on clôture », « fin de session », ou demande de mettre les documents à jour.
---

# Clôture de session : V2 scoring crédit UEMOA

Objectif : qu'aucune information utile de la session ne se perde, sans alourdir les documents. Daniela valide avant toute écriture et exécute elle-même les commandes Git.

## Étape 1 : faire l'inventaire de la session

1. Relire la conversation depuis la dernière clôture : décisions, tâches avancées, idées, contacts, sources, termes, erreurs découvertes.
2. Lire l'état actuel : `docs/v2/00_FICHE_SUIVI.md` (en-tête, tâches, questions ouvertes, dernier journal), les dernières entrées de `docs/v2/CARNET.md`, le tableau « Suivi des axes » du fichier `00_QUESTIONS_DE_RECHERCHE.md` de l'initiative active.
3. Repérer le travail du chat atelier : `git status` et `git log` depuis le dernier commit, nouveaux fichiers dans `docs/v2/initiative-*/`, nouvelles lignes dans `docs/v2/REFERENCES.md`.

## Étape 2 : router chaque information vers son document

| Quand il se passe ceci... | ...on met à jour |
|---|---|
| Une tâche avance ou se termine, une phase change | `00_FICHE_SUIVI.md` : tâches, statut des phases, en-tête « phase en cours / prochaine action », date de mise à jour |
| La session se termine | `00_FICHE_SUIVI.md`, journal des sessions : 3 lignes maximum, des liens plutôt que des répétitions |
| Une question reste sans réponse | `00_FICHE_SUIVI.md`, questions ouvertes (Q-xx) |
| Un contact, une piste de données ou un partenaire apparaît | `00_FICHE_SUIVI.md`, contacts et pistes |
| Une décision est prise ou révisée | `CARNET.md` : nouvelle entrée D-xxx (date, décision, pourquoi, alternatives écartées, statut). Une décision révisée n'est jamais effacée : on ajoute une entrée et on passe l'ancienne à « Remplacée par D-xxx » |
| La vision, les objectifs ou les contraintes de Daniela évoluent | `01_CADRAGE_INITIAL.md` |
| Une erreur est découverte dans l'analyse de la V1 | `02_DIAGNOSTIC_V1.md` |
| Un terme clé apparaît ou se précise | `GLOSSAIRE.md` (sens réglementaire, académique, pratique ; source) |
| Une source est utilisée ou vérifiée | `REFERENCES.md` : R-xxx, type, date de consultation, archive, colonne « Vérifié » |
| Une question de recherche est ajoutée, un axe avance | `00_QUESTIONS_DE_RECHERCHE.md` de l'initiative : « Questions ajoutées en cours de route », « Suivi des axes » |
| Un document est créé, déplacé ou supprimé | `docs/v2/README.md` : index et arborescence uniquement |

## Étape 3 : filtrer

Pour chaque ligne envisagée : « servira-t-elle de repère dans 3 mois ? » Sinon, ne pas l'écrire.
Jamais dans les documents : le débogage, les incidents d'environnement (permissions, mots de passe, installations), les petites corrections.

## Étape 4 : faire valider

Présenter à Daniela la liste des mises à jour, regroupée par document, une ligne par modification. Attendre sa validation ou ses corrections. Ne rien écrire avant.

## Étape 5 : appliquer et contrôler

Appliquer les modifications validées, puis vérifier :
- les identifiants se suivent sans doublon (D-xxx, R-xxx, Q-xx, P1-Tx) ;
- toutes les dates sont absolues (jj/mm/aaaa) ;
- aucun tiret cadratin (`grep -rn "—" docs/v2` doit être vide) ;
- les liens internes pointent vers des fichiers existants ;
- l'index du README correspond aux fichiers réellement présents ;
- aucune source non vérifiée ne fonde une décision du carnet.

## Étape 6 : commit

Donner à Daniela la commande à exécuter elle-même, avec un message de commit court et descriptif, sans ligne Co-Authored-By :

```bash
cd ~/projects/Credit_Risk_Scoring_Project
git add docs/ .claude/
git status
git commit -m "<message>"
git push
```

Terminer par un récapitulatif de deux lignes : ce qui a été mis à jour, et la prochaine action.
