# Point de décision 1 : le périmètre provisoire

**Préparé le :** 22/11/2026.
**Statut :** **tranché le 22/11/2026.** Les cinq choix ont été validés par Daniela et inscrits au carnet sous les décisions D-016 à D-020.
**Prévu par :** la décision D-011, l'étude en entonnoir.

**Ce que ce point décide.** Le segment ciblé, le produit de crédit, la définition du défaut, l'utilisateur de l'outil et la voie d'accès aux données. Après lui, les recherches restantes travaillent à l'intérieur de ce cadre au lieu d'explorer tout l'écosystème.

**Ce qu'il ne décide pas.** C'est un périmètre **provisoire**. Le point de décision 2, en fin de P1, le confirmera ou le corrigera à la lumière de la recherche sur les données et de la littérature scientifique.

**Sur quoi il s'appuie.** Les axes A (marché), B (réglementation), G (pays pilote) et la question 21 (outils existants). Cinq sources portant les conclusions ont été vérifiées dans leur texte : R-006, R-009, R-031, R-100, R-121.

---

## Choix 1 : le segment de clientèle

**Option retenue proposée : les particuliers et les très petites entreprises (entreprises individuelles) des banques classiques.**

| Ce qui soutient | Ce qui fragilise |
|---|---|
| Aucune banque classique de la zone ne documente d'outil de scoring statistique pour ce segment (question 21) | **Le segment recule fortement au Bénin** : de 20,1 % à 9,0 % des crédits accordés entre 2020 et 2025, et moins 30 % sur la seule année 2025 [R-006] |
| Le besoin est massif : 8,7 % des adultes empruntent à une institution, contre 43 % à la famille [R-013] | Le marché béninois est le plus petit des trois pays étudiés : 109 Mds FCFA de nouveaux crédits aux particuliers en 2025, contre 739 et 805 |
| Le concurrent identifié couvre les PME, **pas les particuliers** [R-121 vérifiée] | Avec un taux d'usure à 14 %, les banques pourraient se replier sur les profils les plus sûrs |
| La forte concentration joue en faveur du projet : 4 banques portent 63 % du crédit au Bénin | Une banque qui se désengage n'achètera pas un outil pour mieux faire ce qu'elle abandonne |

**L'incertitude à assumer.** La question « les banques veulent-elles encore de ce segment ? » n'est pas tranchée, et aucun rapport ne la tranchera. Elle est en tête du guide d'entretien.

**Les deux lectures possibles du recul :**
- les banques se désengagent par manque de rentabilité, et l'acheteur n'est pas la banque ;
- elles s'en détournent faute de savoir évaluer ce risque, et c'est le problème que l'outil résout.

**Solution de repli, à garder en réserve.** Si le terrain confirme la première lecture, l'acheteur devient les **IMF de grande taille** (article 44), supervisées comme les banques, donc atteignables sans reconstruire l'outil. Le Bénin est le seul des trois pays où elles comptent plus de comptes que les banques.

---

## Choix 2 : le produit de crédit

**Option retenue proposée : le crédit d'un montant modeste à un particulier ou à une entreprise individuelle, accordé par une banque, avec un remboursement par échéances.**

Sont **exclus** :

| Exclu | Pourquoi |
|---|---|
| Le nano-crédit digital (7 à 30 jours, par mobile money) | Déjà automatisé par les opérateurs et leurs prestataires, dont la donnée leur appartient. De plus, sa tarification pose une question de conformité au taux d'usure qui n'est pas tranchée |
| Le crédit aux PME constituées | C'est le terrain du concurrent, et il suppose des états financiers que la cible n'a pas |
| Le crédit immobilier et l'équipement lourd | Autre horizon de risque, autres garanties, autre métier |

---

## Choix 3 : la définition du défaut

**Option retenue proposée : une échéance impayée depuis plus de 90 jours sur le crédit considéré.**

C'est la seule option qui soit à la fois réglementaire et comparable au standard international, et c'est **la seule décision du document qui repose sur une source vérifiée mot pour mot** : Instruction BCEAO n°026-11-2016, article 8 point 2, lue dans le texte officiel le 29/10/2026 [R-031].

Deux précisions issues de la même lecture :
- pour la clientèle de détail, le défaut s'apprécie **par crédit**, sans contamination des autres crédits du client (article 11) ;
- le délai de 180 jours ne concerne que les États, les organismes publics et les PME, donc pas la cible.

**Le point qui reste ouvert : les créances restructurées.** La réglementation les classe parmi les créances en souffrance. Faut-il les compter comme un défaut dans le modèle ? Cela change la variable cible. À trancher avec un professionnel, question du guide d'entretien.

**Recommandation complémentaire :** construire aussi un indicateur d'alerte à 30 jours de retard. Il ne remplace pas la cible réglementaire, il sert à détecter plus tôt.

---

## Choix 4 : l'utilisateur de l'outil

**Option retenue proposée : l'analyste crédit de la banque, qui garde la décision.**

L'outil **propose et explique**, il ne décide pas. Ce n'est pas une préférence, c'est une contrainte légale vérifiée [R-100] :
- une décision produisant des effets significatifs ne peut pas être prise sur le seul fondement d'un traitement automatisé (article 401) ;
- le client peut exiger les informations utiles sur la logique de la décision, sous 60 jours (article 437).

**Conséquences de conception, à porter dès l'architecture :**
- chaque résultat s'accompagne de motifs lisibles par l'analyste **et** par le client ;
- l'analyste peut passer outre, et son motif est enregistré ;
- la direction des risques est l'acheteur, l'analyste est l'utilisateur quotidien. Les deux doivent être convaincus, mais pas par les mêmes arguments.

---

## Choix 5 : la voie d'accès aux données

**Option retenue proposée : traiter les trois voies par ordre, sans en abandonner aucune.**

| Rang | Voie | État |
|---|---|---|
| 1 | **Les données propres de la banque**, plus le rapport du bureau de crédit | La plus sûre. Mais le bureau ne couvre que 25 % des adultes, et près de la moitié des contrats n'y sont pas à jour |
| 2 | **Les relevés apportés par le client**, avec son consentement exprès | Base légale vérifiée [R-100, article 389] et **créneau libre dans l'UEMOA** selon la question 21. C'est la différenciation possible, mais elle suppose de résoudre Q-12, l'identité |
| 3 | **Les flux du paiement instantané de la BCEAO** | Découverte du 29/10 : le concurrent y accède via des agrégateurs partenaires. Voie qui ne dépend pas d'un opérateur unique. Peu documentée |

**Écartée : la donnée des opérateurs télécoms.** Elle leur appartient, des acteurs installés l'exploitent déjà, et elle ne s'obtient pas sans partenariat.

**Ce qui doit être instruit avant le point de décision 2** par la recherche « données et accès » : la faisabilité technique de la voie 2 (comment un relevé devient une variable fiable), la question d'identité Q-12, et l'état réel de la voie 3.

---

## Ce que le projet affirme après ce point

Si les cinq choix sont retenus, la proposition du projet tient en une phrase, qui servira de base au product brief :

> **Un outil d'aide à la décision d'octroi, destiné aux analystes crédit des banques de l'UEMOA, qui évalue les particuliers et les très petites entreprises sans historique de crédit, en complétant le rapport du bureau de crédit par le comportement de paiement observé sur plusieurs mois, qui explique chacune de ses décisions, et qui se déploie chez la banque sur ses propres serveurs.**

Chaque élément de cette phrase répond à une contrainte établie, aucun n'est décoratif.

---

## Questions refermées par ce point

| Question | État après décision |
|---|---|
| Q-01, le maillon ciblé | Tranchée, sous réserve du terrain |
| Q-03, la définition du défaut | Tranchée, sauf le traitement des créances restructurées |
| Q-04, l'utilisateur | Tranchée |
| Q-09, les outils existants | Répondue par la question 21 |

## Questions qui restent ouvertes

| Question | Quand elle se tranchera |
|---|---|
| Q-08, qui paie, et le modèle économique | P2, après les premiers entretiens |
| Q-11, le verrou de l'accès aux flux | Recherche « données et accès », puis P3 |
| Q-12, la couche d'identité | Même recherche |
| Q-02, la source de données du projet lui-même | P3 |
| **L'appétit réel des banques pour ce segment** | Entretiens. C'est le risque principal du périmètre retenu |

---

## Ce qui déclencherait une révision

À surveiller pendant la suite de la P1 :

1. **Deux ou trois banquiers confirment qu'ils abandonnent le segment pour une raison de rentabilité.** Alors l'acheteur bascule vers les IMF de grande taille, et le produit se recalibre.
2. **Aucune des trois voies de données ne se révèle praticable.** Alors le projet se replie sur un démonstrateur à données synthétiques calibrées, et la question du partenariat devient prioritaire sur la technique.
3. **Un partenariat réel se présente**, avec accès à des données, dans un autre pays ou sur un autre segment. L'accès aux données prime sur le périmètre théorique.
