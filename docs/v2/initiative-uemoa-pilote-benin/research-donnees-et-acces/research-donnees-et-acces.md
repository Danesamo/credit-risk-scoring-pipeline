---
title: 'Étude technique : données et accès (axes C et E)'
type: 'technical'
topic: 'Données et accès (axes C et E fusionnés)'
decision: "Faisabilité des trois voies d'accès aux données de D-020 (Q-11, Q-12, Q-02)"
source: 'run'
status: complete
preset: 'standard'
validation: 'high'
red_team: 'on'
created: '2026-11-22'
updated: '2026-11-22'
claims_verified: 6
claims_unverified: 8
claims_disputed: 1
claims_overturned: 0
---

# Étude technique : données et accès (axes C et E fusionnés)

**Décision servie :** la faisabilité réelle des trois voies d'accès aux données retenues par la décision D-020, en entrée du point de décision 2. Si aucune voie n'était praticable, le périmètre du point de décision 1 devrait être revu.
**Questions traitées :** Q-11 (le verrou de l'accès aux flux), Q-12 (la couche d'identité), Q-02 (les données du projet lui-même), et le volet technique de la question 22.
**Recherche menée le :** 22/11/2026, en deux tours sur cinq volets, suivis d'une contre-vérification indépendante et d'une passe de contradiction ciblée sur la voie 2 (méthode `bmad-deep-recon`, niveau standard, vérification « high »).

**Comment lire ce rapport**
- Chaque affirmation porte un **niveau de preuve** :
  - **prouvé** : lu dans une source pendant la recherche ;
  - **indice** : suggéré, ou vu seulement en extrait de moteur de recherche ;
  - **déduit** : c'est notre raisonnement.
- **Vérification « high »** : une affirmation qui fonde la faisabilité d'une voie doit être confirmée par **deux sources indépendantes**. Celles qui n'en ont qu'une sont marquées **« à source unique »** et ne fondent pas de conclusion seules.
- Les sources sont citées par leur identifiant `[R-xxx]` de la [bibliographie](../../REFERENCES.md). Aucune n'est encore vérifiée ensemble.
- **Ce que le web ne peut pas établir**, Daniela peut le constater elle-même en quelques minutes. C'est l'objet de la **section 10, « Tests à faire soi-même »**, qui est un livrable de ce rapport.

---

> # Résultat des tests terrain, 23/11/2026
>
> Tests T1, T2 et T3 exécutés sur un compte MTN MoMo réel au Bénin. **Ils infirment la conclusion principale du rapport : la voie 2a est techniquement praticable.** Seuls les constats de structure sont consignés ici. Aucune donnée personnelle, aucun montant, aucun nom de tiers n'est conservé dans le projet.
>
> **T1, l'export existe.** Dans l'application MoMo, écran « Relevés », bouton « Obtenir relevés ». L'utilisateur choisit une plage par bouton (7, 30 ou 90 jours) ou par deux champs de dates libres. Le relevé est produit en **PDF**, partageable immédiatement (messagerie, courriel). Aucun coût ni délai constaté. **Profondeur maximale établie le 23/11/2026 : 90 jours, et pas davantage.** Les champs de dates libres n'ouvrent pas au-delà, les dates antérieures étant grisées dans le sélecteur. Un relevé de 90 jours produit le même format, simplement plus long. **C'est la limite structurante de la voie 2a : un client ne peut fournir que les trois derniers mois de son activité.**
>
> **T2, le relevé identifie le titulaire et porte les champs utiles.** En-tête : titulaire du compte, numéro de portefeuille, niveau de profil de l'abonné, dates de début et de fin, durée, solde disponible. Chaque opération porte **neuf champs** : date et heure, type de paiement, numéro de la contrepartie, nom du compte de la contrepartie, montant signé, identifiant de transaction, frais, **solde après opération**, référence. Le solde après chaque opération et le sens du flux sont présents : ce sont les deux éléments décisifs pour reconstituer un comportement de paiement.
>
> **T3, le PDF est lisible par une machine.** Le texte est sélectionnable et extractible, donc exploitable sans reconnaissance de caractères. **Aucune signature électronique, aucun code QR et aucun numéro de référence du relevé n'ont été constatés**, ce qui laisse entière la question de la falsification relevée par la passe de contradiction.
>
> **Deux découvertes non prévues par les tests.**
> 1. **L'écran « Relevés » affiche des agrégats mensuels calculés par l'opérateur** : argent entrant, argent sortant et solde sur le mois courant. C'est exactement le type de signal recherché, déjà agrégé à la source.
> 2. **Le service PI-SPI apparaît comme une fonction accessible à l'utilisateur** depuis l'accueil de l'application. Cela nuance la conclusion du volet D3, qui jugeait le PI-SPI réservé aux entreprises clientes d'un participant. À instruire.
>
> **Un risque nouveau, à traiter en P2 et P4.** Le relevé contient les **noms des contreparties**, donc des données personnelles de tiers qui n'ont jamais consenti à ce traitement. Un client qui transmet son relevé à sa banque transmet aussi l'identité de toutes les personnes avec qui il a échangé. Au regard du Code du numérique, cela impose au minimum une minimisation (ne conserver que ce qui sert au scoring) et interdit de conserver les noms des tiers.

## 1. Synthèse

### Verdict par voie

| Voie (D-020) | Verdict au 22/11/2026 | Ce qui le fonde | Ce qui le ferait basculer |
|---|---|---|---|
| **1. Données de la banque et bureau de crédit** | **Praticable** pour les clients que la banque connaît déjà ; utilité limitée pour les clients sans historique | La banque déclare ses crédits chaque mois à la BCEAO [R-163] et le rapport du bureau détaille contrats, échéances, impayés et un score [R-154], [R-160] (**prouvé**, deux sources). La transmission à un prestataire est encadrée par la loi bancaire et la sous-traitance (axe B) [R-059], [R-033] | La couverture du bureau (25 % des adultes [R-004]) et la profondeur réelle du rapport, à constater sur un vrai rapport (test T8) |
| **2. Relevés apportés par le client** | **Non établie : tout dépend des tests de la section 10.** Deux chemins, aucun démontré | **(2a) Export par le client** : aucune source publique ne montre d'export d'historique depuis MTN MoMo, Moov Money ou Celtiis Cash [R-176], [R-177] (**indice** : absence constatée). **(2b) Agrégation de comptes réglementée** : le texte existe, avec enregistrement de l'agrégateur [R-048], [R-174] (**prouvé**, deux sources) et interface obligatoire sans contrat [R-048] (**à source unique**). Mais aucun agrégateur enregistré, aucune interface ouverte et aucune norme technique n'ont été trouvés | **Positif** : un export de plusieurs mois, lisible par une machine et portant le nom du titulaire (tests T1 à T4). **Négatif** : un historique court et non exportable, ou le refus de la BCEAO d'appliquer l'article 60 aux portefeuilles de monnaie électronique |
| **3. Flux du paiement instantané (PI-SPI)** | **Impraticable en l'état pour les particuliers** ; possible seulement pour une TPE cliente d'un participant | L'« API Business » d'un participant sert à l'**entreprise cliente** pour payer, encaisser et suivre ses propres transactions ; au Bénin, une seule est homologuée (Ecobank) [R-170], [R-205] (**prouvé**, deux sources). Qu'un prestataire de scoring ne puisse pas lire les flux des particuliers est **déduit** : aucun règlement de participation n'a été lu | La publication d'un service d'accès consenti aux comptes adossé au PI-SPI (non trouvé) |

### Réponses aux trois questions

- **Q-11, le verrou des flux mobile money** : il **n'est pas levé**.
  - L'opérateur ne publie pas d'accès à l'historique d'un client pour un tiers. Le portail des développeurs MoMo propose l'encaissement, le décaissement et les transferts, mais pas de lecture d'historique [R-189]. Une question posée en mars 2026 sur le forum du groupe MTN (section Ouganda), sur une API d'historique lisible avec le consentement du client, est restée sans réponse [R-187] (**indice** : absence constatée, non prouvée).
  - Les deux seules issues sont le **relevé exporté par le client lui-même**, à tester (T1 à T7), et l'**agrégation de comptes** prévue par l'Instruction BCEAO 001-01-2024, qui existe sur le papier mais n'a pas été vue en fonctionnement.
- **Q-12, la couche d'identité** : elle **existe, mais pas pour nous**.
  - Depuis un décret d'avril 2020, l'opérateur doit recueillir le **NPI** de chaque abonné, le faire vérifier en temps réel par l'ANIP et le conserver [R-211]. L'ANIP indique que l'achat d'un numéro exige une authentification par NPI et empreinte [R-208] (**prouvé**, deux sources de l'administration béninoise).
  - En revanche, ce lien numéro ↔ NPI n'est communicable qu'à l'ARCEP, aux services de sécurité et aux autorités judiciaires [R-211]. Le service de vérification d'identité de l'ANIP prévoit les banques parmi ses utilisateurs, mais sans convention ni interface publique, avec un modèle payant annoncé pour 2027 [R-208], [R-209] (**prouvé** pour l'annonce).
  - Un relevé apporté par le client ne peut donc pas, aujourd'hui, être rattaché au NPI par un tiers privé. Il peut l'être par le **nom et le numéro**, si le relevé les porte (test T2), et par la vérification de la pièce d'identité que la banque fait déjà à l'ouverture (**déduit**).
- **Q-02, les données pour construire le projet** : **aucun jeu de données public ne couvre un pays de l'UEMOA avec une variable de défaut et une licence commerciale** (**prouvé** pour les jeux lus).
  - L'enquête ménages EHCVM du Bénin et le Findex 2025 du Bénin sont réservés à la recherche [R-224], [R-230].
  - Les jeux africains trouvés avec une variable de défaut sont tous hors UEMOA : Kenya et Ghana (propriété du client [R-221]), Zimbabwe (propriété de Zindi et de l'hôte [R-232]), Ouganda (licence non affichée [R-231]).
  - Le bac à sable de la BCEAO (**LIF-BCEAO**) couvre explicitement le « scoring de crédit » et accepte les fintechs, seules ou en partenariat [R-233] (**prouvé**). Le guide ne prévoit pas que la BCEAO fournisse des données (**indice** : absence constatée dans le texte).

### Ce que cela change pour le périmètre

- **Le déclencheur de révision n°2 du point de décision 1** (« aucune des trois voies n'est praticable ») **n'est pas atteint** : la voie 1 est praticable. Mais elle est la moins différenciante.
- **La différenciation** promise par la phrase du projet (« le comportement de paiement observé sur plusieurs mois ») repose sur la voie 2, qui n'est pas démontrée. Elle peut toutefois se replier, **sans changer de périmètre**, sur les **flux des comptes que la banque tient elle-même** : la banque voit les mouvements des comptes de ses clients. C'est un comportement observé sur plusieurs mois, accessible par la voie 1 (**déduit**, à confirmer avec une banque).
- **Pour construire le projet**, sans données ouvertes utilisables commercialement, il faut :
  - soit un **partenariat** (banque ou IMF de l'article 44, éventuellement dans le cadre du LIF-BCEAO) ;
  - soit un **démonstrateur sur données synthétiques** calibrées sur les statistiques déjà vérifiées, qui démontre la chaîne technique mais pas la performance.

**Principale réserve.** Plusieurs conclusions reposent sur une **absence** constatée sur le web : pas d'export, pas d'agrégateur, pas d'API. Une absence n'est pas une preuve. Les tests de la section 10 et les questions écrites de la section 11 peuvent la transformer en fait en quelques jours.

---

## 2. Volet D1 : voie 1, données de la banque et bureau de crédit

**Rappel.** Le prix du rapport pour une banque n'est pas public (acquis de la question 21, QO-C7) : il n'a pas été cherché.

### 2.1 Le rapport de solvabilité de Creditinfo West Africa

Le site actuel du bureau bloque les accès automatisés. Ses pages ont été lues dans des copies d'archive (Wayback Machine). Le contenu actuel peut différer.

| Élément | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| **Contenu** | Identité (nom, numéro de pièce, profession ; raison sociale et registre du commerce pour une entreprise) ; demande de crédit (objet, date, montant) ; consultations précédentes par des établissements ; historique des contrats en cours et échus ; détail de chaque crédit (type, montant, **échéances payées et impayées**) ; incidents de paiement ; informations négatives | prouvé (deux sources) | [R-154] (FAQ archivée en 2025-11), [R-160] (fiche du Trésor béninois) |
| **Rapport le plus complet** | « Rapport Creditinfo Plus » : ajoute la notation et le Creditinfo Predictor, et affiche les remboursements sur les prêts passés et en cours | prouvé (même éditeur) | [R-154], [R-155] |
| **Score** | **Creditinfo Predictor** : note de **250 à 900** et classe de risque de **A à E**, avec des **codes de motif** qui expliquent la note ; un « rapport de notation » donne aussi l'historique de la note | prouvé (description de 2022, même éditeur) ; lien avec le « Score CIP » de 2018 déduit | [R-156], [R-125] |
| **Format et canal** | Côté banque, tableau de bord avec feux tricolores et onglets détaillés, donc une interface web (déduit). Côté particulier, **HelloCreditinfo** sur WhatsApp (depuis juillet 2024, numéro ivoirien ; fonctionnement depuis le Bénin non vérifié) pour télécharger son rapport. **Aucune API** trouvée dans les pages lues | prouvé (descriptions) ; absence d'API : indice | [R-157], [R-158] |
| **Accès du particulier** | Rapport gratuit une fois par an [R-160], [R-164]. Le formulaire de 2025 demande la pièce d'identité (CNI ou passeport) et un consentement signé [R-159]. Contact à Cotonou : +229 66 48 55 55 [R-160] | prouvé | [R-159], [R-160], [R-164] |
| **Correction des erreurs** | Enquête du bureau sous 2 jours, correction sous 15 jours selon la fiche du Trésor. La loi uniforme citerait d'autres délais (indice) | prouvé (fiche) ; divergence : indice | [R-161], [R-052] |
| **Facturiers** | Fin 2025, 21 grands facturiers participent au bureau, dont 4 au Bénin (acquis de la question 21). Leur présence dans le rapport d'un particulier n'est pas établie | prouvé (participation) ; contenu du rapport : non vérifié | [R-004] |
| **Profondeur réelle** | Nombre de mois d'historique, présence des garanties, des jours de retard : **non établis**. Une page de 2020 renvoyait à un modèle de rapport (PDF de 2018), qui n'est plus en ligne ni archivé | non vérifié | [R-162] |

### 2.2 Ce que la banque détient et déclare

| Élément | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| **Déclaration mensuelle** | Les banques et les SFD transmettent leurs données de crédit **à la BCEAO**, sur support électronique, **chaque mois au plus tard le 10** ; le bureau les collecte auprès de la BCEAO. Le format est fixé par le contrat avec le bureau, et il n'est pas publié | prouvé (deux sources) | [R-163], [R-154] |
| **Contenu de la loi uniforme sur les bureaux de crédit** | Consentement écrit préalable ; historique conservé 5 ans ; Centrale des risques, Centrale des incidents de paiement et grands facturiers parmi les sources | indice (lecture par mots-clés) | [R-052] |
| **Transmission à un prestataire** | La loi bancaire permet de communiquer des données couvertes par le secret à un prestataire chargé de « fonctions opérationnelles » (art. 68). La sous-traitance impose des données disponibles dans l'UMOA et la soumission du contrat à la Commission bancaire (circulaire 04-2017, art. 33) | prouvé (axe B) | [R-059], [R-033] |

**Lecture (déduit).** La banque possède trois sources de données exploitables :
- le **fichier qu'elle déclare chaque mois** (crédits, échéances, impayés) ;
- le **rapport du bureau** sur ses demandeurs ;
- les **mouvements des comptes qu'elle tient** (versements, retraits, virements).

C'est cette troisième source, rarement citée, qui peut fournir le « comportement de paiement sur plusieurs mois » **sans passer par l'opérateur**, pour les clients qui ont déjà un compte dans la banque. La limite reste la même : le bureau couvre 25 % des adultes [R-004], et un nouveau client n'a pas d'historique chez la banque.

---

## 3. Volet D2 : voie 2, relevés apportés par le client

### 3.1 Ce que l'on sait des historiques au Bénin

| Élément | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| Application **MyMTN BN** (version du 26/10/2026) | Permet de « suivre ses transactions MoMo en temps réel ». Sa fiche ne mentionne **ni export, ni relevé, ni PDF** | prouvé (contenu de la fiche) ; l'absence d'export dans l'application n'est **pas** prouvée | [R-176] |
| Application **Moov Money BJ** (version de juillet 2026, donc à revérifier) | Transferts, factures, accès aux comptes des banques partenaires. Aucune mention d'historique exportable | prouvé (fiche) | [R-177] |
| Application **MyMoov** | Permettrait de consulter son solde et « les relevés de toutes ses transactions » : le seul indice favorable à un relevé côté client au Bénin | indice (extrait de moteur, fiche non ouverte) | [R-236] |
| **Celtiis Cash** | Accessible par la super-application « waa », ouvrable quel que soit l'opérateur. Historique détaillé des achats mentionné, sans export | indice | [R-179] |
| **USSD** | Sur MTN MoMo, le menu est `*880#` [R-178]. Selon une page sur le Congo, l'historique par USSD se limite à un mini-relevé des 5 à 10 dernières opérations [R-204] | indice (autre pays pour le mini-relevé) | [R-178], [R-204] |
| **Documents contractuels MoMo** | La page en ligne de la politique de confidentialité MoMo ne donne qu'un résumé. Le PDF complet et les conditions générales MoMo renvoient une **erreur 404** le 22/11/2026. La durée de conservation, le droit d'obtenir un relevé et le partage avec des tiers n'ont donc pas pu être établis | prouvé (erreur constatée deux fois, par deux méthodes) | [R-185], [R-186] |
| **Moov et Celtiis** | Aucune condition générale propre au Bénin trouvée (seule celle de Moov Côte d'Ivoire) | absence constatée | [R-190], [R-191] |
| **Usage interne par l'opérateur** | Les conditions de Prêt Xpress définissent des « données d'utilisation du compte Mobile Money » : MTN exploite déjà ces données pour son propre crédit | indice | [R-018] |
| **API pour développeurs** | Le portail MoMo propose l'encaissement, le décaissement et les transferts [R-189]. Une question de mars 2026 (forum du groupe MTN, section Ouganda) sur une API d'historique lisible par un tiers avec consentement est restée sans réponse [R-187]. Le Bénin semble ouvert à la mise en production, avec des pièces d'entreprise locale (question d'un utilisateur, fil non ouvert) [R-188] | prouvé (trois produits, fil sans réponse) ; Go-Live au Bénin : indice ; absence d'API d'historique : indice, à source unique | [R-187], [R-188], [R-189] |
| **Portefeuilles multiples** | Les comptes mobile money et bancaires sont déjà reliés : Celtiis Cash avec Ecobank et UBA | indice | [R-180] |
| **Parts de marché** | L'ARCEP publie des tableaux trimestriels des services financiers mobiles, au moins jusqu'au T3 2025, utiles pour choisir l'opérateur à tester en premier. Contenu non lu | indice | [R-181] |

**Conclusion (indice).** Aucune source publique ne montre qu'un client béninois peut exporter un historique de plusieurs mois lisible par une machine. **Ce n'est pas prouvé non plus qu'il ne le peut pas.** Les tests T1 à T7 trancheront.

### 3.2 Précédents ailleurs, et ce qu'ils prouvent

| Précédent | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| **Kenya, relevés M-Pesa** | Relevés demandés par l'application ou `*334#`, livrés en **PDF protégé par un mot de passe** envoyé par SMS. Le mot de passe protège la confidentialité, **pas l'authenticité** du document remis à un prêteur | indice (presse) ; conclusion sur l'authenticité déduite | [R-182] |
| **Kenya, analyse de relevés par les prêteurs** | Des solutions analysent des relevés M-Pesa fournis par le client (question 21) [R-118], [R-119]. Une source signale des relevés PDF falsifiés par IA générative, et des prêteurs qui passent à un accès direct par API | prouvé (offres) ; falsification : source faible | [R-118], [R-119], [R-198] |
| **Nigeria, agrégation de comptes** | L'agrégateur Okra, malgré plus de 16 M$ levés, a fermé en mai 2025 ; son concurrent Mono a été racheté par Flutterwave. Le modèle économique de l'analyse de comptes reste fragile | indice | [R-183] |
| **Inde, Account Aggregator** | Volumes très élevés (plus de 180 millions de comptes liés), mais aucun taux de défaut ni mesure de pouvoir prédictif publiés dans l'extrait vu | indice | [R-184] |
| **Pouvoir prédictif** | Björkegren et Grissen (World Bank Economic Review, 2020) : les signatures comportementales tirées de l'**usage du téléphone** prédisent le remboursement ; le quintile le plus risqué fait défaut 2,8 fois plus que le moins risqué. Il s'agit de relevés d'appels d'un opérateur télécom sud-américain, collectés **par l'opérateur prêteur**, pas de relevés mobile money apportés par le client. AUC annoncées de 0,77 et 0,76 : indice (absentes du résumé lu) | prouvé (résumé) ; historique | [R-194] |
| Préprint « FairLend-Africa » (2026) | ROC-AUC de 0,71 avec des transactions mobile money, des recharges téléphoniques et la régularité de l'épargne (origine des données et pays non vérifiés) | indice (extrait de moteur, préprint non relu par des pairs) | [R-195] |
| **Fraude documentée** | Au Kenya, la fraude documentée porte surtout sur de **faux SMS** M-Pesa. Aucun cas documenté de faux relevé présenté à un prêteur n'a été trouvé | indice | [R-196], [R-197] |

**Conclusion (déduit).** **Aucune étude publiée ne mesure le pouvoir prédictif d'un relevé apporté par le client.** Les chiffres solides portent sur des données collectées par l'opérateur lui-même. Le gain de la voie 2 ne pourra donc être mesuré qu'en test rétrospectif chez un partenaire.

---

## 4. Volet D3 : voie 3 (PI-SPI), registre des agréments, agrégation de comptes

### 4.1 Le paiement instantané de la BCEAO (PI-SPI)

| Élément | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| **Nature et lancement** | Plateforme interopérable du système de paiement instantané de l'UEMOA, **lancée le 30/09/2025**, ouverte jour et nuit. Elle permet les transferts entre comptes de banques, d'IMF et d'émetteurs de monnaie électronique, « indépendamment du type de compte » | prouvé (deux documents BCEAO) | [R-168], [R-169] |
| **Participants** | **80** au 02/04/2026 (59 banques, 9 émetteurs de monnaie électronique, 11 IMF, 1 établissement de paiement), connexion exigée au plus tard le 30/06/2026. Échéances ensuite repoussées (indice). Au Bénin, **6** participants au 13/11/2025 : BOA, Coris Bank, Ecobank, Orabank, UBA, Moov Money. **175** participants au 30/09/2026, dont 18 au Bénin (indice) | prouvé (80, 6) ; indice (175, 18) | [R-168], [R-171], [R-172], [R-206] |
| **MTN MoMo** | Adoption du PI-SPI « dès le 2 novembre », avec de nouveaux plafonds et une nouvelle grille. **L'année est incertaine** : 2025 selon une source, 2026 selon une autre | contesté | [R-178], [R-205] |
| **Accès d'un tiers** | Les entreprises et prestataires passent par l'**« API Business » d'un participant**, homologuée par la BCEAO. Elle sert à payer, encaisser et suivre **ses propres** transactions. **24** homologuées au 17/09/2026, dont **une seule au Bénin : Ecobank**, et toujours une seule en novembre 2026 | prouvé (deux sources) | [R-170], [R-205] |
| **Données échangées** | Norme ISO 20022 et API standardisées : vues seulement dans un extrait de presse ; aucune source BCEAO lue ne les cite | indice | [R-173] |

**Conclusion (déduit).** Un prestataire de scoring ne peut pas lire les flux PI-SPI des particuliers. Au mieux, une **TPE cliente d'Ecobank** pourrait lui ouvrir l'accès à ses propres flux par l'API Business de sa banque. Comme la bascule des opérateurs est récente, l'historique PI-SPI disponible est court : quelques semaines si MTN MoMo a basculé le 2 novembre 2026, environ un an si c'était en 2025 (date contestée).

### 4.2 Le registre officiel des agréments (QO-C1)

| Catégorie | Contenu du registre | Niveau | Sources |
|---|---|---|---|
| **Établissements de paiement** | **34** agréés dans l'UMOA au 31/08/2026, dont **4 au Bénin** : Julaya Bénin, Open SI, FedaPay Bénin, QOS Integrated Center Bénin. La liste ne donne que le nom, le numéro et la date d'agrément, **jamais les services autorisés** | prouvé (deux listes officielles) | [R-165], [R-166], [R-167] |
| **Émetteurs de monnaie électronique** | 18 dans l'UMOA au 29/06/2026, dont 3 au Bénin : MTN Mobile Money Bénin, Moov Money Bénin, International Digital Money | prouvé | [R-166], [R-167] |
| **Agrégateurs de comptes enregistrés** | **Aucune liste publiée trouvée** ; aucun agrégateur identifiable publiquement | indice (absence constatée) | [R-165], [R-166] |

**Réponse à QO-C1.** Le registre public **ne permet pas** de savoir qui est autorisé pour l'information sur les comptes. Les agrégateurs « purs » ne sont pas agréés mais enregistrés (section 4.3), et leur liste n'a pas été trouvée. **Seule la BCEAO peut répondre** (question n°1 de la section 11).

### 4.3 L'agrégation de comptes : ce que permet le texte

| Règle | Instruction BCEAO 001-01-2024 | Niveau | Sources |
|---|---|---|---|
| **Statut** | Un prestataire qui fournit **uniquement** l'agrégation de comptes ou l'information sur les comptes est **enregistré** par la BCEAO, et non agréé, puis inscrit sur une liste qu'elle tient (art. 9 et 22 à 25 ; demande instruite en 3 mois) | **prouvé, deux sources** | [R-048], [R-174] |
| **Dossier** | Le dossier suit un canevas commun aux établissements de paiement. Il faut une assurance de responsabilité civile professionnelle ou une garantie financière (annexes I et II) ; capital minimum de 10 M FCFA pour un agrégateur seul selon un extrait de moteur (article non ouvert) | prouvé (annexes) ; capital : indice | [R-048] |
| **Interface obligatoire** | Art. 60 : les prestataires « qui gèrent des comptes accessibles en ligne doivent fournir au moins une interface d'accès sécurisée » aux agrégateurs ; l'usage des données personnelles « requiert [le] consentement explicite » du client | prouvé, **à source unique** : une analyse juridique ne corrobore que le consentement explicite (art. 30), sans traiter l'art. 60 | [R-048], [R-175] |
| **Sans contrat** | Art. 63 : le service « n'est pas subordonné à l'existence de relations contractuelles » entre l'agrégateur et le gestionnaire du compte, qui doit traiter les demandes « sans aucune discrimination » | prouvé, **à source unique** | [R-048] |
| **Limite d'usage** | Art. 31 : l'agrégateur ne peut utiliser les données « à des fins autres que la fourniture du service [...] expressément demandé par l'utilisateur ». Le scoring doit donc faire partie de ce que le client demande | prouvé ; conséquence déduite | [R-048] |
| **Comptes de monnaie électronique** | L'Instruction s'applique aux émetteurs de monnaie électronique (art. 2), mais le « compte de paiement » est défini comme un compte d'établissement de paiement. **L'application de l'art. 60 aux portefeuilles MoMo est plausible mais pas établie** | ambigu | [R-048] |
| **Normes techniques et mise en œuvre** | Aucune norme d'interface publiée, aucun cadre d'open banking, aucune interface ouverte constatée. La mise en conformité générale a été repoussée plusieurs fois | absence constatée ; prorogations : indice | [R-048], [R-207] |

**Conclusion (déduit).** Le texte de 2024 fournit une **voie réglementaire** à la voie 2 : un client peut demander qu'un agrégateur enregistré lise ses comptes, et le teneur de compte doit lui ouvrir une interface sans contrat. C'est la version propre, non falsifiable, du « relevé apporté par le client ». Mais rien ne montre qu'elle fonctionne aujourd'hui. Elle suppose aussi de **s'enregistrer comme agrégateur**, ce qui change la nature du projet : une entité régulée plutôt qu'un simple logiciel.

---

## 5. Volet D4 : la couche d'identité (Q-12)

### 5.1 Au Bénin

| Élément | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| **Couverture** | Près de **13,8 M** d'inscrits au registre national des personnes physiques (RNPP) ; 8,9 M de personnes ont retiré une pièce au 06/05/2026. La Banque mondiale cite « 7,7 M de NPI », probablement le nombre de certificats (CIP) délivrés : incohérence de source | prouvé (ANIP) ; écart : déduit | [R-208], [R-210] |
| **Pièces** | Certificat « C'est moi » (gratuit, 7,5 M), certificat d'identification personnelle (1 000 FCFA, 7,7 M), carte d'identité biométrique avec puce (près de 2 M) | prouvé | [R-208] |
| **Lien NPI ↔ numéro de téléphone** | Décret du 22/04/2020 : l'opérateur recueille le **NPI** avant toute fourniture du service (art. 8), le fait **vérifier en temps réel par l'ANIP** contre redevance (art. 5) et le **conserve** avec une copie des pièces tant que l'abonné est actif, puis 5 ans (art. 12). Il abroge le décret de 2016, qui ne mentionnait pas le NPI. L'ANIP confirme : « l'acquisition de numéro de téléphone [est] conditionné[e] par l'authentification à partir du NPI et de l'empreinte » | **prouvé, deux sources** (deux institutions distinctes du même État, donc pas totalement indépendantes ; numéro exact du décret, probablement 2020-249, non confirmé) | [R-211], [R-212], [R-208] |
| **Qui peut obtenir ce lien** | Seulement l'ARCEP, le Centre de documentation de sécurité publique et les autorités judiciaires et administratives sur injonction (art. 11 et 14). **Aucune communication à une banque ou à une fintech n'est prévue** | prouvé (texte) ; absence de base légale pour un tiers privé : déduit | [R-211] |
| **Vérification d'identité par un tiers** | 25 M (ou 27 M selon la présentation) de vérifications d'identité en 2025. L'ANIP place les banques parmi les utilisateurs de sa plateforme d'interopérabilité. L'ANIP « doit tirer profit prochainement des eKYC », avec un modèle économique attendu en 2027. Aucune convention, aucun tarif, aucune API publique | prouvé (annonces) ; ouverture aux banques : indice | [R-208], [R-209] |
| **NPI et comptes** | Aucune source ne dit que le NPI est exigé pour ouvrir un compte bancaire ou mobile money, ni qu'il est relié aux comptes. La carte « C'est moi » faciliterait l'ouverture d'un compte mobile money | absence constatée ; indice | [R-208], [R-218] |
| **Plafonds de monnaie électronique** | Depuis le 02/11/2026, 4 M FCFA d'avoirs par « client identifié » et par émetteur, 15 M FCFA de rechargements par mois (Instruction n°020 du 08/10/2026). Rien sur les pièces d'identité | prouvé | [R-192], [R-193] |
| **Fiabilité de l'identification** | Des campagnes de coupure de lignes non identifiées ont eu lieu en 2025, et la justice a mis en garde les distributeurs de cartes SIM | indice | [R-213], [R-214] |

### 5.2 Au Nigeria, le modèle cité le 18/11/2026

- La liaison entre carte SIM et numéro national d'identification (NIN) est obligatoire depuis 2020.
- La plateforme NINAuth (2025) offre une authentification par interface aux administrations et aux entreprises [R-215].
- Banques et fintechs vérifient le numéro bancaire BVN et le NIN en temps réel par des interfaces agréées par la banque centrale [R-216].
- Plus de 70 millions de BVN sont enregistrés [R-217].

Niveau : **indice** pour tout ce paragraphe (presse et blog d'un fournisseur ; sources primaires non lues).

**Conclusion (déduit).** Le Bénin a **la même brique de base que le Nigeria**, puisque le numéro de téléphone est rattaché à une identité vérifiée. Ce qui manque, c'est **l'accès d'un tiers privé** à cette brique, que le Nigeria a organisé et que le Bénin annonce pour plus tard. En attendant, un relevé peut être rattaché au client par son **nom et son numéro**, à condition que le relevé les porte (test T2). La banque, de son côté, vérifie déjà la pièce d'identité. Deux limites restent :
- le **partage de téléphone** (22 % des cartes SIM utilisées par plusieurs personnes au Togo voisin [R-199]) ;
- les failles de l'identification à la vente [R-213].

Ces limites rendent le lien « numéro = une personne » imparfait.

---

## 6. Volet D5 : les données pour construire le projet (Q-02)

### 6.1 Les jeux de données individuels et leur licence

| Jeu de données | Contenu utile | Variable de défaut | Pays et années | Licence exacte | **Utilisable dans un produit commercial** | Niveau | Sources |
|---|---|---|---|---|---|---|---|
| **EHCVM Bénin 2021-2022** (enquête ménages harmonisée de l'UEMOA, environ 8 000 ménages) | Conditions de vie des ménages ; présence d'un module sur l'emprunt non vérifiée | Non | Bénin, 2021-2022 | Microdata **Research Data License** : « statistical and scientific research purposes only », pas de redistribution ni de vente sans accord écrit | **Non** | prouvé | [R-224], [R-225] |
| **Global Findex 2025, fichier Bénin** (1 000 répondants, 199 variables) | Compte, paiements numériques, emprunt, épargne | Non | Bénin, collecte 2024 | Conditions de la Microdata Library : recherche seulement, pas de redistribution ni de vente | **Non** | prouvé | [R-230], [R-222] |
| **Global Findex 2021** | Mêmes thèmes, 139 économies | Non | 2021 | Research Data License (lue sur la fiche d'un pays) | **Non** | prouvé (un pays) ; indice (les autres) | [R-229], [R-223] |
| Zindi « **African Credit Scoring Challenge** » | Prêts et clients d'institutions, indicateurs macroéconomiques | **Oui** | Kenya, Ghana (2024-2025) | « The data is private property of the client » ; redistribution interdite | **Non** | prouvé (statut) ; usage commercial exclu : déduit | [R-221], [R-220] |
| Zindi « **IndabaX Zimbabwe 2026** » | Prêts de type bancaire | **Oui** | Zimbabwe, 2026 | « Sole property of Zindi and the competition host » | **Non** | prouvé | [R-232] |
| Zindi « **Xente Credit Scoring Challenge** » | Transactions et prêts | **Oui** (`IsDefaulted`) | Ouganda | Aucune licence affichée | **À vérifier** | prouvé (contenu) | [R-231] |
| Zindi « **Financial Inclusion in Africa** » (environ 33 600 personnes) | Démographie, détention d'un compte | Non | Kenya, Rwanda, Tanzanie, Ouganda, 2016-2018 | Aucune licence affichée ; Zindi distingue les jeux en accès ouvert (CC-BY-SA 4.0) et les jeux propriétaires | **À vérifier** | prouvé (contenu) | [R-219], [R-220] |
| **Home Credit Default Risk** (Kaggle) | Demandes de crédit, historique de bureau | **Oui** | Non vérifié | Règles illisibles sans connexion | **À vérifier** | non établi | [R-227] |
| **Kiva** (instantanés de données) | Prêts de microfinance : montant, secteur, pays, statut | Indice (statut « defaulted ») | Plusieurs pays ; UEMOA à vérifier | Conditions des instantanés non lues ; version Kaggle signalée sous CC0 et API réservée à un usage commercial « to charitable ends » (extraits de moteur) | **À vérifier** | indice | [R-228] |
| **German Credit** (UCI) | 1 000 demandeurs, 20 variables | **Oui** | Allemagne, 1994 (historique) | **CC BY 4.0** | **Oui** (avec attribution), mais **non représentatif** de l'UEMOA | prouvé | [R-226] |

**Lecture (déduit).**
- Aucun jeu ne réunit les quatre conditions : public, UEMOA, variable de défaut et usage commercial.
- Les enquêtes de la Banque mondiale (EHCVM, Findex) servent à **calibrer des distributions** dans un travail de recherche : taux d'emprunt formel et informel, par sexe et par niveau de revenu. Elles ne servent pas à entraîner un produit.
- German Credit et Home Credit (si sa licence le permet) ne servent qu'à **tester la chaîne technique**.

### 6.2 Données synthétiques

- Des méthodes récentes génèrent des données financières tabulaires sous contraintes, par exemple la diffusion tabulaire contrainte présentée en 2025 [R-234]. Seul le résumé a été lu : jeux et limites non précisés (**prouvé** pour le résumé).
- **Limite de principe (déduit)** : un générateur calibré sur des statistiques agrégées ne reproduit que les dépendances qu'on y met. Un modèle entraîné dessus apprend ces hypothèses, pas le comportement réel. Les données synthétiques permettent donc de démontrer et de tester l'outil, **jamais d'en valider la performance**.

### 6.3 Partenaires et cadre d'accès

| Piste | Ce que disent les sources | Niveau | Sources |
|---|---|---|---|
| **LIF-BCEAO** (laboratoire d'innovation financière, bac à sable) | Domaines éligibles : « micro-crédit, **crédit scoring**, épargne numérique ». Peuvent candidater les institutions agréées et « les startups, les entreprises de technologies financières, à titre individuel ou en partenariat avec une institution financière agréée » ; le dossier demande, le cas échéant, le contrat d'agence avec un établissement agréé. Test de 3 à 6 mois, prorogeable dans la limite de 2 ans. **La BCEAO ne fournit pas de données** : le candidat apporte ses clients et ses données | prouvé (absence de données fournies : indice) | [R-233] |
| **Bureau de crédit** | Accès à des fins de recherche : non documenté | non trouvé | |
| IFC, UNCDF, CGAP, laboratoires universitaires | Non couverts faute de budget | non trouvé | |

**Conclusion (déduit).** La voie réaliste pour des données réelles est un **partenaire agréé**, banque ou IMF de l'article 44, qui apporte ses données. Cela peut se faire dans le cadre du LIF-BCEAO, qui offre un cadre réglementaire au test, ou sous un accord de confidentialité avec un déploiement chez le partenaire (axe B).

---

## 7. Enseignements croisés

1. **La donnée de flux la plus accessible est celle de la banque elle-même** (D1 et D2). L'historique mobile money est chez l'opérateur, qui ne publie aucun accès pour les tiers [R-187], [R-189]. Mais la banque voit les mouvements des comptes qu'elle tient et déclare ses crédits chaque mois [R-163]. Pour ses clients existants, le « comportement de paiement sur plusieurs mois » est **déjà dans la voie 1** (**déduit**). La voie 2 n'est indispensable que pour les **nouveaux** clients, qui n'ont pas d'historique à la banque.
2. **La voie 2 a deux versions, et la plus solide est aussi la plus lourde** (D2 et D3).
   - Le relevé exporté par le client est simple, mais falsifiable [R-182], [R-198] et de forme inconnue au Bénin.
   - L'agrégation de comptes réglementée n'est pas falsifiable et ne demande pas de contrat [R-048]. Mais elle n'a pas été vue en fonctionnement, et elle impose de s'enregistrer comme agrégateur.

   Le choix entre les deux est une **décision de nature du projet** : un logiciel installé chez la banque, ou un acteur régulé (**déduit**).
3. **L'identité n'est pas le maillon le plus faible ; l'accès l'est** (D4 et D2). La brique « numéro = personne identifiée » existe en droit au Bénin [R-211], [R-208]. Ce qui bloque, c'est qu'aucun tiers privé ne peut l'interroger, et que l'opérateur n'ouvre pas ses historiques. Le jour où l'ANIP ouvrira son service de vérification aux banques (annoncé pour 2027), le rattachement d'un relevé à une personne deviendra vérifiable (**déduit**).
4. **Le PI-SPI change l'interopérabilité, pas l'accès aux données** (D3). Il relie les comptes entre institutions pour payer, mais ne donne pas à un tiers la lecture des flux des particuliers [R-170], [R-205]. Il pourra servir plus tard, si un service d'accès consenti s'y adosse (**déduit**).
5. **Sans partenaire, le projet reste un démonstrateur** (D5). Aucune donnée ouverte ne permet d'entraîner un produit commercial pour l'UEMOA [R-224], [R-230], [R-221]. Le LIF-BCEAO donne un cadre au partenariat, mais pas de données [R-233].

---

## 8. Ce qui contredit la faisabilité (passe de contradiction)

Un assistant au regard neuf a cherché ce qui rendrait les voies impraticables, **en priorité la voie 2**, sans connaître nos preuves.

| Conclusion attaquée | Verdict | Argument contraire le plus fort | Sources |
|---|---|---|---|
| **Voie 2 praticable** | **Affaiblie** | Aucune procédure publique d'export au Bénin : le seul document trouvé sur la réconciliation de plusieurs portefeuilles ne dit rien des formats natifs des opérateurs, et le seul accès documenté est un mini-relevé de 5 à 10 opérations (page sur le Congo). Un relevé PDF peut être falsifié : des faux fabriqués par IA sont signalés au Kenya. Le partage de téléphone (22 % des SIM au Togo) mélange les historiques. Le paiement en espèces reste dominant au Bénin, au point que l'État taxe à 1 % les paiements en espèces de plus de 100 000 FCFA depuis janvier 2025 (indice) | [R-203], [R-204], [R-198], [R-199], [R-201], [R-200] |
| **Accès consenti par l'Instruction BCEAO** | **Affaiblie** | Le texte existe, mais aucun agrégateur enregistré, aucune interface ouverte et aucune norme technique n'ont été trouvés. La mise en conformité a été repoussée plusieurs fois. Le seul agrégateur africain étudié (Okra, Nigeria) a fermé | [R-165], [R-207], [R-183] |
| **Rattachement par le NPI** | **Affaiblie** | Le NPI garantit qu'une ligne a été enregistrée au nom de quelqu'un, pas que cette personne utilise le portefeuille. Coupures de lignes non identifiées en 2025 et mises en garde aux distributeurs | [R-213], [R-214], [R-199] |
| **Voie 3** | **Presque contredite pour les particuliers** | L'API Business sert à une entreprise cliente pour ses propres paiements ; une seule au Bénin (Ecobank) ; si MTN MoMo n'a basculé que le 2 novembre 2026, l'historique ne fait que quelques semaines | [R-205], [R-178] |
| **Voie 1** | **Tient, avec réserves** | Aucune interdiction de transmettre le rapport du bureau n'a été trouvée (loi uniforme lue en partie seulement). Mais le bureau couvre surtout les personnes qui ont déjà emprunté : en 2019, la Banque mondiale comptait environ 5,5 M de personnes et d'entreprises en trois ans, jugeait la couverture « améliorable » et citait le consentement comme un frein (indice). La loi béninoise sur le bureau a été modifiée en 2020, sans que le contenu ait été lu. La population ciblée aura souvent un rapport vide | [R-235], [R-057] |

**Point à vérifier signalé par la contradiction.** Un extrait du Findex 2025 indiquerait que 30,8 % des répondants béninois ont déjà eu un compte mobile money [R-202]. C'est très en dessous des 44,9 % retenus dans l'axe A [R-013]. L'extrait porte probablement sur un sous-échantillon (92 réponses sur 299 dans l'extrait) : **indice à vérifier**, sans changer pour l'instant le chiffre de l'axe A.

**Ce que la contradiction n'a pas trouvé** :
- une interdiction réglementaire ou contractuelle explicite pour un client de partager son historique ;
- une étude montrant que les relevés apportés par le client prédisent mal le remboursement ;
- un cas béninois ou de l'UEMOA de prêteur trompé par un faux relevé.

**Conséquence.** Les verdicts de la synthèse tiennent compte de cette contradiction. La voie 2 est classée **« non établie »**, et non « praticable ». Les tests de la section 10 portent précisément sur les points qu'elle a soulevés : profondeur, format, identifiant du titulaire, possibilité de modifier le document.

---

## 9. Recommandations

1. **Faire les tests de la section 10 avant toute autre décision sur la voie 2.** Ils prennent quelques minutes et valent plus que n'importe quelle page d'aide. *Alimente : point de décision 2, D-020.*
2. **Reformuler la source du « comportement de paiement »** dans la phrase du projet. Ce comportement peut venir des **comptes tenus par la banque** (voie 1) pour les clients existants, et de la voie 2 pour les nouveaux clients. Confiance moyenne (déduit, à valider avec une banque). *Alimente : product brief (proposition de valeur), PRD (sources de données).*
3. **Poser deux questions écrites à la BCEAO** (direction nationale de Cotonou) : y a-t-il des agrégateurs de comptes enregistrés, et l'article 60 vise-t-il les portefeuilles de monnaie électronique ? Les réponses tranchent la version réglementaire de la voie 2. *Alimente : Q-11, P3.*
4. **Ne pas compter sur la voie 3 pour les particuliers.** La garder en veille, et réserver le cas des TPE clientes d'un participant à une étape ultérieure. Confiance moyenne à haute. *Alimente : D-020, architecture.*
5. **Pour Q-02, viser un partenaire agréé**, banque ou IMF de l'article 44, éventuellement dans le cadre du LIF-BCEAO [R-233]. En attendant, préparer un **démonstrateur sur données synthétiques**, présenté honnêtement comme un démonstrateur. Confiance haute pour le constat, moyenne pour la stratégie. *Alimente : Q-02, P3.*
6. **Demander son propre rapport au bureau de crédit** (test T8) pour en connaître la structure réelle avant d'en faire une variable du modèle. *Alimente : P3, P5.*
7. **Garder l'identité comme point de vigilance, pas comme verrou.** Rattacher le relevé par le nom et le numéro, contrôlés par la banque, et suivre l'ouverture du service de vérification de l'ANIP (annoncée pour 2027). *Alimente : Q-12, architecture.*

---

## 10. Tests à faire soi-même

**Pour qui :** Daniela, avec son propre compte mobile money au Bénin. **Durée :** quelques minutes par test. **Ordre :** du plus décisif au moins décisif. Si T1 donne un export de plusieurs mois, la voie 2 change de statut.

**Avant de commencer**
- Noter pour chaque test : la **date**, le **nom et la version de l'application** (menu Paramètres, puis « À propos »), et le **chemin exact suivi** (menus touchés, dans l'ordre).
- Faire des **captures d'écran**. Avant de les partager, masquer les montants, les noms de tiers et les numéros.
- **Ne jamais saisir ni montrer son code secret.** Ne rien valider qui déclenche une opération payante ou un prêt.
- Reporter les résultats dans la grille de fin de section.

### T1. L'application MTN MoMo permet-elle d'exporter un historique ? (le plus décisif)
1. Ouvrir l'**application MoMo** de MTN. Si elle n'est pas installée, ouvrir **MyMTN BN**. Si les deux sont installées, faire le test dans les deux.
2. Ouvrir l'**historique des transactions** (rubrique « Transactions », « Historique » ou « Activité » ; sinon chercher dans « Compte », « Profil » ou le menu « ... »).
3. Faire défiler jusqu'à la **transaction la plus ancienne affichée**. Noter sa date : c'est la **profondeur d'historique**.
4. Chercher un bouton **« Télécharger », « Exporter », « Relevé », « Partager » ou « Envoyer par e-mail »**, à côté de l'historique ou dans les menus.
5. S'il existe, demander le relevé le plus long possible et noter :
   - le **format** (PDF, CSV, autre) ;
   - le **choix de période** possible (1, 3, 6, 12 mois, dates libres) ;
   - le **mode de réception** (téléchargement, e-mail, SMS) ;
   - le **délai** ;
   - le **coût** éventuel.
6. S'il n'existe pas, noter « pas d'export » et passer à T2 avec l'écran d'historique.
7. Si les deux applications sont installées, noter si la profondeur d'historique est la même dans MoMo et dans MyMTN BN.

**Ce que la réponse change :** un export de plusieurs mois rend la voie 2a praticable techniquement. Son absence la renvoie vers l'agence (T7) ou vers l'agrégation réglementée.

### T2. Le relevé ou l'écran d'historique permet-il d'identifier le titulaire et d'analyser les opérations ?
Sur le relevé obtenu en T1, ou à défaut sur l'écran d'historique, cocher ce qui apparaît :
- **le nom complet** du titulaire, et s'il correspond exactement à la pièce d'identité ;
- **le numéro de téléphone** du titulaire ;
- **le NPI** ou un numéro de pièce d'identité ;
- un **numéro de compte** ou de portefeuille ;
- pour chaque opération :
  - **date et heure**, **montant** ;
  - **sens** (entrée ou sortie) ;
  - **type** (dépôt, retrait, transfert, paiement, facture) ;
  - **frais** ;
  - **solde après l'opération** ;
  - **nom ou numéro de la contrepartie** ;
  - **identifiant de transaction**.

**Ce que la réponse change :** sans nom ni numéro, le relevé ne peut pas être rattaché au client (Q-12). Sans solde ni type d'opération, il est beaucoup moins utile pour le scoring.

### T3. Le relevé est-il lisible par une machine, et peut-il être modifié ?
Uniquement si T1 a produit un fichier.
1. **PDF protégé ?** Le fichier demande-t-il un mot de passe à l'ouverture ? Si oui, comment arrive-t-il (SMS, e-mail, code fixe) ?
2. **Texte ou image ?** Dans le PDF, essayer de **sélectionner un mot**. Si on peut le sélectionner et le copier, c'est un PDF texte, lisible par une machine. Sinon, c'est une image, qu'il faudra traiter par reconnaissance de caractères.
3. **Élément de contrôle ?** Chercher :
   - un **QR code** ;
   - un **numéro de référence du relevé** ;
   - un **cachet** ;
   - dans un lecteur PDF sur ordinateur, une mention « **Signé par** » ou un panneau « Signatures ».
4. **Modifiable ?** Ouvrir une **copie** du fichier dans un éditeur PDF ou un traitement de texte, puis essayer de changer un montant. Noter si c'est **facile**, **difficile** ou **impossible**. Ne jamais utiliser le fichier modifié, et le supprimer ensuite.
5. Si c'est un **CSV**, l'ouvrir dans un tableur et noter les **noms des colonnes**.

**Ce que la réponse change :** un PDF texte signé ou vérifiable rend la voie 2a crédible face à la fraude. Un PDF image modifiable sans trace la rend fragile, comme au Kenya.

### T4. Les mêmes questions chez Moov Money et Celtiis Cash
Uniquement pour un portefeuille que Daniela possède, ou qu'elle peut ouvrir sans frais.
1. **Moov Money** : ouvrir **Moov Money BJ** (ou MyMoov), puis refaire T1, T2 et T3. Vérifier en particulier si une rubrique « relevés » existe, puisqu'une source l'annonce pour MyMoov.
2. **Celtiis Cash** : ouvrir la super-application **waa** (ou MyCeltiis Cash), rubrique Celtiis Cash, puis refaire T1, T2 et T3.
3. Pour chacun, noter le **code USSD** du menu (à lire sur la carte SIM, le site de l'opérateur ou en agence) et s'il propose un mini-relevé.

**Ce que la réponse change :** si un seul opérateur exporte, la voie 2a ne couvre que ses clients. Si aucun n'exporte, elle repose sur l'agence ou sur l'agrégation réglementée.

### T5. Que montre le menu USSD de MTN MoMo ?
1. Composer **`*880#`** et parcourir le menu sans valider d'opération.
2. Chercher une option « Mini-relevé », « Dernières transactions » ou « Historique ». Noter son chemin, par exemple « 5 puis 3 ».
3. Si elle existe : **combien d'opérations** sont affichées, sur quelle période, et le résultat arrive-t-il **à l'écran ou par SMS** ?

**Ce que la réponse change :** un mini-relevé de 5 à 10 opérations ne suffit pas au scoring. Il permet seulement de recouper un relevé plus long.

### T6. Les SMS de confirmation ont-ils un format stable ?
1. Dans la messagerie du téléphone, ouvrir les SMS envoyés par MTN MoMo (ou Moov, Celtiis).
2. Copier le **texte exact** de trois SMS : un **dépôt** reçu, un **retrait** et un **transfert** reçu ou envoyé. Remplacer les noms, les montants et les numéros par des X.
3. Pour chacun, noter s'il contient : identifiant de transaction, date et heure, montant, frais, **nouveau solde**, nom de la contrepartie.
4. Comparer les trois : la **structure** est-elle la même d'un SMS à l'autre, avec les mêmes mots aux mêmes places ?
5. Noter l'**expéditeur** affiché (« MoMo », « MTN », ou un numéro ordinaire).

**Ce que la réponse change :** des SMS stables et complets ouvrent une autre forme de voie 2 (lecture des SMS avec consentement) et donnent un moyen de recouper un relevé.

### T7. Peut-on obtenir un relevé officiel en agence, et quels documents contractuels s'appliquent ?
1. Dans une agence MTN, ou par le service client, demander un **relevé officiel du compte MoMo sur 6 et sur 12 mois**.
2. Noter :
   - si c'est **possible** ;
   - le **délai** et le **coût** ;
   - la **période maximale** ;
   - la **forme** (papier tamponné, PDF signé, envoi par e-mail) ;
   - les **pièces demandées**.
3. Demander si une banque peut **faire confirmer par MTN l'authenticité** d'un relevé, avec l'accord écrit du client.
4. Demander une copie des **conditions générales MoMo en vigueur** et de la **politique de confidentialité MoMo**, puisque les liens publics renvoient une erreur. Y repérer : durée de conservation, droit d'accès et de copie, partage avec des tiers.
5. Si possible, refaire la même démarche chez **Moov** et chez **Celtiis**.

**Ce que la réponse change :** un relevé officiel daté et tamponné est une forme de voie 2a moins falsifiable. Les conditions générales disent si le client a un droit contractuel à son historique.

### T8. Que contient réellement mon rapport au bureau de crédit ?
1. Demander son rapport gratuit (une fois par an) :
   - par **HelloCreditinfo** sur WhatsApp (+225 07 12 16 16 16, numéro ivoirien : noter s'il répond depuis le Bénin) ;
   - ou à l'antenne de Cotonou (+229 66 48 55 55), avec le formulaire et une pièce d'identité.
2. Noter :
   - les **rubriques présentes** ;
   - le **nombre de mois d'historique** de paiement ;
   - la présence d'un **score** (note de 250 à 900, classe de A à E, motifs) ;
   - la présence de **données de facturiers** (électricité, eau, téléphone) ;
   - les **jours de retard** et les **garanties** ;
   - le **délai de réception**.
3. Si l'on n'a jamais emprunté, noter simplement ce que dit le rapport : vide, ou présent mais sans crédit. C'est exactement la situation du client « sans historique ».

**Ce que la réponse change :** la structure réelle du rapport fixe ce que la voie 1 peut apporter au modèle.

### T9. L'application affiche-t-elle mon identité, et laquelle ?
1. Dans l'application MoMo (puis Moov, Celtiis), ouvrir **Profil** ou **Mon compte**.
2. Noter si apparaissent :
   - le **nom complet**, et s'il est identique à la pièce ;
   - le **NPI** ou le **numéro de pièce** ;
   - le **niveau de compte** (par exemple « vérifié » ou « niveau 2 »).
3. Dans un SMS de transfert reçu d'un proche, noter si le **nom de l'expéditeur** affiché est son nom complet officiel ou un surnom.
4. Si Daniela ouvre un compte Celtiis Cash, noter si le **NPI** est demandé et si une vérification par empreinte ou par code SMS a lieu.

**Ce que la réponse change :** si l'application affiche le nom officiel, le rattachement par le nom (Q-12) est plus fiable.

### T10. Le service de l'ANIP montre-t-il les numéros rattachés à mon NPI ?
1. Composer **`*151#`** (canal de l'ANIP), ou ouvrir l'application « ANIP BJ » ou eservices.anip.bj.
2. Chercher une option qui affiche :
   - les **numéros de téléphone liés à son NPI** ;
   - l'**historique des vérifications** faites sur son identité ;
   - une rubrique de **consentement** au partage avec un tiers.
3. Noter ce qui existe, même partiellement.

**Ce que la réponse change :** un tel service côté citoyen indiquerait une base possible pour un rattachement consenti.

### T11. Mon application bancaire permet-elle d'exporter un relevé ? (si Daniela a un compte bancaire)
1. Ouvrir l'application de sa banque et la rubrique **comptes** ou **relevés**.
2. Noter :
   - la **profondeur** d'historique et le **format** d'export ;
   - la présence du **nom** et du **numéro de compte** ;
   - s'il s'agit d'un PDF texte ou image, et s'il est signé.
3. Noter si l'application propose une rubrique de **partage de données** ou d'**accès d'un tiers**, qui serait un signe de l'interface de l'article 60.
4. Lors d'un passage en agence, demander si le **NPI** est exigé pour ouvrir un compte.

**Ce que la réponse change :** une banque qui exporte proprement ses relevés rend la voie 2 possible aussi pour les flux bancaires. La rubrique de partage indiquerait si l'article 60 est appliqué.

### Grille de résultats (à remplir)

| Test | Application et version | Date | Résultat principal | Profondeur | Format | Identifiant du titulaire | Modifiable | Remarque |
|---|---|---|---|---|---|---|---|---|
| T1 | | | | | | | | |
| T2 | | | | | | | | |
| T3 | | | | | | | | |
| T4 | | | | | | | | |
| T5 | | | | | | | | |
| T6 | | | | | | | | |
| T7 | | | | | | | | |
| T8 | | | | | | | | |
| T9 | | | | | | | | |
| T10 | | | | | | | | |
| T11 | | | | | | | | |

---

## 11. Questions ouvertes

### 11.1 À poser par écrit

| # | Destinataire | Question | Ce qu'elle tranche |
|---|---|---|---|
| 1 | **BCEAO**, direction nationale de Cotonou | Existe-t-il des agrégateurs de comptes enregistrés (art. 22 à 25 de l'Instruction 001-01-2024), et lesquels ? L'obligation d'interface de l'art. 60 vise-t-elle les portefeuilles de monnaie électronique ? Des normes techniques sont-elles prévues ? | La version réglementaire de la voie 2 |
| 2 | **MTN Mobile Money Bénin** | Un client peut-il obtenir un relevé de 12 mois, sous quelle forme ? Existe-t-il un service permettant de confirmer à une banque l'authenticité d'un relevé, avec le consentement du client ? | La voie 2a et sa résistance à la fraude |
| 3 | **ANIP** | Une banque peut-elle utiliser le service de vérification d'identité (eKYC), à quelles conditions et à quel tarif ? | Q-12 |
| 4 | **Creditinfo West Africa** | Le rapport est-il accessible par interface (API) pour une banque abonnée ? Un prestataire de la banque peut-il traiter le rapport ? | La voie 1 dans un outil tiers |
| 5 | **BCEAO** (LIF) | Calendrier des appels à candidatures du LIF-BCEAO | Q-02 (cadre du partenariat) |
| 6 | **APDP** (autorité de protection des données) | Une banque ou son prestataire doit-elle accomplir une formalité préalable (déclaration ou autorisation) pour traiter, à des fins de scoring, des relevés apportés par le client ? | La base légale de la voie 2 |

### 11.2 Questions de recherche non résolues

| # | Question | Pour y répondre |
|---|---|---|
| QO-D1 | Profondeur réelle du rapport du bureau de crédit et présence des facturiers béninois | Test T8 |
| QO-D2 | Numéro exact du décret d'avril 2020 (probablement 2020-249) | Journal officiel, SGG |
| QO-D3 | Date de bascule de MTN MoMo sur le PI-SPI (2025 ou 2026) | Communiqué MTN ou BCEAO |
| QO-D4 | Sources primaires nigérianes (NINAuth, circulaire de la banque centrale sur BVN et NIN, cadre d'open banking) | Recherche ciblée |
| QO-D5 | Licences de Xente, Financial Inclusion in Africa, Home Credit et Kiva | Lecture des règles avec un compte |
| QO-D6 | Variables de l'EHCVM sur l'emprunt, utiles au calibrage | Dictionnaire de variables |
| QO-D7 | Le chiffre de 30,8 % du Findex 2025 sur la détention d'un compte mobile money au Bénin | Lecture de la variable et de son dénominateur |
| QO-D8 | Pouvoir prédictif d'un relevé apporté par le client | Test rétrospectif chez un partenaire |

---

## 12. Sources utilisées

Les détails (lien, date de consultation, statut de vérification) sont dans la [bibliographie](../../REFERENCES.md). Les nouvelles sources ont été consultées le 22/11/2026 ; parmi les sources réutilisées, R-018, R-048, R-052, R-057 et R-125 ont été relues ce jour-là, les autres sont reprises des recherches précédentes.

Identifiants **réutilisés** : R-004, R-013, R-018, R-033, R-048, R-052, R-057, R-059, R-118, R-119 et R-125.

Identifiants **nouveaux** : R-154 à R-236.

| ID | Ce qu'elle appuie | Éditeur | Publication | Type | Niveau principal |
|---|---|---|---|---|---|
| [R-004] | Couverture du bureau de crédit (25 % des adultes) | BCEAO | 2026-07 | primaire | prouvé |
| [R-013] | Comptes mobile money au Bénin (axe A) | Banque mondiale | 2025 | primaire | prouvé |
| [R-018] | Données d'utilisation MoMo dans les conditions de Prêt Xpress | MTN Bénin | 2025-10 | primaire | indice |
| [R-033] | Sous-traitance bancaire (axe B) | Commission bancaire de l'UMOA | 2017-09 | primaire | prouvé (axe B) |
| [R-048] | Instruction 001-01-2024 : agrégateurs, interface, sans contrat, limite d'usage | BCEAO | 2024-01 | primaire | prouvé |
| [R-052] | Loi uniforme sur les bureaux de crédit | BCEAO | 2013-06 | primaire | indice (mots-clés) |
| [R-057] | Modification de la loi béninoise sur le bureau de crédit (2020) | Financial Afrik | 2020-06 | secondaire | indice |
| [R-059] | Secret bancaire et prestataires (axe B) | République du Bénin | 2024-09 | primaire | prouvé (axe B) |
| [R-118] | Analyse de relevés M-Pesa (Kenya) | Prembly | inconnue | primaire | prouvé |
| [R-119] | Score sur relevés PDF (Kenya) | Creditinfo Kenya | inconnue | primaire | prouvé |
| [R-125] | Score CIP lancé en 2018 | Financial Afrik (tribune Creditinfo) | 2020-07 | primaire | prouvé |
| [R-154] | Contenu du rapport de solvabilité (FAQ archivée) | Creditinfo West Africa | 2025-11 | primaire | prouvé |
| [R-155] | Rapport Creditinfo Plus | Creditinfo West Africa | 2022-07 | primaire | prouvé |
| [R-156] | Creditinfo Predictor (250-900, A-E, motifs) | Creditinfo West Africa | 2022-07 | primaire | prouvé |
| [R-157] | Rapport en tableau de bord | Creditinfo West Africa | 2022-07 | primaire | prouvé |
| [R-158] | HelloCreditinfo par WhatsApp | Creditinfo West Africa | 2024-07 | primaire | prouvé |
| [R-159] | Formulaire de demande de rapport (2025) | Creditinfo West Africa | 2025-10 | primaire | prouvé |
| [R-160] | Trois points à vérifier dans son rapport | Trésor public du Bénin | inconnue | primaire | prouvé |
| [R-161] | Correction des erreurs | Trésor public du Bénin | inconnue | primaire | prouvé |
| [R-162] | Modèle de rapport (2018, plus en ligne) | Creditinfo VoLo | 2018-02 | primaire | prouvé (existence) |
| [R-163] | Transmission mensuelle des données à la BCEAO | BCEAO | 2015-05 | primaire | prouvé |
| [R-164] | Accès au rapport (Burkina Faso) | UBA Burkina Faso | 2019-10 | primaire | prouvé |
| [R-165] | Établissements de paiement agréés au 31/08/2026 | BCEAO | 2026-10 | primaire | prouvé |
| [R-166] | Émetteurs de monnaie électronique et établissements de paiement au 29/06/2026 | Commission bancaire de l'UMOA | 2026-06 | primaire | prouvé |
| [R-167] | Établissements agréés au Bénin (2026) | BCEAO | 2026-06 | primaire | prouvé |
| [R-168] | Connexion au PI-SPI (02/04/2026) | BCEAO | 2026-04 | primaire | prouvé |
| [R-169] | Lancement du PI-SPI | BCEAO | 2025-09 | primaire | prouvé |
| [R-170] | Homologation des API Business, liste | BCEAO | 2026-09 | primaire | prouvé |
| [R-171] | Participants PI-SPI au 13/11/2025 | BCEAO | 2025-11 | primaire | prouvé |
| [R-172] | 175 participants au 30/09/2026 | Financial Afrik | 2026-10 | secondaire | indice |
| [R-173] | ISO 20022 pour le PI-SPI | AllAfrica | 2025-09 | secondaire | indice |
| [R-174] | Enregistrement des agrégateurs (analyse) | Cabinet Houda | 2024 | secondaire | prouvé |
| [R-175] | Analyse de l'Instruction 001-01-2024 (consentement explicite, art. 30) | Droit Médias Finance | 2024-02 | secondaire | prouvé (partiel) |
| [R-176] | Application MyMTN BN | SPACETEL BENIN (App Store) | 2026-10 | primaire | prouvé |
| [R-177] | Application Moov Money BJ | Moov Africa Bénin (App Store) | 2026-07 | primaire | prouvé |
| [R-178] | MTN MoMo adopte le PI-SPI | Bénin Web TV | 2025 ou 2026 | secondaire | contesté |
| [R-179] | Celtiis, super-application waa | Bénin Web TV | inconnue | secondaire | indice |
| [R-180] | Ecobank et Celtiis Cash | La Nouvelle Tribune | 2026-02 | secondaire | indice |
| [R-181] | Observatoire des services financiers mobiles (T3 2025) | ARCEP Bénin | 2025-12 | primaire | indice (non lu) |
| [R-182] | Relevés M-Pesa protégés par mot de passe | People Daily | inconnue | secondaire | indice |
| [R-183] | Chute d'Okra | NextBillion | 2025-07 | secondaire | indice |
| [R-184] | Account Aggregator (Inde) | Sahamati | 2026-01 | secondaire | indice |
| [R-185] | Politique de confidentialité MTN MoMo (page) | MTN Mobile Money Bénin | inconnue | primaire | prouvé (PDF en 404) |
| [R-186] | Politique de confidentialité MTN Bénin | MTN Bénin | inconnue | primaire | prouvé |
| [R-187] | Forum MoMo (section Ouganda) : API d'historique sans réponse | MTN MoMo Developer Community | 2026-03 | secondaire | prouvé |
| [R-188] | Forum MoMo : mise en production au Bénin | MTN MoMo Developer Community | inconnue | secondaire | indice |
| [R-189] | Portail MoMo Developer : produits | MTN Group | inconnue | primaire | prouvé |
| [R-190] | Conditions Moov Money (Côte d'Ivoire) | Moov Africa Côte d'Ivoire | 2025-12 | primaire | repérée |
| [R-191] | Conditions des offres mobiles Celtiis | SBIN / Celtiis | inconnue | primaire | indice |
| [R-192] | Plafonds de monnaie électronique (Instruction n°020) | BCEAO | 2026-10 | primaire | prouvé |
| [R-193] | Plafond porté à 4 M FCFA | Financial Afrik | 2026-10 | secondaire | indice |
| [R-194] | Usage du téléphone et remboursement | World Bank Economic Review (Björkegren, Grissen) | 2020-10 | primaire | prouvé |
| [R-195] | FairLend-Africa | Zenodo | 2026-06 | secondaire | indice |
| [R-196] | Fraudes M-Pesa | The Star (Kenya) | 2025-03 | secondaire | indice |
| [R-197] | Fausses offres de prêt | Africa Check | inconnue | secondaire | indice |
| [R-198] | Faux documents fabriqués par IA | Streamline Newsroom (Kenya) | 2026-06 | secondaire | prouvé (source faible) |
| [R-199] | Partage de téléphone au Togo | arXiv (Aiken, Thakur, Blumenstock) | 2021-10 | primaire | prouvé |
| [R-200] | Données télécoms et inclusion financière | UIT (FIGI) | 2021 | primaire | indice |
| [R-201] | Économie sans espèces au Bénin | FinDev Gateway | 2025-01 | secondaire | indice |
| [R-202] | Variable Findex 2025 sur le mobile money (Bénin) | Banque mondiale | 2025 | primaire | indice |
| [R-203] | Réconciliation multi-portefeuilles au Bénin | Kolonell | 2026-08 | secondaire | prouvé (absence d'information) |
| [R-204] | Historique MTN MoMo au Congo (mini-relevé) | iambeezy | inconnue | secondaire | indice |
| [R-205] | Une seule API Business au Bénin | Bénin Web TV | 2026-11 | secondaire | prouvé |
| [R-206] | Échéances PI-SPI repoussées | Financial Afrik | 2026-06 | secondaire | indice |
| [R-207] | Mise en conformité prorogée à mai 2025 | Droit Médias Finance | 2025 | secondaire | indice |
| [R-208] | ANIP : couverture, NPI et SIM, eKYC | ANIP Bénin (ID4Africa) | 2026-05 | primaire | prouvé |
| [R-209] | ANIP : plateforme d'interopérabilité | ANIP Bénin (ID4Africa) | 2026-05 | primaire | prouvé |
| [R-210] | Système d'identification au Bénin | Banque mondiale | 2026-05 | secondaire | prouvé |
| [R-211] | Décret du 22/04/2020 sur l'identification des utilisateurs | République du Bénin (ARCEP) | 2020-04 | primaire | prouvé |
| [R-212] | Décret 2016-465 (abrogé) | République du Bénin (SGG) | 2016-08 | primaire | prouvé |
| [R-213] | Cartes SIM non enregistrées désactivées (2025) | Osiris | 2025-03 | secondaire | indice |
| [R-214] | Mise en garde aux distributeurs de SIM | Osiris | inconnue | secondaire | indice |
| [R-215] | NINAuth (Nigeria) | Nairametrics | 2025-07 | secondaire | indice |
| [R-216] | Vérification BVN et NIN (Nigeria) | Youverify | 2026 | secondaire | indice |
| [R-217] | BVN au Nigeria | Legit.ng | inconnue | secondaire | indice |
| [R-218] | Mobile money au Bénin | TechCabal | 2021-11 | secondaire | indice |
| [R-219] | Financial Inclusion in Africa | Zindi | inconnue | primaire | prouvé |
| [R-220] | Règles des compétitions | Zindi | inconnue | primaire | prouvé |
| [R-221] | African Credit Scoring Challenge | Zindi | 2024-11 | primaire | prouvé |
| [R-222] | Conditions d'utilisation de la Microdata Library | Banque mondiale | inconnue | primaire | prouvé |
| [R-223] | Global Findex 2021 | Banque mondiale | 2022-06 | primaire | prouvé |
| [R-224] | EHCVM Bénin 2021-2022 | Banque mondiale (Data Catalog) | 2026-06 | primaire | prouvé |
| [R-225] | Licences publiques de la Banque mondiale | Banque mondiale (Data Catalog) | inconnue | primaire | prouvé |
| [R-226] | German Credit | UCI | 1994-11 | primaire | prouvé |
| [R-227] | Règles de Home Credit | Kaggle | inconnue | primaire | non lisible |
| [R-228] | Données Kiva | Kiva | inconnue | primaire | indice |
| [R-229] | Licence du Findex 2021 (fiche d'un pays) | Banque mondiale (Data Catalog) | 2026-06 | primaire | prouvé |
| [R-230] | Findex 2025, fichier Bénin | Banque mondiale | 2025-12 | primaire | prouvé |
| [R-231] | Xente Credit Scoring Challenge | Zindi | inconnue | primaire | prouvé |
| [R-232] | IndabaX Zimbabwe 2026 | Zindi | 2026-05 | primaire | prouvé |
| [R-233] | Guide du candidat au LIF-BCEAO | BCEAO | inconnue | primaire | prouvé |
| [R-234] | Diffusion tabulaire contrainte pour la finance | arXiv | 2026-06 | primaire | prouvé (résumé) |
| [R-235] | Credit reporting without borders | Banque mondiale | 2019-03 | primaire | indice |
| [R-236] | MyMoov : « relevés de toutes ses transactions » | App Store (éditeur non lu) | inconnue | primaire | indice (non ouverte) |

---

## 13. Dates de revérification

Seuils de fraîcheur de la méthode : fonctions d'un produit, 1 mois ; signaux de l'écosystème, 6 mois ; paysage, 12 mois ; pratiques et textes, 2 ans.

| Affirmation clé | À revérifier le |
|---|---|
| Fonctions des applications MoMo, Moov, Celtiis (absence d'export) | **déjà dépassé** : ce sont les tests T1 à T4 |
| Absence d'API MoMo d'historique pour un tiers | **déjà dépassé** (question écrite n°2) |
| Service de vérification d'identité de l'ANIP | **déjà dépassé** (question écrite n°3) |
| Contenu du rapport du bureau de crédit (FAQ archivée en 2025) | **déjà dépassé** : c'est le test T8 |
| Partage de téléphone au Togo (étude de 2021) | **déjà dépassé** (pratique) |
| Instruction 001-01-2024 (agrégateurs, art. 60, 63) | **déjà dépassé** au sens de la méthode ; texte toujours cité par les listes de 2026, mais vigueur et textes d'application à revérifier (question écrite n°1) |
| PI-SPI : API Business, une seule au Bénin | 01/12/2026 |
| Registre des établissements de paiement | 01/04/2027 |
| Licences des jeux de données | 01/06/2027 |

**Conclusion** : presque toutes les conclusions de faisabilité portent sur des fonctions qui changent vite. Les **tests de la section 10** et les **questions écrites de la section 11** sont les revérifications prioritaires.

---

## 14. Termes proposés pour le glossaire

Ces termes sont à ajouter au [glossaire](../../GLOSSAIRE.md) après validation par Daniela. Le glossaire n'a pas été modifié.

| Terme | Définition proposée | Sens à distinguer | Source |
|---|---|---|---|
| Agrégateur de comptes | Prestataire qui, avec le consentement explicite du client, consolide sur une seule interface les informations de ses comptes tenus chez plusieurs prestataires de paiement ; dans l'UMOA, il est **enregistré** par la BCEAO, et non agréé, quand il ne fait que cela | À distinguer de l'agrégateur de **paiements** (encaissement multi-opérateurs) | [R-048], [R-174] |
| Interface d'accès aux comptes (art. 60) | Interface sécurisée que les gestionnaires de comptes en ligne doivent fournir aux agrégateurs, sans contrat préalable (art. 63) | Aucune norme technique publiée au 22/11/2026 | [R-048] |
| PI-SPI | Plateforme interopérable du système de paiement instantané de la BCEAO, lancée le 30/09/2025, qui relie banques, IMF et émetteurs de monnaie électronique | Interopérabilité des paiements, pas accès aux données | [R-169], [R-168] |
| API Business (PI-SPI) | Interface homologuée par la BCEAO qu'un participant au PI-SPI offre à ses entreprises clientes pour payer, encaisser et suivre leurs propres transactions | Ne donne pas accès aux flux des particuliers | [R-170] |
| Établissement de paiement (EP) | Établissement agréé par la BCEAO pour fournir des services de paiement ; 34 dans l'UMOA, dont 4 au Bénin, au 31/08/2026 | À distinguer de l'émetteur de monnaie électronique | [R-165] |
| NPI (numéro personnel d'identification) | Identifiant unique attribué par l'ANIP à chaque personne inscrite au registre national ; recueilli et vérifié par l'opérateur à la souscription d'une ligne | Lien numéro ↔ NPI conservé par l'opérateur, non communicable à un tiers privé | [R-211], [R-208] |
| RNPP | Registre national des personnes physiques, tenu par l'ANIP (13,8 M d'inscrits en 2026) | | [R-208] |
| eKYC | Vérification d'identité en ligne auprès du registre national ; au Bénin, 25 M (ou 27 M selon les présentations) de vérifications en 2025, ouverture payante aux acteurs privés annoncée pour 2027 | | [R-208], [R-209] |
| Creditinfo Predictor | Score du bureau de crédit de l'UEMOA, de 250 à 900, avec une classe de risque de A à E et des codes de motif | Probablement le même produit que le « Score CIP » de 2018 (non vérifié) | [R-156] |
| Relevé apporté par le client | Historique de transactions (mobile money ou bancaire) que le client obtient lui-même et transmet, avec son consentement, à un prêteur | À distinguer de l'accès par agrégateur (non falsifiable) et de la donnée de l'opérateur | [R-182], [R-048] |
| Partage de téléphone | Usage d'une même carte SIM ou d'un même téléphone par plusieurs personnes ; 22 % des SIM au Togo selon une étude de 2021 | Un historique de numéro peut mélanger plusieurs personnes | [R-199] |
| LIF-BCEAO | Laboratoire d'innovation financière de la BCEAO : bac à sable de 3 à 6 mois, prorogeable jusqu'à 2 ans, ouvert aux fintechs, qui couvre le scoring de crédit | Ne fournit pas de données | [R-233] |
| Licence de recherche (Microdata) | Licence de la Banque mondiale qui limite l'usage à la recherche statistique et scientifique, sans redistribution ni vente | S'oppose à l'« accès ouvert » (usage commercial permis) | [R-225], [R-222] |
| Données synthétiques | Données artificielles générées pour reproduire des statistiques connues | Servent à démontrer et tester, pas à valider une performance | [R-234] |
