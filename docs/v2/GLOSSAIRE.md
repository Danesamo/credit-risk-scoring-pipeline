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
| Défaut | Situation où un emprunteur ne respecte pas ses obligations de remboursement. | Réglementaire (seuil de retard, critères du régulateur) ; académique (la variable cible du modèle, 0 ou 1) ; pratique (ce que l'institution considère comme « mauvais payeur ») | À sourcer (axe B) |
| Créance en souffrance | Terme de la réglementation UEMOA pour les créances impayées ou douteuses. | Lien exact avec le « défaut » au sens de Bâle à établir | À sourcer (axe B) |
| PD (probabilité de défaut) | Probabilité qu'un emprunteur fasse défaut sur un horizon donné, en général 12 mois. | Une PD réglementaire doit être calibrée, ce qui n'était pas le cas en V1 | À sourcer |
| LGD (perte en cas de défaut) | Part du montant exposé qui est perdue si l'emprunteur fait défaut. | | À sourcer |
| EAD (exposition au défaut) | Montant dû au moment du défaut. | | À sourcer |
| SFD | Système financier décentralisé : nom réglementaire des institutions de microfinance dans l'UEMOA. | | À sourcer (axe A) |
| BIC | Bureau d'information sur le crédit. | | À sourcer (axe C) |
| Scoring d'octroi | Évaluation d'un demandeur au moment où il demande un crédit, pour décider d'accorder ou non. | À distinguer du scoring comportemental (clients déjà en portefeuille) | Voir cadrage, section 3 |
| Calibration | Ajustement qui fait qu'une probabilité prédite correspond à une fréquence réellement observée. | | À sourcer |
| Test out-of-time | Évaluation d'un modèle sur une période postérieure à celle de l'entraînement. | Norme du métier, plus exigeante qu'un découpage aléatoire | À sourcer |
