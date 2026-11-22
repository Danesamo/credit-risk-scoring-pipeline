# RT-1 : contre-expertise (red team) sur les voies d'accès aux données

- Date : 2026-11-22
- Rôle : contradicteur indépendant. Mandat : chercher de bonne foi les preuves que les conclusions sont fausses, en priorité la voie 2.
- Budget utilisé : 20 appels d'outils (1 chargement d'outils, 18 recherches ou lectures de pages, 1 écriture). 11 appels portaient sur la conclusion 1.
- Niveaux : **prouvé** = lu sur la page ouverte ; **indice** = extrait de moteur de recherche ou source faible ; **déduit** = raisonnement à partir d'éléments trouvés.
- Limite importante : plusieurs éléments viennent seulement des extraits renvoyés par le moteur de recherche (niveau indice). Ils servent de pistes à vérifier, pas de preuves.

---

## Conclusion 1 : voie 2 praticable (relevé mobile money ou bancaire apporté par le client)

### Verdict : affaiblie

Rien de ce que j'ai trouvé ne montre qu'il est **impossible** d'obtenir un relevé. Mais je n'ai trouvé **aucune** source publique qui décrive, pour le Bénin, une procédure permettant d'obtenir un historique de plusieurs mois dans un format lisible par une machine. Le seul accès documenté côté client est un mini-relevé de quelques opérations. Et plusieurs éléments vont contre la fiabilité et la représentativité d'un tel relevé.

### Éléments contraires

1. 
   - element : Par USSD, l'historique MTN MoMo se limite à un « mini-relevé » des 5 à 10 dernières opérations. Pour aller plus loin, il faut passer par l'application, sans format d'export décrit.
   - niveau : indice (extrait de moteur ; la page source porte sur MTN MoMo Congo, pas sur le Bénin)
   - source : https://blog.iambeezy.app/fr/historique-transferts-mtn-momo-congo/
   - titre : Historique des transferts MTN MoMo Congo
   - editeur : iambeezy (blog)
   - date_publication : inconnue
   - consulte : 2026-11-22
   - type : blog / guide utilisateur
   - confiance : faible (autre pays, source non officielle)

2. 
   - element : Le seul document en ligne sur l'export multi-portefeuilles au Bénin (MTN MoMo, Moov/Celtiis) parle de lire des « relevés existants », mais ne dit rien du format natif des opérateurs (CSV, PDF, SMS), de la profondeur d'historique ni d'un éventuel accès par API. Aucune documentation d'opérateur trouvée sur ce point.
   - niveau : prouvé (page ouverte ; le constat porte sur l'absence d'information)
   - source : https://kolonell.com/fr/blog/benin-reconciliation-multi-wallet-mtn-celtiis-export-compta-2026
   - titre : Bénin : réconciliation multi-wallet MTN / Celtiis, export compta 2026
   - editeur : Kolonell
   - date_publication : 2026-08
   - consulte : 2026-11-22
   - type : blog commercial
   - confiance : moyenne sur le constat d'absence, faible comme source générale

3. 
   - element : La politique de confidentialité MTN MoMo Bénin (V3), qui devrait décrire les droits d'accès et de portabilité, la durée de conservation et le partage avec des tiers, renvoie une erreur 404. Je n'ai donc pas pu vérifier les droits contractuels du client sur ses données.
   - niveau : prouvé (erreur 404 constatée)
   - source : https://www.mtn.bj/wp-content/uploads/2025/12/Politique%20de%20confidentialit%C3%A9%20MTN%20MOMO%20V3%20-%20signed.pdf
   - titre : Politique de confidentialité MTN MOMO V3 (signée)
   - editeur : MTN Bénin
   - date_publication : 2025-12 (d'après le chemin de l'URL)
   - consulte : 2026-11-22
   - type : document contractuel d'opérateur (inaccessible)
   - confiance : n/a (le document n'a pas pu être lu)

4. 
   - element : Au Kenya, l'écosystème du prêt s'appuie sur l'analyse des relevés M-Pesa en PDF, et des réseaux criminels utilisent l'IA générative pour fabriquer des relevés PDF « mathématiquement cohérents » qui trompent la vérification automatique. Les prêteurs y répondent en resserrant leurs critères et en passant à un accès direct en lecture par API.
   - niveau : prouvé (page ouverte), mais source de presse faible, et c'est le Kenya
   - source : https://streamlinefeed.co.ke/news/scammers-using-ai-create-fake-auto-loan-documents-defaults-rise
   - titre : Scammers using AI create fake auto loan documents as defaults rise
   - editeur : Streamline Newsroom (Kenya)
   - date_publication : 2026-06
   - consulte : 2026-11-22
   - type : presse en ligne
   - confiance : faible à moyenne (pas de chiffres de pertes vérifiables)

5. 
   - element : Sur 22 % des cartes SIM au Togo, l'usage observé correspond à plusieurs utilisateurs (7 % des emplacements SIM sont partagés). Le partage est plus fréquent chez les femmes, les jeunes et les ruraux, et il augmente avec les programmes de transferts par mobile money. Conséquence : l'historique d'un numéro ne correspond pas toujours à une seule personne.
   - niveau : prouvé (résumé de l'article ouvert) ; l'application au Bénin est **déduite** (pays voisin, même opérateur dominant)
   - source : https://arxiv.org/abs/2111.00175
   - titre : Phone Sharing and Cash Transfers in Togo: Quantitative Evidence from Mobile Phone Data
   - editeur : arXiv (Aiken, Thakur, Blumenstock)
   - date_publication : 2021-10
   - consulte : 2026-11-22
   - type : article scientifique (prépublication)
   - confiance : élevée pour le Togo, moyenne pour le Bénin

6. 
   - element : Les clients à faible revenu ont souvent plusieurs cartes SIM (promotions, appels moins chers vers d'autres réseaux) et partagent leur téléphone, ce qui limite l'utilité de ces données pour le scoring. Un modèle entraîné sur les données mobile money hérite structurellement de l'écart entre hommes et femmes : historiques plus minces, donc scores plus bas.
   - niveau : indice (synthèse d'extraits ; l'attribution exacte à l'une des pages listées n'est pas vérifiée)
   - source : https://www.itu.int/en/publications/Documents/tsb/2021-FIGI-Use-of-telecommunications-data-for-digital-financial-inclusion/files/basic-html/page25.html
   - titre : FIGI : Use of telecommunications data for digital financial inclusion (p. 25)
   - editeur : UIT (ITU), initiative FIGI
   - date_publication : 2021-01 (mois non vérifié)
   - consulte : 2026-11-22
   - type : rapport institutionnel
   - confiance : moyenne

7. 
   - element : L'argent liquide reste dominant au Bénin : depuis le 1er janvier 2025, les paiements en espèces de plus de 100 000 FCFA sont taxés à 1 % pour réduire « la part encore écrasante » du cash dans les échanges commerciaux. Un relevé mobile money ne verrait donc qu'une partie de l'activité d'un particulier ou d'une TPE.
   - niveau : indice (extrait de moteur)
   - source : https://www.findevgateway.org/fr/actualites/au-benin-lambition-dune-economie-cashless-pour-doper-les-recettes-fiscales
   - titre : Au Bénin, l'ambition d'une économie cashless pour doper les recettes fiscales
   - editeur : FinDev Gateway (CGAP)
   - date_publication : 2025-01 (probable, non vérifiée)
   - consulte : 2026-11-22
   - type : presse spécialisée (reprise)
   - confiance : moyenne

8. 
   - element : D'après la variable Global Findex 2025 (données Bénin 2024), environ 30,8 % des répondants déclarent avoir déjà eu un compte mobile money. Le dénominateur (92 sur 299) laisse penser à un sous-échantillon. Si ce chiffre se confirme, une grande partie de la population cible n'aurait aucun historique mobile money.
   - niveau : indice (extrait de moteur ; chiffre et dénominateur à vérifier sur la page)
   - source : https://microdata.worldbank.org/catalog/7872/variable/F1/V60?name=fin15
   - titre : Global Findex Database 2025, variable fin15
   - editeur : Banque mondiale, Microdata Library
   - date_publication : 2025 (mois inconnu)
   - consulte : 2026-11-22
   - type : base de données d'enquête
   - confiance : faible tant que le chiffre n'est pas vérifié

9. 
   - element : Okra, start-up nigériane d'open banking qui fournissait les données de revenus et de transactions aux prêteurs, a fermé en mai 2025 malgré plus de 16 M$ levés. Mono, son concurrent, a été racheté par Flutterwave. Le modèle économique de l'analyse de comptes pour le crédit reste fragile, même sur un grand marché.
   - niveau : indice (extraits de moteur)
   - source : https://nextbillion.net/news/inside-the-fall-of-okra-how-africas-most-promising-open-banking-startup-shut-down-at-its-peak
   - titre : Inside the fall of Okra: how Africa's most promising open banking startup shut down at its peak
   - editeur : NextBillion (reprise de Nairametrics)
   - date_publication : 2025-07
   - consulte : 2026-11-22
   - type : presse spécialisée
   - confiance : moyenne

### Meilleur argument contre

Au Bénin, aucune source publique ne décrit comment un client obtient un historique MoMo, Moov ou Celtiis de plusieurs mois dans un format lisible par une machine. Le seul accès documenté côté client est un mini-relevé de 5 à 10 opérations, et la politique de confidentialité de MTN MoMo, qui devrait encadrer ce droit, est hors ligne. Si le relevé passe par un PDF ou une capture remis par le client, l'expérience kényane montre que ce support se falsifie de façon industrielle. Enfin, le partage de téléphone (22 % des SIM au Togo), la multiplicité des SIM et la place dominante du cash font qu'un relevé décrit mal la capacité de remboursement d'une personne.

### Cherché sans trouver

- Procédure officielle MTN MoMo, Moov Money ou Celtiis Cash au Bénin pour demander un relevé de plusieurs mois (délai, frais, format) : rien trouvé, ni pour ni contre.
- Études qui mesurent le pouvoir prédictif des relevés apportés par le client (relevé « self-reported » contre données obtenues de l'opérateur) : non trouvées avec les requêtes faites.
- Interdiction contractuelle de partager ses données d'opérateur avec un tiers : document clé inaccessible (404), rien trouvé ailleurs.
- Cas documentés de prêteurs béninois ou de l'UEMOA trompés par de faux relevés mobile money : rien trouvé (seulement au Kenya et au Ghana, et surtout sur la fraude de paiement plutôt que sur les faux relevés).

---

## Conclusion 2 : accès consenti aux comptes par l'Instruction BCEAO n°001-01-2024

### Verdict : affaiblie (le texte existe, sa mise en œuvre n'est pas démontrée)

L'Instruction crée bien les services d'agrégation de comptes et d'information sur les comptes. Mais rien de ce que j'ai trouvé ne montre qu'un agrégateur soit agréé, qu'une banque ou un opérateur ait ouvert une interface, ou qu'une norme technique soit publiée.

### Éléments contraires

1. 
   - element : Au 31 août 2026, seuls 34 établissements de paiement sont agréés dans toute l'UMOA, dont 4 au Bénin. La page ne dit pas si l'un d'eux est agréé pour l'agrégation de comptes ou l'information sur les comptes, et le PDF détaillé n'a pas pu être lu.
   - niveau : prouvé (chiffres lus) ; l'absence d'agrégateur n'est **pas** établie
   - source : https://www.bceao.int/index.php/fr/communique-presse/liste-des-etablissements-de-paiement-agrees-dans-lumoa-au-31-aout-2026
   - titre : Liste des établissements de paiement agréés dans l'UMOA au 31 août 2026
   - editeur : BCEAO
   - date_publication : 2026-10 (date du PDF dans l'URL)
   - consulte : 2026-11-22
   - type : communiqué du régulateur
   - confiance : élevée sur les chiffres

2. 
   - element : La période de mise en conformité a été repoussée plusieurs fois : de juillet 2024 à janvier 2025, puis à mai 2025. Cela montre que le régime se met en place lentement.
   - niveau : indice (titres et extraits)
   - source : https://droitmediasfinance.com/index.php/actualites/droit-tech-fintech/956-uemoa-services-de-paiement-la-bceao-proroge-la-periode-de-mise-en-conformite-a-mai-2025
   - titre : UEMOA, services de paiement : la BCEAO proroge la période de mise en conformité à mai 2025
   - editeur : Droit Médias Finance
   - date_publication : 2025 (mois non vérifié)
   - consulte : 2026-11-22
   - type : presse juridique
   - confiance : moyenne

3. 
   - element : Une tribune critique la réglementation de la BCEAO sur les fintechs, la jugeant « hors sol ». Je n'ai vu que le titre, pas le contenu.
   - niveau : indice (titre seul)
   - source : https://www.osiris.sn/une-reglementation-hors-sol-quand-la-bceao-compromet-l-avenir-de-l-economie.html
   - titre : Une réglementation hors sol : quand la BCEAO compromet l'avenir de l'économie
   - editeur : Osiris (Sénégal)
   - date_publication : inconnue
   - consulte : 2026-11-22
   - type : tribune
   - confiance : faible

4. 
   - element : Le seul acteur d'open banking dont j'ai trouvé un retour d'expérience africain (Okra, Nigeria) a fermé en 2025 (voir conclusion 1, élément 9).
   - niveau : indice
   - source : https://nextbillion.net/news/inside-the-fall-of-okra-how-africas-most-promising-open-banking-startup-shut-down-at-its-peak
   - titre : Inside the fall of Okra
   - editeur : NextBillion
   - date_publication : 2025-07
   - consulte : 2026-11-22
   - type : presse spécialisée
   - confiance : moyenne

### Meilleur argument contre

Le droit d'accès consenti n'est opposable que s'il existe un agrégateur agréé et une interface ouverte par le teneur de compte. Or, sur 34 établissements de paiement agréés dans toute l'UMOA (4 au Bénin), aucune source consultée ne mentionne d'agrégateur, d'interface ouverte ou de norme technique d'interface. La voie réglementaire existe sur le papier mais n'est pas démontrée en pratique au Bénin en novembre 2026.

### Cherché sans trouver

- Exclusion explicite des comptes de monnaie électronique du périmètre de l'agrégation : non vérifiée (texte de l'Instruction non ouvert, faute de budget).
- Norme technique d'interface publiée par la BCEAO pour l'agrégation : rien trouvé.
- Exemple d'agrégateur de comptes agréé dans l'UMOA : non déterminé (PDF illisible par l'outil ; une copie est enregistrée localement dans `tool-results/webfetch-1795350402174-y47eyk.pdf` de la session, à relire).
- Le passage « sans contrat nécessaire » n'a pas été vérifié dans le texte.

---

## Conclusion 3 : rattachement du numéro de téléphone à la personne via le NPI

### Verdict : affaiblie

Le lien SIM ↔ NPI est bien imposé par la réglementation. Mais les campagnes répétées contre les lignes non identifiées et les mises en garde aux distributeurs indiquent que l'identification n'est pas fiable. Et le partage des téléphones casse le lien entre un numéro et une seule personne.

### Éléments contraires

1. 
   - element : Le Procureur spécial de la CRIET a mis en garde les distributeurs de cartes SIM sur leur obligation d'identifier les abonnés, et la justice « relance la chasse ». Ces annonces suggèrent que des SIM ont été vendues sans identification ou au nom de tiers.
   - niveau : indice (titres et extraits)
   - source : https://www.osiris.sn/Benin-La-Justice-relance-la-chasse.html
   - titre : Bénin : la Justice relance la chasse (identification des SIM)
   - editeur : Osiris
   - date_publication : inconnue
   - consulte : 2026-11-22
   - type : presse
   - confiance : faible à moyenne

2. 
   - element : En 2025, l'ARCEP Bénin a dû fixer des échéances successives (mise en réception au 31 mars, coupure au 30 avril 2025) pour les abonnés non identifiés. En 2025, la base contenait donc encore des lignes sans identification à jour.
   - niveau : indice (extraits de moteur)
   - source : https://www.osiris.sn/benin-les-cartes-sim-non-enregistrees-seront-desactivees-des-le-30-avril-2025.html
   - titre : Bénin : les cartes SIM non enregistrées seront désactivées dès le 30 avril 2025
   - editeur : Osiris
   - date_publication : 2025-03 (probable)
   - consulte : 2026-11-22
   - type : presse
   - confiance : moyenne

3. 
   - element : 22 % des SIM sont partagées au Togo (voir conclusion 1, élément 5). Même avec un NPI exact, le titulaire de la ligne n'est pas forcément la personne qui fait les opérations.
   - niveau : prouvé pour le Togo, déduit pour le Bénin
   - source : https://arxiv.org/abs/2111.00175
   - titre : Phone Sharing and Cash Transfers in Togo
   - editeur : arXiv
   - date_publication : 2021-10
   - consulte : 2026-11-22
   - type : article scientifique
   - confiance : moyenne pour le Bénin

### Meilleur argument contre

Le NPI garantit qu'une ligne a été enregistrée au nom de quelqu'un, pas que cette personne est celle qui utilise le portefeuille. Les mises en garde judiciaires aux distributeurs et les coupures de 2025 montrent que l'identification à la vente a eu des failles. Le partage des téléphones, documenté à grande échelle au Togo voisin, mélange les historiques de plusieurs personnes.

### Cherché sans trouver

- Moyen pour un tiers privé (banque, prestataire) de vérifier le lien numéro ↔ NPI : pas cherché spécifiquement, faute de budget.
- Couverture réelle du NPI par sexe ou par zone : pas cherchée.
- Incidents de qualité dans le registre : rien de précis trouvé.

---

## Conclusion 4 : voie 3, flux PI-SPI via l'API Business

### Verdict : affaiblie (presque contredite pour les particuliers)

### Éléments contraires

1. 
   - element : Au 12 novembre 2026, une seule API Business est homologuée au Bénin (Ecobank), contre 34 dans l'UEMOA. L'API Business permet aux **entreprises clientes** d'un établissement de relier leur logiciel de trésorerie ou de facturation à PI-SPI pour payer, encaisser et « suivre les mouvements financiers depuis leurs propres outils ». Ce n'est pas un accès aux flux des particuliers pour un tiers.
   - niveau : prouvé
   - source : https://beninwebtv.bj/pi-spi-34-api-homologuees-dans-luemoa-toujours-une-seule-au-benin/
   - titre : PI-SPI : 34 API homologuées dans l'UEMOA, toujours une seule au Bénin
   - editeur : Bénin Web TV
   - date_publication : 2026-11
   - consulte : 2026-11-22
   - type : presse
   - confiance : élevée

2. 
   - element : La BCEAO a repoussé les échéances de connexion à PI-SPI, et MTN MoMo Bénin n'a basculé ses opérations interopérables sur PI-SPI que le 2 novembre 2026, avec un tarif de 0,5 % au-delà d'un seuil gratuit. L'historique PI-SPI disponible au Bénin est donc de quelques semaines au plus.
   - niveau : indice (titres et extraits)
   - source : https://beninwebtv.bj/benin-mtn-momo-adopte-le-systeme-pi-spi-de-la-bceao-des-le-2-novembre-avec-de-nouveaux-plafonds-et-une-grille-tarifaire-revisee/
   - titre : Bénin : MTN MoMo adopte le système PI-SPI de la BCEAO dès le 2 novembre
   - editeur : Bénin Web TV
   - date_publication : 2026-10 ou 2026-11 (non vérifiée)
   - consulte : 2026-11-22
   - type : presse
   - confiance : moyenne

3. 
   - element : La BCEAO a repoussé les échéances de connexion des participants à PI-SPI.
   - niveau : indice (titre)
   - source : https://www.financialafrik.com/2026/06/25/breaking-news-uemoa-la-bceao-repousse-les-echeances-de-connexion-au-systeme-de-paiement-instantane-pi-spi/
   - titre : UEMOA : la BCEAO repousse les échéances de connexion au système de paiement instantané PI-SPI
   - editeur : Financial Afrik
   - date_publication : 2026-06
   - consulte : 2026-11-22
   - type : presse
   - confiance : moyenne

### Meilleur argument contre

L'API Business sert à une entreprise cliente pour piloter ses propres paiements. Elle ne donne pas à un prestataire de scoring l'historique des particuliers. Au Bénin, une seule est homologuée (Ecobank), et la bascule de MTN MoMo sur PI-SPI date du 2 novembre 2026 : il n'existe pas encore d'historique de plusieurs mois. Au mieux, la voie 3 couvre la TPE cliente d'Ecobank qui donne elle-même accès à ses flux récents.

### Cherché sans trouver

- Volumes de transactions PI-SPI au Bénin : non trouvés.
- Conditions contractuelles d'accès à l'API Business d'Ecobank pour un tiers : non cherchées (budget).

---

## Conclusion 5 : voie 1, données internes de la banque et rapport du bureau de crédit

### Verdict : tient (avec réserves)

Je n'ai trouvé aucune interdiction de transmettre le rapport du bureau de crédit à un sous-traitant. Les réserves portent sur la couverture et la qualité.

### Éléments contraires

1. 
   - element : Le BIC régional (Creditinfo VoLo) a rassemblé environ 5,5 millions de personnes et entreprises sur 8 pays en trois ans. La couverture y est jugée « améliorable », et la difficulté à obtenir le consentement pour partager l'historique antérieur à 2017 a été un blocage majeur.
   - niveau : indice (extrait de moteur)
   - source : https://documents1.worldbank.org/curated/en/482141547662326461/pdf/133786-Credit-reporting-without-borders-Final.pdf
   - titre : Credit reporting without borders
   - editeur : Banque mondiale
   - date_publication : 2019-03
   - consulte : 2026-11-22
   - type : rapport institutionnel
   - confiance : moyenne (chiffres anciens)

2. 
   - element : La loi béninoise sur le BIC a été modifiée en 2020. La nature de la modification (consentement, accès des tiers) n'a pas été lue.
   - niveau : indice (titre seul)
   - source : https://www.financialafrik.com/2020/06/26/benin-importante-modification-de-la-loi-relative-au-bureau-dinformation-sur-le-credit-bic/
   - titre : Bénin : importante modification de la loi relative au bureau d'information sur le crédit (BIC)
   - editeur : Financial Afrik
   - date_publication : 2020-06
   - consulte : 2026-11-22
   - type : presse
   - confiance : faible (contenu non lu)

### Meilleur argument contre

Le bureau de crédit couvre surtout les personnes et entreprises qui ont déjà emprunté auprès d'institutions formelles, et il a été freiné par les problèmes de consentement. Pour la population ciblée (particuliers et TPE peu bancarisés), le rapport sera souvent vide. Les données internes de la banque ne couvrent par définition que ses propres clients.

### Cherché sans trouver

- Interdiction légale ou contractuelle de transmettre le rapport BIC à un prestataire technique : rien trouvé (loi uniforme BIC non ouverte).
- Études sur la qualité et la complétude des données internes des banques de l'UEMOA : pas cherchées, faute de budget.

---

## Synthèse pour l'équipe

| Conclusion | Verdict | Point le plus fragile |
|---|---|---|
| 1. Voie 2 (relevé apporté par le client) | affaiblie | Aucune procédure d'export documentée au Bénin ; relevés PDF falsifiables ; partage de téléphones et cash dominant |
| 2. Agrégation de comptes BCEAO | affaiblie | Aucun agrégateur agréé ni interface ouverte trouvés |
| 3. Lien SIM ↔ NPI | affaiblie | Failles d'identification à la vente ; SIM partagées |
| 4. Voie 3 PI-SPI / API Business | affaiblie (presque contredite pour les particuliers) | Une seule API au Bénin, réservée aux entreprises clientes ; historique de quelques semaines |
| 5. Voie 1 données bancaires + BIC | tient, avec réserves | Couverture du BIC pour la population ciblée |

Vérifications prioritaires à faire (non couvertes par ce budget) : lire le PDF BCEAO des établissements agréés pour repérer un éventuel agrégateur ; obtenir la politique de confidentialité et les conditions générales MoMo Bénin à jour ; tester sur un vrai compte la profondeur et le format du relevé dans l'application MoMo et chez Moov/Celtiis ; vérifier le chiffre Findex 2025 sur la détention de comptes mobile money au Bénin.
