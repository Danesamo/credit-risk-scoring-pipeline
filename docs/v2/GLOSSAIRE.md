# Glossaire V2

Les termes clés du projet, alimentés au fil de l'étude (décision D-010).
Quand un terme a plusieurs sens, on note chacun :
- **Réglementaire** : la définition officielle (BCEAO, Commission bancaire, Comité de Bâle, loi) ;
- **Académique** : le sens dans la recherche, et ce qu'il devient dans un modèle ;
- **Pratique** : ce que les professionnels entendent réellement.

Chaque définition cite sa source. Sans source, elle est marquée « à sourcer ».

---

| Terme | Définition | Sens à distinguer | Source |
|---|---|---|---|
| Défaut | Situation où un emprunteur ne respecte pas ses obligations de remboursement. **Réglementaire (banques)** : créance douteuse dès qu'une échéance est impayée depuis plus de 90 jours (180 jours pour les PME, l'État et les organismes publics), ou si le non-paiement est jugé probable (Instruction BCEAO n°026-11-2016, art. 8). **SFD** : tout l'encours est déclassé au-delà de 3 mois d'impayé. | Académique : la variable cible du modèle (0 ou 1) ; pratique : à recueillir en entretien | [R-031], [R-035], [R-039] (non vérifiées) |
| Créance en souffrance | Terme de la réglementation UEMOA : regroupe les créances restructurées et les créances douteuses ou litigieuses. | Seuil BCEAO de 180 jours d'impayés pour l'État et les PME, 90 jours pour les autres emprunteurs ; avec un seuil uniforme de 90 jours, Fitch estime le taux de l'Union à 12-14 % au lieu de 8,5 % (fin 2024) | [R-003], [R-015] (non vérifiées) ; à confirmer (axe B) |
| Taux brut de dégradation du portefeuille | Créances en souffrance brutes ÷ total des crédits bruts. Exemple : 11,1 % = sur 100 FCFA prêtés, 11,1 FCFA sont en difficulté. | À ne pas confondre avec le taux net (après provisions) | [R-003] (non vérifiée) |
| Taux de provisionnement | Provisions (argent mis de côté pour couvrir les pertes) ÷ créances en souffrance brutes. | Une baisse rend la banque plus vulnérable si les défauts augmentent | [R-003], [R-015] (non vérifiées) |
| Norme de 3 % (SFD) | Norme **de référence** employée par la BCEAO dans ses publications pour le taux brut de dégradation des microfinances. **Ce n'est pas une norme prudentielle** : elle ne figure pas parmi les 9 normes de l'Instruction n°010-08-2010, et aucune base juridique n'a été trouvée (corrigé le 08/10/2026 d'après l'axe B). | Dépassée par le secteur entier (10,2 % au 30/09/2025) ; la BCEAO utilisait 5 % en 2009 | [R-037], [R-065], [R-009] (non vérifiées) |
| Taux d'usure | Taux maximum légal d'un crédit, coût total compris. **14 % l'an pour les banques**, 24 % pour les établissements financiers et les IMF, depuis le 01/06/2026 (Décision n°19 du 29/12/2025/CM/UMOA). | Avant le 01/06/2026 : 15 % pour les banques | [R-040], [R-042] (non vérifiées) |
| TEG (taux effectif global) | Coût total annuel d'un crédit. Au Bénin, il inclut les frais et rémunérations de toute nature, hors impôts et taxes (loi n°2024-15, art. 3). | C'est lui qui est comparé au taux d'usure, pas le seul taux d'intérêt | [R-043] (non vérifiée) |
| Clientèle de détail | Particulier ou PME dont l'exposition ne dépasse pas 150 millions FCFA et 0,2 % du portefeuille de détail, ayant consenti au partage de ses données avec le bureau de crédit. Son défaut s'apprécie **par crédit**, sans contagion à ses autres crédits. | | [R-032], [R-031] (non vérifiées) |
| Compte (dans les statistiques) | Un compte ouvert, pas une somme d'argent ni une personne : une personne peut en avoir plusieurs. Les montants s'écrivent en FCFA (« Mds FCFA » = milliards). | Pour compter les personnes, utiliser le Global Findex | [R-007], [R-013] (non vérifiées) |
| PAR 30 | Portefeuille à risque à 30 jours : part de l'encours dont une échéance a plus de 30 jours de retard. | Indicateur de référence en microfinance, plus précoce que les 90 jours | À sourcer |
| PD (probabilité de défaut) | Probabilité qu'un emprunteur fasse défaut sur un horizon donné, en général 12 mois. | Une PD réglementaire doit être calibrée, ce qui n'était pas le cas en V1 | À sourcer |
| LGD (perte en cas de défaut) | Part du montant exposé qui est perdue si l'emprunteur fait défaut. | | À sourcer |
| EAD (exposition au défaut) | Montant dû au moment du défaut. | | À sourcer |
| SFD | Système financier décentralisé : terme réglementaire de l'UEMOA pour le secteur de la microfinance (loi sur les SFD). | Surveillance : ministère des Finances (au Bénin, ANSSFD) et BCEAO | [R-001] (non vérifiée) ; à sourcer (axe B) |
| IMF | Institution de microfinance : nom courant d'un établissement du secteur. En pratique, une IMF est un SFD. | Pas une tutelle ; simple appellation | [R-001] (non vérifiée) |
| IMF de grande taille | SFD dont l'encours de dépôts ou de crédits atteint au moins 2 milliards FCFA au terme de deux exercices consécutifs (Instruction n°007-06-2010, art. 2). Il est alors contrôlé directement par la BCEAO et la Commission bancaire (art. 44 de la loi SFD). | Normes prudentielles et provisionnement identiques aux autres SFD ; la nouvelle loi béninoise 2025-14 peut avoir changé ce régime (non lue) | [R-038], [R-037], [R-049] (non vérifiées) |
| Crédit digital (nano-crédit) | Petit prêt demandé, reçu et remboursé par mobile money sur le téléphone, décision en quelques secondes. Au Bénin : jusqu'à 100 000 à 150 000 FCFA, sur 7 à 30 jours. | Montages variables : opérateur + banque + prestataire technique (Prêt Xpress), banque d'opérateur (Tik Tak), fintech devenue SFD (Djamo). Pas de définition réglementaire trouvée | [R-018], [R-021], [R-023], [R-026] (non vérifiées) |
| BIC | Bureau d'information sur le crédit. | | À sourcer (axe C) |
| Scoring d'octroi | Évaluation d'un demandeur au moment où il demande un crédit, pour décider d'accorder ou non. | À distinguer du scoring comportemental (clients déjà en portefeuille) | Voir cadrage, section 3 |
| Calibration | Ajustement qui fait qu'une probabilité prédite correspond à une fréquence réellement observée. | | À sourcer |
| Test out-of-time | Évaluation d'un modèle sur une période postérieure à celle de l'entraînement. | Norme du métier, plus exigeante qu'un découpage aléatoire | À sourcer |
