---
title: 'Étude concurrentielle : question 21, outils de scoring des banques UEMOA'
type: 'competitive'
topic: "Question 21 : outils de scoring et d'aide à l'octroi des banques UEMOA"
decision: "Valeur ajoutée du projet face à l'existant (Q-09) ; préparation des entretiens"
source: 'run'
status: complete
preset: 'standard'
validation: 'normal'
red_team: 'on'
created: '2026-10-29'
updated: '2026-10-29'
claims_verified: 3
claims_unverified: 8
claims_disputed: 1
claims_overturned: 0
---

# Étude concurrentielle : question 21, outils de scoring des banques UEMOA

**Décision servie :** la valeur ajoutée du projet face à l'existant (Q-09), et des entretiens crédibles avec des professionnels du crédit.
**Question traitée :** 21 ([questions de recherche](../00_QUESTIONS_DE_RECHERCHE.md)) : quels outils de scoring ou d'aide à l'octroi les banques de l'UEMOA utilisent-elles déjà, et que leur manque-t-il ?
**Périmètre :** Bénin d'abord, puis Côte d'Ivoire et Sénégal.
**Recherche menée le :** 29/10/2026, en deux tours sur cinq volets, suivis d'une passe de contradiction et d'une vérification directe (méthode `bmad-deep-recon`, niveau standard, vérification normale, contradiction activée).

**Comment lire ce rapport**
- Chaque affirmation porte un **niveau de preuve** :
  - **prouvé** : une source le dit explicitement ;
  - **indice** : une source le suggère, ou n'a été vue qu'en extrait de moteur de recherche ;
  - **déduit** : c'est notre raisonnement.
- Les sources sont citées par leur identifiant `[R-xxx]` de la [bibliographie](../../REFERENCES.md). Aucune n'est encore vérifiée ensemble.
- Les **outils internes des banques sont rarement publics**. L'absence d'un outil dans les sources ne prouve pas que la banque n'en a pas. C'est pourquoi beaucoup de points de ce rapport deviennent des **questions d'entretien** (section 10).
- Fraîcheur : 3 mois au plus pour les offres et leurs fonctions, 6 mois pour les tendances, 12 mois pour les études et les avis. Au-delà, l'information est gardée et marquée « historique ».

---

> **Vérification du 29/10/2026, source R-121 (SCORE360).** La page Solutions a été lue directement. Elle confirme l'existence du concurrent et **renforce deux différenciations**, mais corrige un point du rapport.
> - **Segment** : SCORE360 annonce des « PME », « PME semi-formelles » et « PME sans états financiers ». **Les particuliers n'y figurent pas.** La différenciation par le segment est donc réelle.
> - **Explicabilité** : **aucune mention** d'explicabilité, d'interprétabilité ou de transparence sur tout le site lu. La différenciation par l'explication des décisions est donc réelle.
> - **Traction** : **aucun client nommé**, seulement des démonstrations proposées. La revendication « 8+ institutions » reste un indice.
> - **Correction** : le rapport décrit SCORE360 comme travaillant sur « les flux de l'institution elle-même ». La page dit en réalité « flux **PI-SPI via nos fintechs et agrégateurs partenaires** ». Le modèle n'est donc pas purement « déployé chez l'institution sur ses propres données » : il passe aussi par des partenaires d'agrégation. Point à clarifier en démonstration (QO-C2).
> - **Conséquence pour le projet** : le **PI-SPI**, plateforme interopérable de paiement instantané de la BCEAO, apparaît comme une source de flux qui ne dépend pas d'un opérateur unique. C'est une troisième voie possible pour le verrou Q-11, à instruire dans la recherche « données » (axes C et E fusionnés).

## 1. Synthèse

**Ce que les sources montrent**

1. **Les banques classiques ne publient rien sur leurs outils de scoring.** Aucune des banques étudiées ne décrit publiquement un outil de scoring statistique pour les particuliers ou les TPE : Ecobank, Société Générale, Bank of Africa, Coris, et aucune banque béninoise trouvée. Ce sont leurs communiqués, leurs notations financières, l'article Euromoney et leurs offres d'emploi qui ont été lus [R-086], [R-087], [R-088], [R-090], [R-091], [R-093] (**prouvé** pour ces documents). Seul indice contraire : un article ghanéen évoque un scoring unifié prévu par Ecobank pour l'Afrique de l'Ouest [R-147] (**indice**). Une affirmation selon laquelle Ecobank aurait un « scoring par IA » ayant ramené ses créances douteuses sous 5,5 % en 2024 [R-089] ne concorde pas avec les chiffres du groupe : environ 6,7 % fin 2024 (calcul) [R-086], 9,4 % fin 2025 [R-087] (chiffres **prouvés**, contradiction **déduite**). L'exception est **Orange Bank Africa**, une banque agréée créée par Orange et NSIA : elle accorde des prêts instantanés et son DG décrivait en 2023 un scoring en temps réel sur les données Orange et Orange Money [R-080], [R-082] (**prouvé**, en partie historique).
2. **Le crédit digital grand public est noté là où se trouve la donnée : chez l'opérateur.**
   - Au Bénin, Prêt Xpress (lancé en mars 2024, historique) associe Ecobank, qui prête, et MTN MoMo, qui distribue, avec Optasia comme partenaire [R-094] (**prouvé**). Optasia y fournit la plateforme d'IA [R-095] (**indice**). MTN détient la donnée (**déduit** : l'éligibilité exige 6 mois d'usage MoMo).
   - En Côte d'Ivoire, Bridge Microfinance prête sur des données MTN (identité du client, crédit téléphonique, usage MoMo) [R-096] (**prouvé**).
   - Optasia dit elle-même accéder aux données « par ses partenaires de distribution » [R-097], et JUMO note à partir des données d'Orange Money [R-098] (**prouvé** ; communiqué JUMO de juillet 2025, historique).
   - **La banque prête, mais ne détient ni la donnée ni le modèle** (**déduit**).
3. **Le score du bureau de crédit est la référence commune, mais il est limité.**
   - Creditinfo West Africa intègre un score de A à E à chaque rapport [R-125] (**prouvé**, source de 2020, historique) ; le scoring figure aussi parmi ses produits à valeur ajoutée [R-058].
   - Le bureau couvre **25 % des adultes**, et son taux de consultation est **estimé à 66,8 %** fin 2025 [R-004] (**prouvé** pour le chiffre). Le lire comme « un tiers des crédits accordés sans consultation » est une **déduction** : la BCEAO ne définit pas ce taux.
   - **46 % des contrats** ne sont pas mis à jour dans l'Union, **68 %** en Côte d'Ivoire [R-134] (**prouvé**, chiffres contestés par Creditinfo).
4. **Aucune solution vendue aux banques et fondée sur des relevés, des SMS ou l'agrégation de comptes fournis par le client n'a été trouvée dans l'UEMOA.** Ces solutions existent au Kenya [R-118], [R-119]. L'agrégation de comptes est un service de paiement réglementé par l'Instruction BCEAO 001-01-2024, dont les obligations s'appliquent depuis 2025 [R-111], [R-113]. Les seules traces de données fournies par l'usager sont des pilotes et des projets : scoring psychométrique de l'IFC [R-107], [R-108], essai LenddoEFL avec une IMF sénégalaise [R-110], et jeune entreprise Tontine Bénin [R-124]. Niveau : **indice** (absence constatée dans les sources lues), **à confirmer** dans le registre officiel de la BCEAO.
5. **Un concurrent direct existe pour un outil déployé chez l'institution.** **SCORE360** (Abidjan) propose aux banques, IMF et SFD des 8 pays un scoring PME fondé sur les flux de l'institution elle-même. Ses modèles sont entraînés sur place, et il revendique « 8+ institutions connectées », sans client nommé [R-121] (**prouvé** pour l'offre, **indice** pour la traction).

**Ce que cela veut dire pour Q-09 (déduit, à valider en entretien)**
- **Il y a bien un espace** : un outil de scoring d'octroi pour les **particuliers et TPE des banques classiques**. Il serait **déployé chez la banque**, sur ses données et le rapport du bureau de crédit, **explicable** et **calibré localement**. Aucun acteur ne le documente avec une référence bancaire publique.
- **Cet espace n'est pas vide**, pour trois raisons :
  - SCORE360 revendique déjà ce modèle de déploiement, pour les PME ;
  - Creditinfo propose des scores et un logiciel de décision automatisée, sans client nommé [R-126] ;
  - les opérateurs occupent déjà le petit crédit digital.
- **La piste « relevés ou historiques fournis par le client avec son consentement »** paraît libre dans l'UEMOA (indice). C'est une différenciation possible, mais une source avertit qu'un relevé ponctuel est fragile [R-136].

**Réserve majeure (passe de contradiction).** Le besoin d'inclusion est documenté, mais **l'acheteur bancaire est incertain**. Avec un taux d'usure de 14 %, une analyse estime que les banques pourraient « privilégier les profils les plus sûrs » et laisser le petit crédit aux SFD et établissements financiers, plafonnés à 24 % [R-151], [R-044] (**indice**). C'est la question à poser en priorité aux banquiers.

---

## 2. Volet C1 : outils internes des banques et de leurs groupes

| Banque ou groupe | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| **Orange Bank Africa** (Orange et NSIA ; Côte d'Ivoire, succursale au Sénégal) | Prêt instantané « Tik Tak » depuis Orange Money. Le DG déclare : « Notre capacité à prêter de l'argent aux populations non-bancarisées repose sur un outil de « scoring » qui évalue en temps réel le risque crédit », à partir des usages Orange et Orange Money. Volumes : 640 Mds FCFA prêtés depuis 2020 et 3 M de clients (février 2026). L'outil n'est pas nommé : interne ou acheté, on ne sait pas | prouvé (usage d'un scoring) ; origine de l'outil inconnue | [R-080] (2023, historique), [R-082], [R-081], [R-024] |
| | Banque à part entière : système central Temenos ; succursale sénégalaise autorisée par la Commission bancaire | indice | [R-085], [R-146], [R-084] |
| **Ecobank** (groupe ETI) | Les communiqués de résultats 2024 et des 9 premiers mois de 2026 ne mentionnent ni scoring, ni IA appliquée au crédit, ni moteur de décision. En 2026, les micro-crédits progressent surtout **hors UEMOA**, et les prêts dans l'UEMOA reculent de 3 % | prouvé (absence dans ces documents) | [R-086], [R-087] |
| | L'IA mise en avant concerne la fraude (Hawk AI), pas le crédit | prouvé | [R-088] |
| | « Scoring par IA ayant ramené les NPL sous 5,5 % en 2024 » : **ne concorde pas** avec les chiffres du groupe. Le blog qui l'affirme n'a pas pu être ouvert ; les chiffres ETI donnent environ 6,7 % fin 2024 (calcul), 9,4 % fin 2025 et 7,5 % en septembre 2026 | contesté (chiffres prouvés, contradiction déduite) | [R-089] contre [R-086], [R-087] |
| | Un article ghanéen évoque un scoring d'Ecobank Ghana et un scoring unifié prévu pour l'Afrique de l'Ouest | indice | [R-147] |
| | Prêteur de Prêt Xpress au Bénin (avec MTN et Optasia, voir volet C4). Un montage semblable avec MTN et Optasia existerait en Guinée, hors UEMOA | prouvé (Bénin, historique) ; indice (Guinée) | [R-094], [R-106] |
| **Société Générale** (Côte d'Ivoire, Bénin) | Offre de 2023 en Côte d'Ivoire (analyste risques corporate) : notation interne des entreprises et avis de crédit, sans logiciel, langage ni scoring statistique cité | prouvé ; historique | [R-091] |
| | Offres de janvier 2025 (Côte d'Ivoire, Bénin), dont un poste d'analyste risques de crédit : le détail des postes risque n'a pas été lu ; seuls des outils bureautiques sont cités, pour un autre poste | indice faible ; historique | [R-090] |
| | Une « plateforme régionale crédit » à Abidjan centraliserait l'analyse des dossiers pour plusieurs filiales | indice (offre retirée, non lue) | [R-091] |
| **Bank of Africa Bénin** | La notation financière d'août 2026 cite le « renforcement du dispositif de contrôle interne et de gestion des risques » et une hausse du coût du risque, sans outil de scoring | prouvé | [R-093] |
| **Coris Bank** | Application MyCoris (plateforme Bankerise de Proxym) : un canal digital, sans prêt instantané ni scoring documenté | indice | [R-153], [R-092] |
| **Banques béninoises** (BIIC, NSIA, Orabank, UBA, Coris) | Les partenariats avec le mobile money portent sur le paiement et l'épargne. Aucun prêt digital propre ni scoring trouvé | indice (absence de résultat, pas preuve d'absence) | [R-022] |
| **Offres d'emploi 2025-2026** | Aucune offre d'une banque de la zone citant SAS, Python, grilles de score ou apprentissage automatique pour un poste risque de crédit n'a été trouvée | absence constatée | (recherches C1) |

**Lecture (déduit).** Dans les banques classiques, l'octroi aux particuliers et aux TPE semble reposer sur l'analyse de dossier, la notation interne (surtout pour les entreprises) et le rapport du bureau de crédit. Cela concorde avec ce que l'axe B a établi : la circulaire n°04-2017/CB/C de la Commission bancaire (art. 20, lue dans une copie marquée « projet ») exige « un système approprié de notation ou de classement des crédits », sans imposer de modèle statistique [R-033]. **À confirmer en entretien.**

---

## 3. Volet C2 : éditeurs de logiciels d'octroi et de scoring

| Acteur | Offre | Présence dans la zone | Niveau | Sources |
|---|---|---|---|---|
| Éditeurs internationaux de décision crédit (Provenir, FICO, Experian, CRIF, SAS, Moody's, Oracle Origination, Mambu) | Moteurs de décision et scorecards | **Aucun client nommé dans l'UEMOA** trouvé, malgré une recherche filtrée sur leurs sites | absence constatée | (recherches C2) |
| Systèmes centraux : Sopra Banking Amplitude (NSIA Côte d'Ivoire, groupe BDK, BGFI, Orabank) ; Sopra Banking Software, produit non précisé (BMS Côte d'Ivoire, 2025) ; Temenos (Orange Bank Africa) ; Delta-Bank (Sénégal) | Système central de la banque | Clients nommés, mais **aucun module de scoring ou d'octroi** mentionné | prouvé (BMS, 2026) ; indice (les autres, historique) | [R-145], [R-140], [R-141], [R-142], [R-143], [R-144], [R-146] |
| **Creditinfo West Africa** (au-delà du bureau) | Modèles de scoring, « logiciel de gestion automatisée » des prêts permettant un traitement « sans intervention humaine », antifraude, alertes | Offre affichée, **aucun client ni prix** ; visite stratégique du groupe au Sénégal et en Côte d'Ivoire (avril 2026) | prouvé (offre) ; indice (visite) | [R-126], [R-129], [R-128] |
| **SCORE360** (Abidjan) | Scoring PME en marque blanche pour banques, IMF, SFD et fintechs ; données : flux de transactions de l'institution, données du paiement instantané BCEAO (PI-SPI) ; modèles entraînés sur place, seuls des agrégats chiffrés sortent | 8 pays de l'UEMOA revendiqués, « 8+ institutions connectées », **aucun client nommé** | prouvé (offre) ; indice (traction) | [R-121] |
| **Xloan** (Open, Inc.) | Article de positionnement sur le scoring alternatif pour le crédit et le leasing dans l'UEMOA (mobile money, crédit téléphonique, factures, réseaux sociaux) | Aucun client nommé ; accès aux données par « partenariats » non précisés | prouvé (contenu) ; indice (offre déployée) | [R-122] |
| **FABA Finance** (Abidjan, 2025) | Intermédiaire de crédit avec un score propre (« Ghost Score »), qui transmet des dossiers pré-qualifiés aux banques ; pilote en Côte d'Ivoire et au Sénégal | Aucun partenaire bancaire nommé ; **apporteur de dossiers, pas éditeur** | prouvé (description) ; déduit (positionnement) | [R-148], [R-149] |
| Logiciels pour la microfinance : Kolonell (Dakar), WEBGRAM SmartMifin (Dakar) | Logiciel d'octroi sur mesure avec grille de score à règles, de 12 à 22 M FCFA (Kolonell) ; logiciel d'IMF ouvert par API à des « outils de scoring » (WEBGRAM) | Pages commerciales, aucun client réel cité | prouvé (offre Kolonell) ; indice (WEBGRAM, Kolonell Cotonou) | [R-138], [R-139], [R-150] |
| LenddoEFL (psychométrie) | Test essayé avec des clients de CAURIE Microfinance (Sénégal) | Essai, pas un contrat ; historique | indice | [R-110] |

**Lecture (déduit).** Sur le marché bancaire de la zone, aucun éditeur international de scoring n'est installé de façon visible. L'offre la plus proche du projet vient d'acteurs régionaux : Creditinfo (bureau et décision) et SCORE360, qui revendique des institutions connectées, sans date de lancement. Faute de clients nommés, leur adoption réelle n'est pas prouvée.

---

## 4. Volet C3 : le score du bureau d'information sur le crédit

| Élément | Contenu | Niveau | Sources |
|---|---|---|---|
| Produit | **Score CIP**, lancé en 2018, classe de **A** (bons payeurs) **à E**, intégré à **chaque rapport de solvabilité**, utilisable en décision automatique ou en appui aux agents. Score de 250 à 900 selon une page produit vue en extrait | prouvé (historique) ; indice (échelle 250-900) | [R-125], [R-127] |
| Gamme | Rapports de solvabilité ; scoring, alertes, comparaisons (« benchmarking »), service par WhatsApp (HelloCreditinfo) ; données des établissements, de sources publiques et de **grands facturiers** (eau, électricité, téléphone). Grille 2025 homologuée par la BCEAO | prouvé | [R-058], [R-126] |
| Couverture | Fin 2025 : **19,7 M de clients, soit 25 % des adultes** ; 248 établissements participants sur 284 (151 établissements de crédit, 97 IMF) ; 21 grands facturiers, dont **4 au Bénin** [R-004]. Fin 2023 : 239 établissements sur 262 participaient (91,2 %) [R-133] | prouvé | [R-004], [R-133] |
| Usage | **Taux de consultation de 66,8 %** fin 2025 (45 % en 2018) : environ un tiers des crédits seraient encore accordés sans consultation (lecture, définition du taux non donnée) | prouvé (chiffre) ; déduit (lecture) | [R-004] |
| Qualité | **46,2 %** de contrats non mis à jour dans l'Union, **67,88 %** en Côte d'Ivoire (septembre 2026). Le DG de Creditinfo cite d'autres chiffres (environ 45 % contre 30 %) | prouvé (chiffres contestés) | [R-134] |
| Bénin | « Café des données » sur la qualité des données au ministère des Finances (juillet 2026), sans chiffre béninois | prouvé | [R-130] |
| Prix | Pour un particulier : gratuit une fois par an, puis 2 500 FCFA HT (1 250 FCFA par WhatsApp). **Prix pour les banques non trouvé** : les montants de la grille sont des images | indice | [R-131], [R-058] |
| Pouvoir prédictif | « Les clients bien scorés sont dix fois plus susceptibles d'être de bons payeurs », chiffre de l'opérateur sans méthode publiée. Aucune évaluation indépendante trouvée | prouvé (déclaration) ; non vérifiable | [R-132] |
| Usage réel par les agents | Au Togo, les agents de crédit des coopératives évaluent les clients **par la relation** plutôt que par le score du bureau | prouvé (Togo, 2022) | [R-135] |
| Perspectives annoncées | Score enrichi par l'IA, données alternatives pour les clients sans historique, lien avec le paiement instantané | prouvé (annonce) ; aucune réalisation datée | [R-132] |

**Lecture (déduit).** Le score du bureau est la seule brique de scoring commune à toutes les banques, et il est déjà payé avec chaque rapport. Un nouvel outil ne doit donc pas le remplacer mais **le compléter**, sur trois points : les trois quarts d'adultes absents du bureau, les données périmées et le comportement récent du client à la banque.

---

## 5. Volet C4 : scoring alternatif et détenteur de la donnée

### 5.1 Qui détient la donnée

| Fournisseur | Prêteur | **Détenteur de la donnée** | Client direct | Pays | Niveau | Sources |
|---|---|---|---|---|---|---|
| Optasia (plateforme IA) ; XtraCash possible pour l'exécution | Ecobank Bénin | **MTN Mobile Money Bénin** (ancienneté MoMo de 6 mois exigée) ; selon un extrait de la page produit, les données sont partagées avec Ecobank et d'autres partenaires | MTN (avec Ecobank) | **Bénin** | prouvé (prêteur et distributeur, 2024, historique) ; indice (rôle d'Optasia, XtraCash, partage des données) ; déduit (MTN détenteur de la donnée) | [R-094], [R-095], [R-018], [R-102], [R-103] |
| XtraCash (groupe Optasia, indice) | Bridge Microfinance S.A | **MTN Côte d'Ivoire** : « KYC, airtime usage, Mobile Money Account Usage data » ; impayés déclarés aux bureaux de crédit après 90 jours | MTN | Côte d'Ivoire | prouvé | [R-096] |
| Optasia (modèle général) | Les institutions financières, qui portent les prêts au bilan ; Optasia garantit les défauts | **Les partenaires de distribution** (« we use distribution partners to access customer data, disburse, and collect ») | Opérateurs ; certaines banques (FirstRand) | 38 pays ; Cameroun et Congo en 2025 ; **aucun pays UEMOA confirmé** dans le rapport | prouvé | [R-097] |
| JUMO | Banques panafricaines et institutions de développement non nommées | **Orange Money** (« données transactionnelles ») | Orange Money Group | Afrique francophone ; Côte d'Ivoire et Bénin cités comme marchés | prouvé (juillet 2025, historique) | [R-098], [R-152] |
| Ezra (fintech) | Orange Bank Côte d'Ivoire | Orange Money (déduit) | Groupe Orange | Côte d'Ivoire | prouvé (partenariat) ; déduit (données) | [R-099] |
| Orange Bank Africa (scoring revendiqué) | Orange Bank Africa | **Données Orange et Orange Money** ; que la banque y accède en tant que filiale du groupe est une déduction | Elle-même | Côte d'Ivoire, Sénégal | prouvé (scoring revendiqué par le DG en 2023, historique) ; déduit (accès en tant que filiale) | [R-080], [R-024] |
| Simbrella | Non identifié (Bank of Africa au Burkina Faso, selon un extrait) | Probablement l'opérateur | Non identifié | Sénégal, Bénin, Côte d'Ivoire cités | indice | [R-104], [R-105] |
| Psychométrie (IFC et Creditinfo West Africa) | IMF pilotes | **Le client** (questionnaire) et le bureau | IMF | Sénégal, Côte d'Ivoire | prouvé (projet) ; résultats non publiés | [R-107], [R-108], [R-109] |
| SCORE360 | Les banques, IMF et SFD clientes | **L'institution elle-même** (ses flux) | Institutions financières | UEMOA (revendiqué) | prouvé (offre) | [R-121] |

**Réponse à la question de positionnement (déduit).** Dans tous les montages de crédit digital vérifiés dans la zone, **l'opérateur détient les flux**. Le fournisseur de scoring travaille pour l'opérateur ou partage le risque avec lui, et la banque apporte son bilan et sa licence. Un nouvel acteur qui vendrait du scoring sur données mobile money aux banques n'aurait **pas accès à ces données** sans l'accord de l'opérateur. Il se retrouverait aussi en concurrence avec des acteurs installés : Optasia revendique 38 pays et des accords de groupe avec les grands opérateurs, dont Orange [R-097] ; JUMO s'est associé à Orange Money [R-098]. Optasia propose déjà, en Afrique du Sud, de noter les clients des banques à partir de leurs propres données de transactions [R-101] (**indice**) : un signal qu'elle pourrait aussi viser le modèle « données de la banque ». Les seules voies qui ne dépendent pas de l'opérateur passent par la donnée de la banque (comme SCORE360), le client (psychométrie, relevés) ou le bureau.

### 5.2 Données fournies par le client lui-même

| Type de solution | Dans l'UEMOA | Ailleurs en Afrique | Sources |
|---|---|---|---|
| Analyse de **relevés** (bancaires ou mobile money) exportés par le client | **Rien trouvé** | Kenya : Prembly (API d'analyse de relevés M-Pesa, avec probabilité de défaut et score), Creditinfo Kenya et Kamoa (« Boosted Score » à partir de relevés PDF M-Pesa et bancaires), SuperCrunch | [R-118], [R-119], [R-120] |
| Lecture des **SMS de transaction** | **Rien trouvé.** L'autorité ivoirienne des télécoms (ARTCI) a mis en garde en 2023 contre des applications de prêt qui accèdent aux contacts du téléphone : des pratiques intrusives existent, hors cadre | Non recherché en détail | [R-123] |
| **Agrégation de comptes** (accès consenti aux comptes) | **Encadrée** par l'Instruction BCEAO 001-01-2024, qui en fait un service de paiement réglementé, dont les obligations s'appliquent depuis 2025. **Aucun prestataire agréé pour ce service** n'a été trouvé : 11 agréments en mai 2025, puis 10 de plus en septembre 2025, pour des services de paiement (indice ; registre BCEAO non consulté). Les « agrégateurs » visibles (HoneyCoin, pawaPay, API MTN) agrègent des **paiements**, pas des données (déduit). Pas d'interfaces normalisées obligatoires (indice) | Nigeria (Mono, Okra) : non recherché faute de budget | [R-111], [R-113], [R-114], [R-115], [R-116], [R-117], [R-112] |
| Questionnaire **psychométrique** | Pilotes IFC avec Creditinfo (Sénégal, Côte d'Ivoire), sans résultats publiés (projets de 2021 et 2022, historiques) ; essai LenddoEFL avec CAURIE Microfinance (indice) | | [R-107], [R-108], [R-109], [R-110] |
| Épargne en tontine transformée en score | Tontine Bénin, fiche de jeune entreprise vue en extrait | | [R-124] |

**Réponse à la question posée par Daniela au lancement.** Dans les sources lues, **personne ne propose aux banques de l'UEMOA un scoring fondé sur des relevés ou des historiques fournis par le client**. C'est une absence constatée, donc un **indice**, **à confirmer** dans le registre officiel des agréments de la BCEAO. Les seules traces de données fournies par l'usager sont des pilotes psychométriques et une jeune entreprise de tontine. Le cadre de l'agrégation de comptes s'applique depuis 2025 [R-111], [R-113]. Ce créneau paraît donc **libre et légal** (**déduit**), sous réserve de l'agrément et du droit des données (axe B).

**Limites de ce créneau** :
- une source estime que seules des données cohérentes dans la durée sont fiables, pas un export ponctuel [R-136] ;
- les clients changent souvent de portefeuille mobile [R-136] ;
- un banquier de Bank of Africa jugeait en 2023 le scoring alternatif « très, très risqué, du moins pour nous » [R-136] (historique).

---

## 6. Volet C5 : ce qui manque, selon les sources

| Manque | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| **Clients sans historique** | Cité comme défi par le bureau de crédit et la BCEAO (rencontre de Cotonou, octobre 2025). L'IFC parle de micro et petites entreprises informelles « non scorables », faute de garanties et de données financières | prouvé (IFC : projet de 2022, historique) | [R-132], [R-108] |
| **Couverture** | Le bureau couvre 25 % des adultes | prouvé | [R-004] |
| **Qualité des données** | Contrats non mis à jour (46 % dans l'Union, 68 % en Côte d'Ivoire) ; l'AFI cite erreurs, incohérences, formats hétérogènes et instabilité des sources | prouvé | [R-134], [R-137] |
| **Explicabilité et transparence** | Selon l'AFI (enquête à laquelle la BCEAO a répondu), un « déficit de transparence » « nuit à l'interprétabilité des modèles prédictifs », et la complexité des algorithmes « crée un risque de modèle » et rend la décision « obscure ». Constat général, **non propre à l'UEMOA** ; enquête de 2023, rapport de février 2025 (historique) | prouvé (général) | [R-137] |
| **Calibration locale** | Aucune source ne l'aborde explicitement pour l'UEMOA | non trouvé ; déduit des volets C3 et C4 | |
| **Compétences** | L'IFC prévoit de former les équipes crédit, risque et informatique des institutions à l'usage des scores | indice | [R-108] |
| **Consentement et protection** | En 2023, un praticien observait que le client « n'est pas sûr de ce à quoi il a consenti ». L'usage des données non financières est une « zone grise » | prouvé (historique) | [R-136] |
| **Coût des outils** | Aucune source trouvée | non trouvé | |

---

## 7. Enseignements croisés

1. **Le marché est coupé en deux, et le projet vise la partie la moins équipée publiquement** (C1, C3 et C4).
   - Le petit crédit digital est servi par les opérateurs, avec leurs données et leurs prestataires (Optasia, JUMO), ou par une banque d'opérateur (Orange Bank Africa).
   - Le crédit bancaire classique aux particuliers et aux TPE ne documente que l'analyse de dossier et le score du bureau.

   C'est cette seconde partie que vise le projet (**déduit**).
2. **Le score du bureau est un complément obligé, pas un concurrent à éviter** (C3, axe B). Il est déjà intégré à chaque rapport [R-125], et l'axe B a établi que les banques et les SFD supervisés doivent consulter le bureau avant tout crédit (loi uniforme BIC, art. 60) [R-052]. Mais il ignore les trois quarts des adultes et repose sur des contrats souvent périmés [R-004], [R-134]. Un outil qui **intègre le score du bureau comme une variable**, et qui ajoute les données récentes de la banque, se place en complément (**déduit**).
3. **Le modèle « déployé chez la banque » est déjà revendiqué par SCORE360** (C2), et il est cohérent avec les contraintes établies par l'axe B : données et serveurs disponibles dans l'UMOA (circulaire 04-2017, art. 33) [R-033], secret bancaire et sa dérogation pour les prestataires (loi bancaire 2024-14, art. 68) [R-059]. La différence ne peut donc pas tenir au seul mode de déploiement. Elle doit porter sur le **segment** (particuliers et TPE plutôt que PME), l'**explicabilité** et la **validation transparente** (**déduit**).
4. **Les relevés et historiques fournis par le client sont la seule source alternative qu'aucune offre commerciale aux banques n'occupe dans l'UEMOA** (indice), à côté de pilotes psychométriques. C'est aussi la seule qui ne dépend ni de l'opérateur ni de la banque (C4). Elle est légale (agrégation de comptes) mais fragile : un export ponctuel, des portefeuilles multiples (**déduit**).
5. **Le manque d'explicabilité est documenté en général, pas localement** (C5). C'est un argument de différenciation plausible, en cohérence avec le droit béninois établi par l'axe B : pas de décision fondée sur le seul traitement automatisé sans possibilité pour le client de faire valoir son point de vue, et droit à la logique sous-jacente (Code du numérique, art. 401 et 437) [R-100]. Il reste à vérifier en entretien que les banquiers le ressentent (**déduit**).

---

## 8. Ce qui contredit l'idée d'un manque (passe de contradiction)

Un assistant au regard neuf a cherché ce qui contredit nos quatre conclusions, sans connaître nos preuves. **Aucune n'est contredite, toutes sont affaiblies.** Les deux concurrents qu'il a trouvés ont été vérifiés directement (digest V-1).

| Conclusion | Verdict | Argument contraire le plus fort | Sources |
|---|---|---|---|
| Les banques classiques ne documentent pas de scoring statistique | Affaiblie | Orange Bank Africa, une **banque agréée**, note en temps réel des millions de clients : la conclusion n'est vraie qu'en excluant les banques filiales d'opérateurs. L'absence de publication ne prouve pas l'absence d'outil, et Creditinfo propose déjà du scoring aux établissements assujettis (indice) | [R-082], [R-083], [R-058], [R-126] |
| Le crédit digital est noté par l'opérateur, la banque ne détient rien | Affaiblie | Chez Orange Bank Africa, le prêteur est une banque qui a accès aux données du groupe. Le modèle « banque filiale d'opérateur » peut s'étendre | [R-024], [R-085] |
| Aucune solution sur données fournies par le client | Affaiblie, puis **précisée** | SCORE360 et Xloan se positionnent sur le scoring alternatif dans l'UEMOA. Vérification : SCORE360 utilise les flux **de l'institution**, et Xloan reste flou sur ses données (son article évoque l'accès consenti aux flux mobile money et aux relevés, sans preuve de mise en œuvre). **Aucun des deux ne prouve l'usage de relevés fournis par le client.** La conclusion tient dans sa forme précise, mais le marché du scoring alternatif n'est pas vide | [R-121], [R-122] |
| Il existe un manque réel | Affaiblie **sur l'acheteur**, pas sur le besoin | Avec un taux d'usure de 14 %, une analyse estime que les banques pourraient « privilégier les profils les plus sûrs » et laisser le petit crédit aux SFD et établissements financiers (24 %). Le petit crédit digital est déjà servi par les opérateurs | [R-151], [R-044] |

**Ce que la contradiction n'a pas trouvé** :
- un client bancaire nommé dans la zone pour un éditeur international ;
- une banque classique de la zone qui note elle-même les clients mobile money ;
- une étude montrant que les outils actuels suffisent ;
- des échecs documentés de projets de scoring dans la zone (non recherchés en détail).

**Conséquence.** Les conclusions de la synthèse sont formulées avec ces restrictions : « banques classiques, hors filiales d'opérateurs », et « données **fournies par le client** » plutôt que « données alternatives ». La question de l'acheteur passe en tête des questions d'entretien.

---

## 9. Recommandations

1. **Positionner la valeur ajoutée (Q-09)** : un outil de scoring d'octroi pour les **particuliers et TPE des banques classiques**, qui **complète le score du bureau** avec les données de la banque, **déployé chez elle**, **explicable** (motifs de décision lisibles par l'analyste et le client) et **validé de façon transparente** (calibration locale, test sur une période postérieure). Confiance moyenne : le besoin est documenté, mais l'acheteur reste incertain (section 8). *Alimente : Q-09, product brief (proposition de valeur), PRD (différenciation).*
2. **Ne pas se positionner sur le scoring par données d'opérateur** : la donnée appartient à l'opérateur, et Optasia et JUMO y sont installés [R-097], [R-098]. Confiance haute pour le montage, moyenne pour la stratégie. *Alimente : Q-01, analyse des alternatives du brief.*
3. **Garder « données fournies par le client avec consentement » comme piste de différenciation à tester**, sans en faire le cœur avant les entretiens : créneau qui paraît libre (indice) et légal [R-111], mais fragile [R-136]. *Alimente : Q-02 (stratégie de données), P3.*
4. **Étudier SCORE360 et l'offre de décision de Creditinfo comme concurrents de référence** : demander des démonstrations, des références et des prix, et en parler aux banquiers. *Alimente : analyse concurrentielle du brief.*
5. **Mettre en tête des entretiens la question de l'acheteur** : une banque paierait-elle pour mieux noter les particuliers et les TPE, avec un plafond à 14 % ? Sinon, qui : IMF de l'article 44, établissements financiers ? C'est cohérent avec Q-08. *Alimente : Q-04, Q-08, guide d'entretien (P1-T4).*

---

## 10. Questions ouvertes et questions d'entretien

### 10.1 Questions ouvertes de recherche

| # | Question | Pour y répondre |
|---|---|---|
| QO-C1 | Le registre officiel de la BCEAO compte-t-il un prestataire agréé pour l'agrégation de comptes ou l'information sur les comptes ? | Liste des établissements de paiement agréés (bceao.int) |
| QO-C2 | SCORE360 a-t-il des clients réels (banques, IMF), et lesquels ? Que coûte-t-il ? | Démonstration, contact direct, presse |
| QO-C3 | Creditinfo West Africa vend-il son logiciel de décision et ses scorecards sur mesure à des banques de la zone ? À quel prix ? | Contact direct ; grille 2026 |
| QO-C4 | Les rapports annuels complets d'Ecobank 2024 et 2025 parlent-ils d'outils de décision crédit ? | Téléchargement manuel (le site bloque les robots) |
| QO-C5 | Les acteurs nigérians d'agrégation et d'analyse de relevés (Mono, Okra, Periculum, Indicina) sont-ils actifs en Afrique francophone ? | Recherche ciblée |
| QO-C6 | Quels résultats pour les pilotes psychométriques de l'IFC (Sénégal, Côte d'Ivoire) ? | Rapport de fin de projet IFC |
| QO-C7 | Prix du score du bureau pour une banque | Grille 2025 (images à lire), contact Creditinfo |

### 10.2 Questions à poser aux professionnels du crédit

Ces questions sont préparées à partir des trous de ce rapport. Elles visent ce que les documents publics ne disent pas.
1. Comment décidez-vous aujourd'hui d'accorder un crédit à un particulier ou à une TPE ? Avec quelle grille ou quel outil, interne, de groupe ou acheté ?
2. Comment utilisez-vous le score du bureau de crédit : seuil automatique, simple information, ou pas du tout ? Que pensez-vous de sa fiabilité ?
3. Que faites-vous d'un demandeur absent du bureau de crédit ?
4. Votre groupe vous fournit-il un modèle de scoring ? Est-il calibré sur votre pays ?
5. Avec un taux d'usure à 14 %, le crédit aux particuliers et aux TPE est-il une priorité ou un segment que vous réduisez ?
6. Connaissez-vous SCORE360, l'offre de décision de Creditinfo, ou d'autres outils ? Les avez-vous testés ?
7. Accepteriez-vous un outil déployé chez vous, sur vos données ? Qui doit le valider (direction des risques, groupe, Commission bancaire) ?
8. L'explication des décisions (pour l'analyste et pour le client) vous est-elle demandée, par le client, l'audit ou le régulateur ?
9. Un client qui apporterait lui-même son historique mobile money ou bancaire, avec son accord, vous intéresserait-il ?

---

## 11. Sources utilisées

Les détails (lien, date de consultation, statut de vérification) sont dans la [bibliographie](../../REFERENCES.md). Les sources ont été consultées le 29/10/2026. Les identifiants R-004, R-018, R-022, R-024, R-044 et R-058 existaient déjà ; R-033, R-052, R-059 et R-100 sont des sources de l'axe B, citées pour des règles établies par cet axe (non relues ici). **R-100 a été attribué entre-temps à une autre source** : la numérotation de cette recherche va donc de R-080 à R-099, puis de R-101 à R-153.

| ID | Ce qu'elle appuie | Éditeur | Publication | Type | Niveau principal |
|---|---|---|---|---|---|
| [R-004] | Bureau de crédit fin 2025 : participants, 25 % des adultes, consultation 66,8 %, facturiers | BCEAO | 2026-07 | primaire | prouvé |
| [R-018] | Conditions de Prêt Xpress (Bénin) | MTN Bénin | 2025-10 | primaire | indice (page en erreur) |
| [R-022] | MTN Bénin : prêts digitaux, partenariats d'épargne | Osiris (Agence Ecofin) | 2025-05 | secondaire | indice |
| [R-024] | Orange Bank Africa : Tik Tak, 500 Mds, 2 M de clients | Osiris | 2025-07 | secondaire | prouvé |
| [R-044] | Taux d'usure de 14 % et 24 % | Financial Afrik | 2026-07 | secondaire | prouvé |
| [R-058] | Grille tarifaire 2025 du bureau de crédit : produits, données, catégories d'abonnés | Creditinfo West Africa | 2024-12 | primaire | prouvé |
| [R-033] | Circulaire 04-2017/CB/C : système de notation des crédits, données dans l'UMOA (axe B) | Commission bancaire de l'UMOA | 2017-09 | primaire | prouvé (axe B, copie « projet » pour l'art. 20) |
| [R-052] | Loi uniforme BIC : consultation obligatoire avant tout crédit, art. 60 (axe B) | BCEAO | 2013-06 | primaire | lu (axe B) |
| [R-059] | Loi bancaire béninoise 2024-14 : secret bancaire et dérogation pour les prestataires, art. 68 (axe B) | République du Bénin | 2024-09 | primaire | lu (axe B) |
| [R-100] | Code du numérique, version promulguée : art. 401 et 437 (axe B) | République du Bénin | 2018 | primaire | vérifié ensemble (selon la bibliographie) |
| [R-080] | Scoring temps réel d'Orange Bank Africa (interview du DG) | Osiris | 2023-10 | secondaire | prouvé (historique) |
| [R-081] | Tik Tak, 5 ans | CIO Mag | 2025-07 | secondaire | prouvé |
| [R-082] | Orange Bank Africa : 640 Mds, 3 M de clients | Senego (Sud Quotidien) | 2026-02 | secondaire | prouvé |
| [R-083] | Orange Bank Africa : scoring et algorithmes (2020) | Osiris | 2020-07 | secondaire | indice |
| [R-084] | Succursale sénégalaise d'Orange Bank Africa | Droit Médias Finance | 2023-10 | secondaire | indice |
| [R-085] | Orange Bank Africa sur Temenos Transact | IBS Intelligence | 2020-07 | secondaire | indice |
| [R-086] | Résultats 2024 d'Ecobank : pas de scoring mentionné | Ecobank Transnational Inc. | 2025-03 | primaire | prouvé |
| [R-087] | Résultats 9 mois 2026 d'Ecobank : micro-crédits hors UEMOA, NPL | Ecobank Transnational Inc. | 2026-10 | primaire | prouvé |
| [R-088] | Euromoney 2025 : IA d'Ecobank pour la fraude | Euromoney | 2025-07 | secondaire | prouvé |
| [R-089] | Blog : « scoring par IA » d'Ecobank (contredit) | businessmodelcanvastemplate.com | inconnue | secondaire | contesté (non lu) |
| [R-090] | Offres Société Générale 2025 | yop.l-frii.com | 2025-01 | secondaire | prouvé |
| [R-091] | Offre SG Côte d'Ivoire, risques corporate | lesopportunites.com | 2023-11 | secondaire | prouvé (historique) |
| [R-092] | Coris Bank sur Lendsqr | Lendsqr | 2026-02 | secondaire | indice |
| [R-093] | Notation financière de BOA Bénin | Bloomfield (BRVM) | 2026-08 | primaire | prouvé |
| [R-094] | Lancement de Prêt Xpress au Bénin | Benin Web TV | 2024-03 | secondaire | prouvé |
| [R-095] | Optasia, micro-crédit au Bénin avec MTN et Ecobank | Optasia | inconnue | primaire | indice (403) |
| [R-096] | Conditions XtraCash, MTN Côte d'Ivoire | MTN Côte d'Ivoire | inconnue | primaire | prouvé |
| [R-097] | Optasia, résultats 2025 : modèle, données, pays | Optasia Ltd | 2026-03 | primaire | prouvé |
| [R-098] | Orange Money et JUMO | Groupe Orange | 2025-07 | primaire | prouvé |
| [R-099] | Orange Bank, Orange Money et Ezra | FinDev Gateway (CGAP) | 2025-12 | secondaire | prouvé |
| [R-101] | Optasia vers les banques (Afrique du Sud) | The Banking Brief | inconnue | secondaire | indice |
| [R-102] | XtraCash, filiale d'Optasia (MTN Ouganda) | MTN Ouganda | inconnue | primaire | indice |
| [R-103] | Page Prêt Xpress de MTN Bénin (frais, durée) | MTN Bénin | inconnue | primaire | indice (404) |
| [R-104] | Simbrella : présence au Sénégal, Bénin, Côte d'Ivoire | Simbrella | inconnue | primaire | indice |
| [R-105] | Bank of Africa et Simbrella (Burkina Faso) | AFIS | inconnue | secondaire | indice |
| [R-106] | Ecobank, MTN et Optasia en Guinée | Developing Telecoms | inconnue | secondaire | indice (404) |
| [R-107] | Pilote psychométrique IFC au Sénégal | IFC | 2021-05 | primaire | prouvé |
| [R-108] | Projet psychométrique IFC en Côte d'Ivoire | IFC | 2022-11 | primaire | prouvé |
| [R-109] | Programme IFC/FIAS : étapes des pilotes | FIAS (Groupe Banque mondiale) | inconnue | primaire | indice |
| [R-110] | Test LenddoEFL avec CAURIE Microfinance | UNCDF | inconnue | secondaire | indice |
| [R-111] | Instruction 001-01-2024 : agrégation de comptes | La Semaine Juridique (LPA-CGR) | 2025-07 | secondaire | prouvé |
| [R-112] | Pas d'open banking normalisé avant 2028-2030 | Kolonell | 2026 | secondaire | indice |
| [R-113] | Agréments de fintechs par la BCEAO (2025) | Socialnetlink | 2025-09 | secondaire | indice |
| [R-114] | 11 fintechs agréées (mai 2025) | Digital Mag CI | 2025-05 | secondaire | indice |
| [R-115] | API ouvertes MTN Mobile Money | Ericsson | 2023 | primaire | indice |
| [R-116] | Paiements mobile money dans l'UEMOA | HoneyCoin | 2026-10 | primaire | indice |
| [R-117] | Agrégateur de paiements | pawaPay | inconnue | primaire | indice |
| [R-118] | Analyse de relevés M-Pesa | Prembly | inconnue | primaire | prouvé (Kenya) |
| [R-119] | Boosted Score sur relevés PDF | Creditinfo Kenya | inconnue | primaire | prouvé (Kenya) |
| [R-120] | Score sur relevé M-Pesa | Super Systems | inconnue | primaire | indice |
| [R-121] | SCORE360 : offre, données, déploiement | SCORE360 SARL | inconnue | primaire | prouvé (offre) |
| [R-122] | Xloan : scoring alternatif dans l'UEMOA | Xloan / Open, Inc. | 2026-08 | primaire | prouvé (contenu) |
| [R-123] | Mise en garde de l'ARTCI contre des applications de prêt | Osiris | 2023-08 | secondaire | indice |
| [R-124] | Tontine Bénin | VC4A | inconnue | secondaire | indice |
| [R-125] | Score CIP : lancement, échelle A à E | Financial Afrik (tribune Creditinfo) | 2020-07 | primaire | prouvé (historique) |
| [R-126] | Produits du bureau : scoring, décision automatisée, antifraude | Creditinfo West Africa | inconnue | primaire | prouvé |
| [R-127] | Rapport de notation (score 250 à 900) | Creditinfo West Africa | inconnue | primaire | indice |
| [R-128] | Module de décision instantanée de Creditinfo | Creditinfo Group | 2018-02 | primaire | indice |
| [R-129] | Visite de Creditinfo Group au Sénégal et en Côte d'Ivoire | Creditinfo West Africa | 2026-04 | primaire | indice |
| [R-130] | Café des données au Bénin | Creditinfo West Africa | 2026-08 | primaire | prouvé |
| [R-131] | Prix du rapport pour un particulier | Creditinfo West Africa | inconnue | primaire | indice |
| [R-132] | Bilan d'une décennie du bureau de crédit (Cotonou, 2025) | Droit Médias Finance | 2025-10 | secondaire | prouvé |
| [R-133] | Bilan 2023 du bureau de crédit | Droit Médias Finance | 2024 | secondaire | prouvé |
| [R-134] | Qualité des données du bureau en Côte d'Ivoire | AllAfrica (Fraternité Matin) | 2026-09 | secondaire | prouvé |
| [R-135] | Agents de crédit et bureau au Togo | Cambridge University Press (revue *Africa*) | 2022-09 | secondaire | prouvé |
| [R-136] | Panel sur les données alternatives (consentement, risques) | AFIS | 2023-04 | secondaire | prouvé (historique) |
| [R-137] | Rapport sur les données alternatives (qualité, transparence, risque de modèle) | Alliance for Financial Inclusion | 2025-02 | primaire | prouvé |
| [R-138] | Logiciel d'octroi pour la microfinance | Kolonell | 2026-10 | primaire | prouvé (offre) |
| [R-139] | Logiciel de crédit pour IMF à Cotonou | Kolonell | 2026 | primaire | indice |
| [R-140] | NSIA Banque sur Sopra Amplitude | Four Js | 2016 | secondaire | indice |
| [R-141] | Groupe BDK et Sopra Banking | CIO Mag | inconnue | secondaire | indice |
| [R-142] | BGFI Bank sur Amplitude Up | FinTech Futures | inconnue | secondaire | indice |
| [R-143] | Orabank sur Amplitude dans 12 pays | FinTech Futures | inconnue | secondaire | indice (403) |
| [R-144] | Crédit Libanais Sénégal sur Delta-Bank | Global Custodian | inconnue | secondaire | indice |
| [R-145] | BMS Côte d'Ivoire et Sopra Banking Software | SBS | 2026-03 | primaire | prouvé |
| [R-146] | Orange Bank Africa, Temenos et NSIA | FinTech Futures | inconnue | secondaire | indice |
| [R-147] | Scoring d'Ecobank Ghana | Citi Newsroom | 2025-05 | secondaire | indice |
| [R-148] | FABA Finance et son « Ghost Score » | Agence Ivoirienne de Presse | 2026-05 | secondaire | prouvé |
| [R-149] | Guide du bureau de crédit (chiffre périmé) | FABA Finance | 2026-06 | secondaire | prouvé (écart) |
| [R-150] | Logiciel d'IMF SmartMifin | WEBGRAM | 2026-10 | primaire | indice |
| [R-151] | Usure : repli des banques sur les profils sûrs | AllAfrica (Journal de l'Économie Sénégalaise) | 2026-01 | secondaire | prouvé (analyse) |
| [R-152] | Orange Money et la technologie de JUMO | WeAreTech | inconnue | secondaire | indice |
| [R-153] | Coris Holding et Proxym (MyCoris) | Financial Afrik | 2025-11 | secondaire | indice |

---

## 12. Dates de revérification

Calculées à partir des seuils de fraîcheur : offres 3 mois, tendances 6 mois, études 12 mois.

| Affirmation clé | À revérifier le |
|---|---|
| Prêt Xpress au Bénin : Ecobank, MTN, Optasia (offre de 2024) | **déjà dépassé** |
| Rapport AFI sur les données alternatives (février 2025) | **déjà dépassé** |
| Orange Bank Africa : Tik Tak et scoring en temps réel | **déjà dépassé** (01/08/2026) |
| Optasia : modèle et pays (résultats de mars 2026) | **déjà dépassé** (01/09/2026) ; résultats semestriels 2026 à lire |
| SCORE360 : offre et traction | 01/01/2027 |
| Absence de solutions sur données fournies par le client | 01/01/2027 |
| Absence de scoring documenté chez les banques classiques | 01/01/2027 |
| XtraCash en Côte d'Ivoire | 01/01/2027 |
| Bureau de crédit : couverture et consultation | 01/01/2027 |
| Qualité des données du bureau | 01/03/2027 |

**Priorités** :
- **à revérifier en premier**, sur les sites des acteurs : les montages de crédit digital (Prêt Xpress, Tik Tak, Optasia), dont les sources dépassent déjà leur seuil de fraîcheur ;
- **avant tout positionnement final** : SCORE360, et l'absence de solutions fondées sur des données fournies par le client.

---

## 13. Termes proposés pour le glossaire

Ces termes sont à ajouter au [glossaire](../../GLOSSAIRE.md) après validation par Daniela. Le glossaire n'a pas été modifié.

| Terme | Définition proposée | Sens à distinguer | Source |
|---|---|---|---|
| Score CIP | Score du bureau de crédit de l'UEMOA (Creditinfo), classe de A (bon payeur) à E, intégré à chaque rapport de solvabilité | Score du bureau (commun à toutes les banques) contre score interne de la banque | [R-125] |
| Taux de consultation (du bureau de crédit) | Part des crédits pour lesquels le bureau a été consulté avant l'octroi (66,8 % fin 2025) | Définition exacte non publiée par la BCEAO | [R-004] |
| Grands facturiers | Sociétés d'eau, d'électricité et de télécoms qui déclarent l'historique de paiement de leurs clients au bureau de crédit | Donnée alternative déjà intégrée au bureau | [R-058], [R-004] |
| Moteur de décision (crédit) | Logiciel qui applique automatiquement un score et des règles pour accepter, refuser ou orienter une demande de crédit | À distinguer du score lui-même | [R-126] |
| Système bancaire central (core banking) | Logiciel principal d'une banque (comptes, opérations) ; n'inclut pas forcément de module de scoring | Ex. Sopra Amplitude, Temenos | [R-145] |
| Montage opérateur, banque, prestataire | Crédit digital où l'opérateur distribue et détient la donnée, la banque prête et un prestataire fournit le scoring | Ex. Prêt Xpress au Bénin | [R-094], [R-097] |
| Détenteur de la donnée | Acteur qui contrôle l'accès aux données utilisées pour noter le client (opérateur, banque, client) | Question décisive pour le positionnement | [R-097], [R-096] |
| Apprentissage fédéré | Entraînement d'un modèle sur place chez chaque institution, seuls des résultats agrégés et chiffrés étant partagés | Revendiqué par SCORE360 | [R-121] |
| Scoring psychométrique | Évaluation de la solvabilité à partir d'un questionnaire rempli par le demandeur | Donnée fournie par le client | [R-107], [R-108] |
| Agrégation de comptes | Service qui consolide, avec le consentement du client, les informations de ses comptes tenus chez plusieurs prestataires ; service de paiement réglementé dans l'UMOA | À distinguer de l'agrégation de paiements | [R-111] |
| Analyse de relevés | Extraction automatique des revenus, dépenses et remboursements à partir d'un relevé bancaire ou mobile money fourni par le client | Pratiquée au Kenya, non trouvée dans l'UEMOA | [R-118], [R-119] |
| Client sans historique (« thin file ») | Personne absente du bureau de crédit ou avec trop peu de données pour être notée | 75 % des adultes de l'UEMOA ne sont pas dans le bureau | [R-004], [R-132] |
