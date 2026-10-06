# P1 : Questions de recherche de l'étude de contexte

**Rédigé le :** 05/10/2026
**Statut :** Validé par Daniela le 06/10/2026 comme base de départ, évolutive (voir section « Questions ajoutées en cours de route »)
**Périmètre :** cadre UEMOA, comparaison Côte d'Ivoire et Sénégal, terrain Bénin (décision D-009)

Chaque question doit déboucher sur une décision du projet. Une question sans décision associée n'a pas sa place dans l'étude.

---

## Règles de l'étude

1. **Sources primaires d'abord** : textes BCEAO et Commission bancaire, lois, rapports officiels, articles scientifiques, chiffres publiés par les acteurs eux-mêmes.
2. **Chaque chiffre est sourcé et daté.** Sans source fiable, il est marqué « à vérifier ».
3. **Un axe à la fois**, mené dans le chat atelier avec `bmad-deep-recon`. Chaque axe produit un rapport dans ce dossier (`research-<axe>/`).
4. **Le terrain confirme ou contredit** : réponses au post LinkedIn du 06/10/2026, entretiens avec des professionnels du crédit.
5. **Chaque source est référencée dans la [bibliographie](../REFERENCES.md)** avec un identifiant `R-xxx`, que les rapports citent. Chaque source est vérifiée ensemble avant de fonder une décision (décision D-012).
6. **Chaque terme clé rencontré alimente le [glossaire](../GLOSSAIRE.md)**, avec sa définition réglementaire, académique et pratique quand elles diffèrent (décision D-010).

## Ordre des axes et points de décision (décision D-011)

L'étude fonctionne en entonnoir : on ne répond pas aux 20 questions avant de circonscrire le projet.

1. **Axes A, B et G** (marché, réglementation, pays pilote) : vue d'ensemble.
2. **Point de décision 1 : périmètre provisoire.** Segment ciblé (Q-01), type de crédit, définition du défaut (Q-03), utilisateur (Q-04). Consigné dans le carnet.
3. **Axes E, F, C, D**, menés uniquement à l'intérieur de ce périmètre provisoire.
4. **Point de décision 2 : périmètre définitif**, en entrée de la P2 (product brief).

## Guide d'entretien terrain

Les questions de recherche ne sont pas posées telles quelles aux professionnels : on ne leur demande pas ce qu'on peut lire dans un rapport. Un guide d'entretien sera rédigé après les axes A et B (P1-T4), pour poser des questions informées, surtout sur les axes D et C.

---

## A. Le marché du crédit : qui prête à qui ?
*Décision visée : le maillon de l'écosystème à cibler (Q-01).*

1. Quels acteurs font du crédit aux particuliers et aux très petites entreprises (banques, microfinances, opérateurs de mobile money, fintechs), et quels partenariats existent entre eux (nano-crédit banque et opérateur) ?
2. Où en est l'inclusion financière (compte, mobile money, crédit), et avec quels écarts entre Bénin, Côte d'Ivoire et Sénégal ?
3. Quels produits de crédit existent, avec quels montants, durées et taux ?
4. Quel est le niveau des créances en souffrance des banques et des microfinances, et quelles en sont les causes ?

## B. Le cadre réglementaire
*Décisions visées : la définition du défaut (Q-03), le cadre légal du produit (Q-06).*

5. Comment la BCEAO et la Commission bancaire définissent-elles une créance en souffrance, et quelles règles de classement et de provisionnement s'appliquent ?
6. Quel taux maximum (taux d'usure) encadre le crédit ?
7. Que prévoient les textes sur les bureaux d'information sur le crédit : couverture, obligation de consultation, consentement du client ?
8. Quelles règles de protection des données (Bénin, UEMOA) encadrent l'usage de données alternatives (mobile money, télécom) et les décisions automatisées ?
9. Quelles exigences de Bâle II et III, appliquées dans l'UEMOA, concernent les modèles de risque des banques ?

## C. L'infrastructure de données du crédit
*Décisions visées : les données mobilisables, les variables possibles.*

10. Que contient le bureau de crédit régional, qui y accède, et quelle part de la population couvre-t-il ?
11. Où en sont le mobile money et l'interopérabilité des paiements, et ces données sont-elles accessibles avec le consentement du client ?
12. Quel rôle joue l'identité numérique (au Bénin, le numéro personnel d'identification) dans l'accès au crédit ?

## D. Les réalités des emprunteurs
*Décisions visées : l'utilisateur de l'outil (Q-04), les variables à construire.*

13. Quels sont les profils types d'emprunteurs (salariés, informels, agriculteurs, commerçants), avec leurs revenus irréguliers, leur saisonnalité et leur pluriactivité ?
14. Pourquoi les gens n'empruntent-ils pas, et pourquoi font-ils défaut (chocs, surendettement, emprunts multiples) ? Quel rôle jouent les tontines et les garanties sociales ?
15. Comment un analyste crédit évalue-t-il un dossier aujourd'hui, et qu'est-ce qui lui manque ?

## E. Les données disponibles pour le projet
*Décision visée : la stratégie de données (Q-02).*

16. Quels jeux de données publics existent (BCEAO, Findex, FinScope, compétitions Zindi, enquêtes ménages), quelles données synthétiques pourrait-on calibrer, et quels partenaires pourraient fournir des données réelles ?

## F. Les solutions existantes et la valeur ajoutée
*Décision visée : le positionnement et la valeur ajoutée du projet.*

17. Quelles solutions de scoring alternatif sont déployées en Afrique (UEMOA et ailleurs) ? Qu'est-ce qui a marché, qu'est-ce qui a échoué, quelles dérives ont été observées (surendettement lié au crédit digital) ?
18. Que dit la recherche académique : scoring sur données mobiles, équité, explicabilité, démarrage avec peu de données ?
19. Quels besoins restent non couverts ?

## G. Le choix du pays pilote
*Décision visée : confirmer ou réviser le Bénin comme pilote (D-009).*

20. Comment le Bénin, la Côte d'Ivoire et le Sénégal se comparent-ils en données disponibles, en accès au terrain et en taille de marché ?

---

## Questions ajoutées en cours de route

| # | Question | Ajoutée le | Origine | Axe |
|---|---|---|---|---|
| | *(aucune pour l'instant)* | | | |

---

## Suivi des axes

| Axe | Type de recherche (`bmad-deep-recon`) | Statut | Rapport |
|---|---|---|---|
| A. Marché | market | ⬜ À faire | |
| B. Réglementation | domain | ⬜ À faire | |
| G. Pays pilote | choix entre candidats | ⬜ À faire | |
| **Point de décision 1 : périmètre provisoire** | | ⬜ À faire | Carnet |
| E. Données disponibles | technical | ⬜ À faire | |
| F. Solutions existantes | competitive + academic-lit | ⬜ À faire | |
| C. Infrastructure de données | domain | ⬜ À faire | |
| D. Emprunteurs | user-voice + terrain | ⬜ À faire | |
| **Point de décision 2 : périmètre définitif** | | ⬜ À faire | Synthèse générale, réponses à Q-01 à Q-06 |
