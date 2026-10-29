# RT-1 : Contre-expertise (red team) des conclusions Q21 sur les outils de scoring UEMOA

- Date : 2026-10-29
- Mandat : chercher de bonne foi ce qui contredit ou affaiblit les 4 conclusions. Les preuves de l'équipe n'ont pas été consultées.
- Budget : 20 appels d'outils (14 recherches ou lectures web, 1 écriture). Pages ouvertes : senego.com (Orange Bank), osiris.sn (x2), score360.africa, xloan.open.global, fr.allafrica.com. Le reste vient des extraits des moteurs de recherche, ce qui est signalé dans le niveau.
- Niveaux : **prouvé** = lu sur la page ouverte ; **indice** = extrait de recherche ou source non primaire non ouverte ; **déduit** = raisonnement à partir des éléments.

---

## Conclusion 1 : les banques classiques ne documentent aucun scoring statistique particuliers/TPE

### Verdict : affaiblie

L'énoncé tient peut-être au sens strict de « banque classique », mais une banque agréée de la zone accorde à grande échelle des prêts instantanés via une application, avec un outil de scoring revendiqué. Le périmètre « banques classiques » doit donc être défini explicitement, sinon la conclusion est fausse.

### Éléments contraires

1. 
   - element : Orange Bank Africa (banque agréée UMOA, Côte d'Ivoire puis succursale au Sénégal) accorde le microcrédit « Tik Tak » depuis l'interface Orange Money, « jusqu'à 1 million de francs CFA en quelques secondes » ; 640 milliards FCFA octroyés depuis juillet 2020 ; 3 millions de clients (80 % CI) ; 37 % des clients actifs utilisent le crédit.
   - niveau : prouvé
   - source : https://senego.com/pour-atteindre-3-millions-de-clients-au-senegal-et-en-cote-divoire-orange-bank-a-mise-sur-un-service-de-pret-express_1930453.html
   - titre : Pour atteindre 3 millions de clients au Sénégal et en Côte d'Ivoire, Orange Bank a misé sur un service de prêt express
   - editeur : Senego (reprend Sud Quotidien)
   - date_publication : 2026-02
   - consulte : 2026-10-29
   - type : presse
   - confiance : moyenne-haute (chiffres concordants avec d'autres titres : allafrica 2026-02, digitalmag.ci)
2. 
   - element : la capacité de prêt d'Orange Bank Africa « repose sur un outil de scoring qui évalue le risque en temps réel » à partir des données d'usage Orange et Orange Money ; gestion du risque par « data mining, scoring, algorithmes ».
   - niveau : indice (extraits de moteur de recherche, page non ouverte ; l'article osiris.sn ouvert du 2025-07 ne détaille pas le modèle)
   - source : https://osiris.sn/orange-est-devenu-une-banque-africaine-credit-epargne-carte-bancaire.html
   - titre : Orange est devenu une banque africaine : crédit, épargne, carte bancaire
   - editeur : Osiris (repris de la presse)
   - date_publication : 2020-07 (selon la reprise algerie-eco.com du 27/07/2020)
   - consulte : 2026-10-29
   - type : presse
   - confiance : moyenne
3. 
   - element : Orange Bank Africa a reçu l'autorisation de la Commission bancaire de l'UMOA pour une succursale au Sénégal (crédit instantané de 5 000 à 1 000 000 FCFA aux clients Orange Money).
   - niveau : indice (extrait de recherche)
   - source : https://droitmediasfinance.com/index.php/actualites/droit-tech-fintech/615-senegal-orange-bank-africa-oba-recoit-lautorisation-douvrir-une-succursale-senegalaise
   - titre : SENEGAL : Orange Bank Africa (OBA) reçoit l'autorisation d'ouvrir une succursale sénégalaise
   - editeur : Droit Medias Finance
   - date_publication : 2023-10 (date d'autorisation citée)
   - consulte : 2026-10-29
   - type : presse spécialisée
   - confiance : moyenne
4. 
   - element : Ecobank (présent au Bénin, en CI, au Sénégal) propose « Xpress Loan / Prêt Xpress », microcrédit court terme instantané sur mobile. Disponibilité pays par pays dans l'UEMOA non vérifiée.
   - niveau : indice faible (synthèse du moteur de recherche, aucune page primaire ouverte)
   - source : https://fr.allafrica.com/stories/201804030921.html
   - titre : L'appli Ecobank Mobile franchit le seuil des 4 millions d'utilisateurs
   - editeur : AllAfrica (communiqué Ecobank)
   - date_publication : 2018-04
   - consulte : 2026-10-29
   - type : communiqué repris
   - confiance : faible
5. 
   - element : l'IFC a financé des projets « psychometric scoring for MSME access to finance » en Côte d'Ivoire et au Sénégal/UEMOA, avec des IMF partenaires ; la Banque mondiale a lancé une étude sur l'adoption du scoring psychométrique par les prêteurs en CI et UEMOA.
   - niveau : indice (titres de fiches IFC / BM, non ouvertes ; partenaires = IMF, pas banques)
   - source : https://disclosures.ifc.org/project-detail/AS/607192/cote-d-ivoire-psychometric-scoring-for-msme-a2f
   - titre : Côte d'Ivoire Psychometric Scoring for MSME A2F
   - editeur : IFC
   - date_publication : inconnue
   - consulte : 2026-10-29
   - type : institution (fiche projet)
   - confiance : moyenne sur l'existence, faible sur l'usage bancaire
6. 
   - element : Creditinfo West Africa vend aux assujettis, en plus des rapports, « des produits à valeur ajoutée comme le scoring et autres innovations analytiques ». Les banques peuvent donc consommer un score statistique sans le documenter elles-mêmes.
   - niveau : indice (extrait de recherche sur documents Creditinfo)
   - source : https://uemoa.creditinfo.com/wp-content/uploads/sites/63/2024/12/GT-2025-vf.pdf
   - titre : GT 2025 (grille tarifaire Creditinfo UEMOA)
   - editeur : Creditinfo West Africa
   - date_publication : 2024-12
   - consulte : 2026-10-29
   - type : document éditeur
   - confiance : moyenne

### Meilleur argument contre

Une banque agréée UMOA (Orange Bank Africa) note et prête en quelques secondes à des millions de clients particuliers en Côte d'Ivoire et au Sénégal, sur une application, avec un scoring revendiqué publiquement : l'affirmation « aucune banque ne documente de scoring statistique » est fausse si l'on ne restreint pas explicitement le périmètre aux banques « classiques » hors filiales d'opérateurs. Par ailleurs, l'absence de documentation publique ne prouve pas l'absence d'outil : les moteurs de décision bancaires sont rarement publiés, et Creditinfo commercialise déjà du scoring aux banques.

### Cherché sans trouver

- Un client bancaire nommé dans la zone pour FICO, Experian, Provenir ou le moteur de décision Creditinfo (requête dédiée : aucun résultat pertinent).
- Un produit de prêt instantané documenté par Société Générale CI/Sénégal (seule trouvaille : agences « Manko », offre mobile, sans détail de scoring).
- Une banque béninoise avec prêt digital instantané (requête Bénin : seul MTN Bénin ressort, voir C2).

---

## Conclusion 2 : le crédit digital grand public est noté par l'opérateur et son prestataire ; la banque ne détient ni donnée ni modèle

### Verdict : affaiblie

Elle reste vraie pour le schéma « opérateur + prestataire + banque porteuse » (MTN Bénin, Orange Money avec JUMO), mais le cas Orange Bank Africa montre un montage où le prêteur est lui-même une banque, filiale de l'opérateur et d'un assureur, qui revendique son propre outil de scoring sur les données Orange Money.

### Éléments contraires

1. 
   - element : Orange Bank Africa (coentreprise Orange et NSIA, banque agréée) prête directement depuis Orange Money ; le scoring exploite les données Orange et Orange Money. La banque est donc à la fois prêteur et, au moins au sein du groupe, détentrice de l'accès aux données. Le propriétaire technique du modèle (interne ou prestataire) n'est pas divulgué dans l'article ouvert.
   - niveau : prouvé pour le montage bancaire et le produit ; indice pour le scoring sur données Orange Money
   - source : https://www.osiris.sn/orange-bank-africa-revele-les-coulisses-qui-simplifient-l-acces-au-microcredit.html
   - titre : Orange Bank Africa révèle les coulisses qui simplifient l'accès au microcrédit
   - editeur : Osiris
   - date_publication : 2025-07
   - consulte : 2026-10-29
   - type : presse
   - confiance : moyenne
2. 
   - element : Orange Bank Africa lancée sur la plateforme Temenos Transact (cœur bancaire propre), ce qui confirme une banque à part entière et pas un simple bilan porteur.
   - niveau : indice (titre de presse spécialisée non ouvert)
   - source : https://ibsintelligence.com/ibsi_prime_news/orange-bank-africa-launched-by-orange-nsia-with-temenos-transact/
   - titre : Orange Bank Africa launched by Orange, NSIA with Temenos Transact
   - editeur : IBS Intelligence
   - date_publication : 2020-07 (déduit de la date de lancement)
   - consulte : 2026-10-29
   - type : presse spécialisée
   - confiance : moyenne

Éléments qui confortent plutôt C2 (pour honnêteté) : MTN Bénin revendique un million d'utilisateurs de ses prêts digitaux lancés en 2024, de 1 000 à 100 000 FCFA, « sans formulaire ni étude de dossier » (indice, https://www.osiris.sn/mobile-money-prets-digitaux-epargne-mtn-detaille-sa-strategie-au-benin.html) ; « Orange Money renforce son offre de crédit grâce à la technologie de JUMO » (indice, https://www.wearetech.africa/fr/fils/actualites/finance/orange-money-renforce-son-offre-de-credit-en-afrique-grace-a-la-technologie-de-jumo).

### Meilleur argument contre

Le plus gros prêteur digital grand public de Côte d'Ivoire est une banque agréée UMOA (Orange Bank Africa), pas seulement un opérateur adossé à une banque passive ; elle revendique son propre scoring sur les données Orange Money et a déjà prêté plusieurs centaines de milliards de FCFA. La dichotomie « opérateur note, banque prête » ne décrit donc pas tout le marché, et le modèle « banque filiale d'opérateur » pourrait s'étendre (Sénégal déjà fait).

### Cherché sans trouver

- Une banque classique (non filiale d'opérateur) qui note elle-même les clients mobile money de la zone pour un nano-crédit.
- Le nom du prestataire ou de l'équipe qui a construit le modèle d'Orange Bank Africa (non divulgué dans la page ouverte).

---

## Conclusion 3 : aucune solution de scoring fondée sur des données fournies par le client (relevés, SMS, agrégation) n'est proposée aux banques dans l'UEMOA

### Verdict : affaiblie

Au moins un éditeur basé à Abidjan se positionne explicitement auprès des banques, IMF, SFD et fintechs des 8 pays de l'UEMOA avec un scoring fondé sur les flux de transactions réels, et un autre éditeur publie une offre de scoring alternatif « mobile money » pour l'UEMOA. Aucun des deux ne prouve l'usage de relevés exportés par le client ou de lecture de SMS, ni de clients nommés : l'énoncé « aucune solution » est trop absolu, l'énoncé « aucune solution documentée avec clients bancaires nommés » tiendrait.

### Éléments contraires

1. 
   - element : SCORE360 SARL (Abidjan, Koumassi) se présente comme « SME Credit Scoring Infrastructure · UEMOA » : transforme les flux de transactions réels des PME (encaissements, paiements) et les données d'interopérabilité PI-SPI en scores dynamiques pour « commercial banks, MFIs, SFDs and credit fintechs » ; revendique « 8 countries » et « 8+ institutions connected » ; API REST, SDK, webhooks, sandbox. Aucun client nommé, pas de date de lancement, pas de mention explicite de relevés exportés ni de SMS.
   - niveau : prouvé (existence et positionnement) ; indice (traction réelle, chiffres auto-déclarés)
   - source : https://score360.africa/en
   - titre : SCORE360, SME Credit Scoring Infrastructure · UEMOA
   - editeur : SCORE360 SARL
   - date_publication : inconnue (site consulté 2026-10)
   - consulte : 2026-10-29
   - type : site éditeur
   - confiance : moyenne (auto-déclaratif, aucune référence vérifiable)
2. 
   - element : Xloan (« by Open, Inc. ») publie une offre de scoring alternatif pour le crédit et le leasing en UEMOA, fondée sur « l'historique des transactions de mobile money », les achats de crédit téléphonique et les paiements de services publics ; la même source évoque l'accès, avec consentement, aux flux mobile money et relevés bancaires. Aucun client nommé.
   - niveau : prouvé (offre publiée) ; indice (déploiement réel inconnu)
   - source : https://xloan.open.global/credit-et-leasing-pourquoi-le-scoring-alternatif-simpose-dans-luemoa/
   - titre : Crédit et leasing : pourquoi le scoring alternatif s'impose dans l'UEMOA
   - editeur : Xloan / Open, Inc.
   - date_publication : 2026-08
   - consulte : 2026-10-29
   - type : blog éditeur
   - confiance : moyenne-faible
3. 
   - element : l'ARTCI a mis en garde (communiqué du 08/08/2023) contre des applications de prêt en ligne en Côte d'Ivoire (Easy Cash, Prêt Rapide, HiPret, CI money, etc.) qui accèdent aux contacts du téléphone ; des applications qui aspirent des données du téléphone pour prêter existent donc dans la zone, même hors cadre légal. Lecture de SMS de transaction non prouvée.
   - niveau : indice
   - source : https://osiris.sn/nouvelle-forme-de-pret-en-ligne-en-cote-d-ivoire-l-artci-appel-a-la-vigilance.html
   - titre : Nouvelle forme de prêt en ligne en Côte d'Ivoire : l'ARTCI appelle à la vigilance
   - editeur : Osiris (reprise du communiqué ARTCI)
   - date_publication : 2023-08
   - consulte : 2026-10-29
   - type : presse reprenant un régulateur
   - confiance : moyenne
4. 
   - element : Tontine Bénin propose une plateforme (application, USSD, collecteurs) qui « transforme l'épargne régulière en un score de crédit automatique » : donnée fournie par l'usager, au Bénin.
   - niveau : indice (extrait VC4A non ouvert)
   - source : https://vc4a.com/ventures/tontine-benin/
   - titre : Tontine Bénin
   - editeur : VC4A
   - date_publication : inconnue
   - consulte : 2026-10-29
   - type : fiche startup
   - confiance : faible

### Meilleur argument contre

Le créneau « scoring sur flux transactionnels fournis par le client, vendu aux banques de l'UEMOA » est déjà revendiqué publiquement par au moins un éditeur ivoirien (SCORE360), avec API, couverture des 8 pays et Cotonou cité nommément, ainsi que par une offre Xloan ; la mise en service du PI-SPI (2025) crée en plus une source de flux que ces acteurs exploitent. L'équipe ne peut donc pas présenter l'idée comme sans concurrent ; tout au plus comme un marché sans acteur établi ni référence bancaire publique.

### Cherché sans trouver

- Mono, Okra, Periculum, Indicina actifs en Afrique francophone : pas de requête dédiée faute de budget, aucun n'est ressorti dans les deux recherches générales sur l'agrégation et l'open banking UEMOA. Résultat incomplet, à compléter.
- Un cadre d'open banking UEMOA finalisé : un extrait indique qu'il n'en existe pas encore (indice, non ouvert), ce qui limite l'agrégation de comptes par API.
- Une application de prêt de la zone documentant la lecture des SMS de transaction pour le scoring : non trouvée.

---

## Conclusion 4 : il existe un manque réel (sans historique, qualité du bureau, transparence, calibration locale)

### Verdict : affaiblie (sur l'existence d'un acheteur bancaire, pas sur le besoin)

Le besoin d'inclusion existe, mais les sources trouvées suggèrent que le plafond d'usure bancaire comprime la marge sur exactement les segments visés et pousse le petit crédit vers les SFD et établissements financiers. Le client naturel d'un outil de scoring « particuliers et TPE » pourrait donc ne pas être la banque.

### Éléments contraires

1. 
   - element : depuis la décision n°19/29-12-2025/CM/UMOA, le taux d'usure est de 14 % pour les banques (contre 15 %) et reste à 24 % pour les établissements financiers et SFD. Selon l'analyse, « la contrainte majeure concerne surtout les segments intermédiaires (entrepreneurs individuels, TPE, PME) » où « la marge de manœuvre des banques se réduit » ; les banques pourraient « privilégier les profils les plus sûrs » ; le dispositif « consacre une segmentation durable du marché du crédit » entre crédit bancaire pour « les acteurs les plus solvables » et crédit non bancaire « plus onéreux ».
   - niveau : prouvé (lu) pour le contenu de l'analyse ; indice pour l'effet réel sur les banques
   - source : https://fr.allafrica.com/stories/202601080036.html
   - titre : Afrique de l'Ouest : Maintien du taux d'usure du crédit non bancaire. Le système peine à « bancariser » le risque
   - editeur : AllAfrica (Le Journal de l'Economie Sénégalaise)
   - date_publication : 2026-01
   - consulte : 2026-10-29
   - type : presse économique
   - confiance : moyenne-haute
2. 
   - element : article d'analyse sur le recalibrage du taux d'usure par la même décision (14 % banques, 24 % EF/SFD), confirmant la structure à deux vitesses.
   - niveau : indice (extrait de recherche)
   - source : https://www.financialafrik.com/2026/07/27/taux-dusure-dans-luemoa-le-recalibrage-opere-par-la-decision-n19-29-12-2025-cm-umoa/
   - titre : Taux d'usure dans l'UEMOA : le recalibrage opéré par la décision n°19/29-12-2025/CM/UMOA
   - editeur : Financial Afrik
   - date_publication : 2026-07
   - consulte : 2026-10-29
   - type : presse économique
   - confiance : moyenne
3. 
   - element : le marché du crédit digital de masse est déjà servi sans la banque classique : MTN Bénin (1 million d'utilisateurs, prêts sans étude de dossier) et Orange Bank Africa (640 milliards FCFA prêtés). Le « manque » sur les petits montants est donc en partie comblé par des acteurs qui ont la donnée et la distribution.
   - niveau : déduit (à partir des éléments C1 et C2)
   - source : https://www.osiris.sn/mobile-money-prets-digitaux-epargne-mtn-detaille-sa-strategie-au-benin.html
   - titre : Mobile money, prêts digitaux, épargne : MTN détaille sa stratégie au Bénin
   - editeur : Osiris
   - date_publication : inconnue (2025-2026 d'après le contenu)
   - consulte : 2026-10-29
   - type : presse
   - confiance : moyenne
4. 
   - element : un logiciel béninois de gestion de crédit pour IMF intègre déjà du scoring sur smartphone (application agent hors ligne, visite, photos, géolocalisation) : une offre locale existe déjà côté microfinance.
   - niveau : indice (extrait de blog d'éditeur non ouvert)
   - source : https://kolonell.com/fr/blog/logiciel-gestion-credit-imf-sur-mesure-cotonou-2026
   - titre : Logiciel de gestion de crédit IMF sur mesure à Cotonou (2026)
   - editeur : Kolonell
   - date_publication : 2026
   - consulte : 2026-10-29
   - type : blog éditeur
   - confiance : faible

### Meilleur argument contre

Avec un plafond de 14 % TEG, une banque de l'UEMOA a peu d'intérêt économique à prêter de petits montants à des clients sans historique, même avec un meilleur score : la même analyse prévoit qu'elle se repliera sur les profils les plus sûrs et laissera ce segment aux SFD et établissements financiers plafonnés à 24 %. Le « manque » est donc peut-être réel pour l'inclusion mais pas solvable par la banque ; les petits montants sont déjà captés par les opérateurs (MTN, Orange Bank Africa) qui ont la donnée et la distribution, et un éditeur local (SCORE360) occupe déjà le discours « PME sans historique ».

### Cherché sans trouver

- Données chiffrées sur la préférence des banques UEMOA pour les titres publics et les grandes entreprises (la requête n'a rien remonté de spécifique ; à chercher dans les rapports BCEAO ou FMI).
- Échecs documentés de projets de scoring alternatif dans la zone : pas de requête dédiée faute de budget.
- Étude concluant que les outils existants (score Creditinfo, analyse de dossier) suffisent : non trouvée.
- Preuve que les banques de la zone refusent d'acheter des logiciels locaux : non trouvée.

---

## Limites de cette contre-expertise

- Plusieurs éléments reposent sur des extraits de moteur de recherche (niveau indice) ; les pages primaires (Orange Bank Africa, IFC, Creditinfo, Ecobank) n'ont pas été ouvertes faute de budget.
- Non couverts : Mono, Okra, Periculum, Indicina en zone francophone ; Wave et Djamo comme prêteurs ; Coris Bank, Bank of Africa, Orabank ; Mali, Burkina, Niger, Togo.
