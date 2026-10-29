# Brief de recherche : question 21, outils de scoring existants

**Approuvé le :** 29/10/2026 par Daniela
**Décision visée :** la valeur ajoutée du projet face à l'existant (Q-09) ; préparer des entretiens crédibles avec des professionnels du crédit.
**Type :** competitive · **Forme :** exploration · **Topologie :** en largeur
**Périmètre :** banques de l'UEMOA ; Bénin d'abord, puis Côte d'Ivoire et Sénégal.

## Volets

| Volet | Contenu |
|---|---|
| C1 | Outils internes des banques et de leurs groupes (Ecobank, Société Générale, Bank of Africa, Coris, NSIA, BIIC, Orange Bank Africa…) ; indices : rapports annuels, communiqués, études de cas, offres d'emploi en risque de crédit et data science |
| C2 | Éditeurs de logiciels d'octroi et de scoring présents dans l'UEMOA (clients cités, fonctions, positionnement) |
| C3 | Scores du bureau d'information sur le crédit (Creditinfo West Africa) : contenu, adoption, limites |
| C4 | Scoring alternatif proposé aux banques. Pour chaque fournisseur : montage et **détenteur de la donnée** (vente directe aux banques, ou partenariat avec un opérateur propriétaire des flux). Existence de solutions fondées sur des **données fournies par le client avec son consentement** (import de relevé, lecture de SMS de transaction, export mobile money, agrégation de comptes) ; si aucune, le dire |
| C5 | Ce qui manque selon les sources : clients sans historique, explicabilité, calibration locale, données |

## Règles

- Trois niveaux de preuve : **prouvé** (une source le dit explicitement), **indice** (offre d'emploi, étude de cas qui le suggère), **déduit** (raisonnement).
- Sources primaires d'abord : banques, éditeurs, institutions (Banque mondiale, IFC, GSMA, CGAP).
- Deux sources pour les affirmations d'adoption et pour toute capacité sur laquelle repose notre différenciation.
- Fraîcheur : offres et fonctions ≤ 3 mois, tendances ≤ 6 mois, avis d'utilisateurs ≤ 12 mois ; au-delà, « historique ».

## Réglages

Standard : 3 assistants (C1 ; C2+C3 ; C4+C5), 8 sources par volet et par tour, 2 tours au plus. Vérification normal. Red team activé : recherche de ce qui contredit l'idée d'un manque.

## Sorties

- Rapport `research-q21-outils-de-scoring-uemoa.md`, citations `R-xxx` à partir de R-080.
- Sources ajoutées à `docs/v2/REFERENCES.md` (Consulté le renseigné, Archive vide, Vérifié = non).
- Termes proposés pour le glossaire en fin de rapport, sans modifier le glossaire.
