---
title: 'Étude de domaine : axe B, cadre réglementaire du crédit'
type: 'domain'
topic: 'Axe B : cadre réglementaire du crédit (UEMOA, Bénin)'
decision: 'Définition du défaut (Q-03) et cadre légal du produit (Q-06)'
source: 'run'
status: complete
preset: 'standard'
validation: 'high'
created: '2026-10-08'
updated: '2026-10-08'
claims_verified: 7
claims_unverified: 15
claims_disputed: 3
claims_overturned: 1
---

# Étude de domaine : axe B, cadre réglementaire du crédit

**Décisions servies :** la définition du défaut (Q-03), le cadre légal du produit (Q-06) et le volet légal du partage de données avec un prestataire (question 22, Q-10).
**Questions traitées :** 5 à 9 et le volet légal de la question 22 ([questions de recherche](../00_QUESTIONS_DE_RECHERCHE.md)).
**Orientation :** banques en priorité, puis IMF de grande taille. Cadre UMOA, transposition au Bénin.
**Recherche menée le :** 08/10/2026, en deux tours suivis d'une contre-vérification indépendante (méthode `bmad-deep-recon`, niveau standard, vérification « high », sans passe de contradiction à la demande de Daniela).

**Comment lire ce rapport**
- Chaque règle cite son **texte officiel et son article**, puis la source `[R-xxx]` de la [bibliographie](../../REFERENCES.md). Aucune source n'est encore vérifiée ensemble : aucune ne fonde une décision à ce stade.
- Chaque règle porte un **statut** :
  - **Confirmée** : article lu dans le texte officiel, et confirmé par une seconde source indépendante ;
  - **Lue** : article lu dans le texte officiel, sans seconde source trouvée ;
  - **À vérifier** : article non lu dans le texte (résumé d'un tiers, scan illisible, vigueur douteuse).
- **Vigueur.** Les textes ont été lus dans la version publiée par les autorités. Leur maintien en vigueur en octobre 2026 n'a pas toujours pu être prouvé : la liste officielle des textes en vigueur de la Commission bancaire était inaccessible. Chaque fois que c'est le cas, le rapport le dit.
- « Interprétation » signale une lecture du texte qui n'est confirmée par aucune autorité. Elle doit être validée par un juriste avant tout engagement.

---

## 1. Synthèse

### Définition du défaut (Q-03)

**Pour les banques, la définition réglementaire est connue et précise.** L'Instruction BCEAO n°026-11-2016 classe une créance en « douteuse ou litigieuse » dans deux cas :
- au moins une échéance est impayée depuis **plus de 90 jours** ;
- le non-paiement est jugé probable, indépendamment de tout impayé.

Le délai passe à **180 jours pour les PME/PMI, les États et les organismes publics** (art. 8) [R-031]. Pour les **particuliers**, la cible du projet, la règle est donc **90 jours**. Pour la **clientèle de détail**, le défaut est apprécié **par crédit**, et non par client (art. 11) [R-031], [R-032]. Les seuils de 90 et 180 jours sont confirmés par le guide d'application de la BCEAO et par le FMI ; le défaut par crédit pour la clientèle de détail est confirmé par le guide [R-035], [R-015].

**Pour les SFD, la règle est différente.** Tout l'encours d'un crédit doit être déclassé au-delà de **3 mois** d'impayé, avec des provisions de 40, 80 puis 100 % (Référentiel comptable des SFD de 2009) [R-039]. C'est un équivalent pratique de 90 jours. Aucun régime à 180 jours n'apparaît dans les passages lus.

**Point à corriger dans nos documents.** La « norme de 3 % » souvent citée pour les SFD n'est **pas une norme prudentielle** : elle ne figure pas dans l'Instruction n°010-08-2010, qui fixe les règles prudentielles des SFD. C'est une norme de référence employée par la BCEAO dans ses publications, sans base juridique trouvée [R-037], [R-065].

### Cadre légal du produit (Q-06)

- **Le taux d'usure a changé.** Depuis le **01/06/2026**, il est de **14 % l'an pour les banques** (contre 15 % avant) et de **24 % pour les établissements financiers et les IMF** (Décision n°19 du 29/12/2025/CM/UMOA, art. 2) [R-040], [R-042], [R-044].
- **Le coût calculé inclut les frais.** Au Bénin, le taux effectif global (TEG) inclut les frais et rémunérations de toute nature (loi n°2024-15, art. 3) [R-043].
- **Le nano-crédit tel qu'observé paraît incompatible avec ce plafond.** Les offres relevées par l'axe A facturent 9 à 14 % de frais sur 7 à 30 jours, soit 110 à 730 % l'an en annualisation simple. Aucune exception n'a été trouvée, et la loi béninoise punit aussi quiconque « apporte sciemment […] son concours » à un prêt usuraire (art. 7) [R-043].
- **Le scoring interne ne sert pas au calcul des fonds propres.** Les banques de l'UMOA appliquent l'**approche standard** de Bâle (dispositif prudentiel, § 90), sans modèles internes [R-032], [R-015]. Un outil de scoring relève donc de la **gestion du risque d'octroi** (circulaire n°04-2017/CB/C, art. 20 et 22), qui exige « un système approprié de notation ou de classement des crédits » [R-033]. Ces articles ont été lus dans une copie marquée « projet », dont la conformité avec la version signée reste à vérifier. Aucune obligation explicite de validation ou de backtesting d'un tel outil n'a été trouvée.
- **IFRS 9 n'est pas appliqué** dans les comptes réglementaires des banques. Leur provisionnement suit un barème calendaire (20, 50, puis 100 %), et le FMI recommande d'adopter IFRS 9 [R-031], [R-015].

### Données et prestataire (Q-22)

- **Bureau de crédit.** Les banques et les SFD supervisés doivent **consulter le bureau d'information sur le crédit avant tout crédit**, avec le **consentement écrit** de l'emprunteur (loi uniforme BIC, art. 53 et 60) [R-052]. Un prestataire n'est pas « utilisateur » du bureau : il ne peut traiter ces rapports que pour le compte de la banque (interprétation).
- **Décisions automatisées.** Au Bénin, une décision de crédit prise **uniquement** par un traitement automatisé est interdite, sauf si elle s'inscrit dans un contrat qui permet au client de **faire valoir son point de vue**. Le client peut demander la **logique sous-jacente** de la décision (Code du numérique, art. 401 et 437) [R-061]. Le scoring pourrait aussi exiger une **autorisation préalable de l'APDP** (art. 407, interprétation).
- **Secret bancaire et sous-traitance.** Le secret bancaire autorise la transmission de données à un prestataire chargé de « fonctions opérationnelles » (loi bancaire n°2024-14, art. 68) [R-059]. La sous-traitance bancaire impose toutefois deux conditions (circulaire n°04-2017/CB/C, art. 33) [R-033] :
  - des **serveurs dans l'UMOA**, ou à défaut des serveurs de secours dans l'Union avec une réplication complète des données ;
  - la **soumission préalable du contrat à la Commission bancaire**.
- **Transfert hors CEDEAO.** Tout transfert de données vers un pays hors CEDEAO exige l'autorisation de l'APDP (art. 391) [R-061]. La CEDEAO impose au minimum d'informer au préalable l'autorité de protection [R-063].

### Principales réserves

1. **Microfinance au Bénin.** Une **nouvelle loi n°2025-14** sur la microfinance a été adoptée le 24/06/2025 [R-050], [R-051]. Son texte, scanné, n'a pas pu être lu. Les règles béninoises des SFD citées ici, issues de la loi de 2012, sont donc peut-être dépassées.
2. **Code du numérique.** Seule la **version adoptée le 13/06/2017** a pu être lue, pas la version promulguée du 20/04/2018.
3. **Crédit digital.** **Aucun texte propre au crédit digital** n'a été trouvé. La presse d'août 2026 évoque un débat sur son cadre prudentiel [R-076].

---

## 2. Volet B1 : créances en souffrance, défaut, classement, provisionnement

*Question 5 : comment la BCEAO et la Commission bancaire définissent-elles une créance en souffrance, et quelles règles de classement et de provisionnement s'appliquent ?*

### 2.1 Banques et établissements financiers

Texte de référence : **Instruction BCEAO n°026-11-2016 du 15/11/2016** relative à la comptabilisation et à l'évaluation des engagements en souffrance, en vigueur depuis le 01/01/2018 (art. 19) [R-031]. Elle s'applique aux banques et aux établissements financiers à caractère bancaire, **pas aux SFD** (art. 1er). Le dispositif prudentiel reprend la même définition (§ 152 à 158) [R-032].

| Règle | Texte et article | Statut |
|---|---|---|
| Quatre catégories : créances saines, créances en souffrance, créances irrécouvrables, engagements douteux. Créances en souffrance = créances restructurées + créances douteuses ou litigieuses. Il n'existe pas de catégorie « compromise ». | Instr. 026-11-2016, art. 3 et 5 [R-031] | Lue ; le § 152 du dispositif confirme la composition des créances en souffrance [R-032] |
| Une échéance impayée depuis 90 jours au plus, sans prorogation ni renouvellement, reste une créance saine. | art. 4 al. 2 [R-031] | Lue |
| **Défaut par impayé** : créance douteuse dès qu'une échéance est impayée depuis **plus de 90 jours**. Le délai passe à **180 jours** pour les États de l'UMOA, les organismes publics hors administration centrale et les **PME/PMI**. Particuliers et grandes entreprises : 90 jours. | art. 8 al. 1 pt 2° et al. 2 [R-031] | Confirmée [R-035], [R-015] |
| **Défaut sans impayé** : créance douteuse si le non-paiement est probable (procédures collectives, faillite personnelle, difficultés de gestion…). | art. 8 al. 1 pt 1° et art. 9 [R-031] | Confirmée [R-032], [R-015] |
| **PME/PMI** : entreprise dont le chiffre d'affaires hors taxes annuel n'excède pas **1 milliard FCFA**, sans critère d'effectif. L'Instruction n°024-11-2016 (définition des attributs) n'a pas été lue. | Décision n°29 du 29/09/2015/CM/UMOA, citée par le guide BCEAO [R-035] | À vérifier (décision non lue) |
| **Créance restructurée** : créance renégociée par des concessions envers un débiteur en difficulté. Tout abandon de créance est passé en perte, et une décote est constatée en coût du risque. | art. 5 et 6 [R-031] | Confirmée [R-032] |
| **Retour en sain d'une créance restructurée** : après 1 an sans impayé, puis 2 ans dans une sous-catégorie spécifique. Pendant 3 ans, un retard de plus de 30 jours ou une nouvelle concession la fait rebasculer en douteux. | art. 7 [R-031] | Lue |
| **Retour en sain d'une créance douteuse** : après 1 an de paiements réguliers, puis 2 ans de probation. | art. 10 [R-031] | Lue |
| **Contagion** : le déclassement d'une créance entraîne celui de tous les encours du débiteur, **sauf** pour l'escompte commercial et la **clientèle de détail**. Pour cette dernière, le défaut reste limité au crédit concerné. | art. 11 [R-031] ; dispositif § 158 [R-032] | Confirmée [R-035] |
| **Clientèle de détail** : particulier ou PME/PMI, exposition d'au plus 0,2 % du portefeuille de détail et d'au plus **150 millions FCFA**, avec le **consentement du client au partage de ses données avec le bureau de crédit**. | dispositif § 135 [R-032] | Confirmée [R-035] (numéro de paragraphe non confirmé par la seconde source) |
| **Provisionnement** des risques privés douteux, partie non couverte par une garantie : au moins **20 %** au déclassement, **50 %** 3 mois après, **100 %** 9 mois après. Partie couverte par une garantie éligible : facultatif pendant 2 ans, 50 % la 3e année, 100 % la 4e. Intérêts impayés : 100 %. Risques sur les États, les organismes publics et les créances restructurées : provisionnement facultatif. | art. 15 et 16 [R-031] | Confirmée [R-035], [R-067] |
| **Passage en irrécouvrable** : créance douteuse non recouvrée au terme du **5e exercice** suivant son déclassement. | art. 13 [R-031] | Lue ; selon une source secondaire, une directive UEMOA de 2020 retient aussi le 5e exercice [R-068] (directive non lue) |
| **Pondération prudentielle** : partie non couverte d'une créance en souffrance pondérée à 150 % si les provisions sont inférieures à 20 %, et à 100 % au-delà. Clientèle de détail : 75 %. | dispositif § 137 et § 157 [R-032] | Lue |

**Vigueur.** L'Instruction n°026-11-2016 est toujours publiée par la Commission bancaire, et aucune modification n'a été trouvée. En revanche, la liste officielle des textes en vigueur était inaccessible (erreur 404) : son maintien en 2026 n'est pas prouvé.

**Divergence à vérifier.** Le FMI écrit que le provisionnement du principal des expositions publiques reste facultatif même après 180 jours [R-015]. C'est cohérent avec l'art. 16 pour les États, mais l'article n'a été relu que pour les risques privés.

### 2.2 SFD (microfinance)

| Règle | Texte et article | Statut |
|---|---|---|
| **Défaut** : un crédit est en souffrance dès qu'**une échéance** est impayée, et **tout l'encours** est alors déclassé. Le déclassement est facultatif entre 0 et 3 mois, donc **obligatoire au-delà de 3 mois**. Les intérêts cessent d'être comptabilisés dès le déclassement. | Référentiel comptable spécifique des SFD (Instruction n°025-02-2009), compte 29 [R-039] | Lue (édition 2009 ; une version de 05/2022 existe, non lue) |
| **Provisionnement** sur l'encours diminué des dépôts de garantie : facultatif de 0 à 3 mois ; **40 %** de 3 à 6 mois (le libellé du compte dit « 6 mois au plus » : rattacher le 40 % à la tranche 3-6 mois est une interprétation) ; **80 %** de 6 à 12 mois ; **100 %** de 12 à 24 mois. | même texte, compte 299 [R-039] | Lue (même réserve) |
| **Irrécouvrable** : impayé de plus de 24 mois, passage en charges. | même texte, compte 29 [R-039] | Lue |
| **Règles prudentielles des SFD** : neuf normes (limitation des risques, liquidité, capitalisation d'au moins 15 %, risques sur une seule signature d'au plus 10 %…). **Aucune ne porte sur la qualité du portefeuille.** | Instruction n°010-08-2010 du 30/08/2010, art. 2 et annexe [R-037] | Lue |
| **« Norme de 3 % »** : la BCEAO compare le taux brut de dégradation du portefeuille des SFD à une « norme maximale de 3,0 % ». Aucun texte cité ; en 2009, la BCEAO utilisait un seuil de 5 %. | note BCEAO, microfinance fin 2023 [R-065] ; note fin 2009 [R-066] | À vérifier : norme de référence, base juridique non trouvée |
| Les SFD de l'article 44 transmettent leurs indicateurs chaque mois, les autres chaque trimestre. L'annexe qui définit ces indicateurs était illisible. | Instruction n°020-12-2010, art. 2 à 4 [R-037] | Lue (annexe non lue) |

**Conséquence.** Dans les passages lus, les SFD n'ont ni seuil de 180 jours pour les PME ni règle de contagion. Leur seuil pratique est le même que pour les particuliers en banque, environ 90 jours.

Les deux calendriers de provisions ne partent pas du même moment : en banque, ils courent depuis le déclassement ; en SFD, depuis l'impayé. Ramenés au même point de départ, le premier impayé, les deux régimes commencent à provisionner vers 3 mois et atteignent 100 % vers 12 mois. Les SFD commencent plus haut, à 40 % contre 20 % pour les banques. Cette comparaison est la mienne et reste à vérifier.

### 2.3 IFRS 9

- Le référentiel des banques reste le **Plan comptable bancaire révisé** (Décision n°357-11-2016, en vigueur au 01/01/2018) [R-031]. Le provisionnement y suit un **barème calendaire** fondé sur les **pertes avérées**. Ce n'est pas le modèle IFRS 9 des **pertes attendues** en trois stades.
- Le **FMI** recommande en mai 2026 de « donner la priorité à l'adoption d'IFRS 9 pour remplacer le modèle des pertes avérées » [R-015]. C'est la confirmation, par une source indépendante, que les banques ne l'appliquent pas encore.
- La circulaire n°04-2017/CB/C demande déjà que les provisions tiennent compte d'**informations prospectives, y compris macroéconomiques** (art. 24, lu dans la copie marquée « projet ») [R-033]. C'est une logique proche d'IFRS 9, mais sans ses trois stades.
- **IFRS pour les entités faisant appel public à l'épargne** : l'Acte uniforme OHADA de 2017 les rend obligatoires pour les entités cotées. Le Plan comptable bancaire y renvoie par son art. 4 [R-035]. En revanche, la décision UMOA citée sous le numéro « CM/17/09/2022 » n'a pas été trouvée (**à vérifier**).
- **Transition annoncée** : la BCEAO aurait lancé le 05/05/2026 un appel à consultants pour la transition du Plan comptable bancaire vers les IFRS [R-078]. L'information vient d'un agrégateur d'appels d'offres et n'a pas été retrouvée sur le site de la BCEAO (**à vérifier**). La BCEAO forme les banques à IFRS 9 depuis 2021 [R-077].

---

## 3. Volet B2 : taux d'usure et coût du crédit

*Question 6 : quel taux maximum (taux d'usure) encadre le crédit ?*

| Règle | Texte et article | Statut |
|---|---|---|
| **Taux d'usure** : **14 % l'an pour les banques** ; **24 % l'an** pour les établissements financiers de crédit, les institutions de microfinance et les autres agents économiques. En vigueur depuis le **01/06/2026**, abroge les dispositions antérieures (15 % pour les banques jusque-là). | Décision n°19 du 29/12/2025/CM/UMOA, art. 2 et 4 [R-040] ; notifiée par l'Avis BCEAO n°007-12-2025 [R-041] | Confirmée [R-042], [R-044]. La page de questions-réponses de la BCEAO sur l'usure des SFD cite encore la décision de 2013 : elle est périmée, mais le taux de 24 % est le même [R-045] |
| Le taux d'usure est fixé par le **Conseil des ministres de l'UMOA**. Est usuraire tout prêt, « en toute matière », dont le TEG dépasse ce taux. | Loi béninoise n°2024-15 du 23/05/2024, art. 1er [R-043] | Lue |
| **Le TEG inclut** les frais et rémunérations de toute nature, y compris ceux versés aux intermédiaires, ainsi que les charges liées aux garanties. Il **exclut** les impôts et taxes. Le taux doit figurer par écrit dans le contrat. | loi 2024-15, art. 2 et 3 [R-043] | Confirmée [R-044] (qui y ajoute les primes d'assurance) ; l'obligation de mentionner le TEG dans le contrat est aussi relevée par [R-072] |
| **Majoration possible** du plafond, par des « perceptions forfaitaires », pour des opérations à frais fixes élevés. Aucune décision d'application n'a été trouvée. | loi 2024-15, art. 4 [R-043] | **Contestée** : la loi béninoise confie la fixation au Conseil des ministres de l'UMOA ; un extrait non attribué la confie au ministre des Finances |
| Les ventes à tempérament sont assimilées à des prêts et soumises au plafond. Interprétation : cela viserait aussi le paiement fractionné (BNPL). | loi 2024-15, art. 5 [R-043] | Lue |
| **Sanctions** : 2 mois à 2 ans de prison et 100 000 à 5 000 000 FCFA d'amende. Les **mêmes peines** s'appliquent à quiconque **apporte sciemment son concours** à l'octroi d'un prêt usuraire. | loi 2024-15, art. 7 [R-043] | Lue |
| **Loi uniforme UMOA sur l'usure** : visée par la Décision n°19 (« notamment en son article premier »), sans date ni numéro. | [R-040] | À vérifier (texte non trouvé) |
| **Affirmation contredite** : la presse a annoncé en 2024 un taux de 18 % pour les banques et de 27 % pour les SFD au Bénin. Cela contredit la loi 2024-15, selon laquelle le taux est fixé par l'UMOA, et la BCEAO, qui donnait 15 % et 24 % avant juin 2026. | [R-046] contre [R-043], [R-042] | Contestée : version de presse probablement erronée, non tranchée (article non lu en entier) |

**Compatibilité avec le crédit digital.** Les offres relevées par l'axe A facturent 9 à 14 % de frais pour 7 à 30 jours. En annualisation simple (calcul : frais × 365 / durée), cela donne :
- 9 % sur 30 jours : environ 110 % l'an ;
- 14 % sur 7 jours : environ 730 % l'an.

Puisque les frais entrent dans le TEG (art. 3), ces tarifs dépassent le plafond de 24 % d'un facteur 5 à 30, et celui de 14 % encore davantage. Aucune exception pour les crédits de très courte durée n'a été trouvée, et aucune décision n'a fixé de perceptions forfaitaires. **Lecture provisoire : ce nano-crédit n'apparaît pas compatible avec le plafond d'usure, sauf texte non identifié.** Confiance moyenne, à faire valider par un juriste : le mode d'annualisation (proportionnelle ou actuarielle) n'est fixé dans aucun texte lu. Par ailleurs, selon le rapport de l'axe A, le prêteur en titre de ces offres est une banque (Ecobank ou UBA) : c'est donc le plafond de 14 % qui s'appliquerait.

**Vigueur de la loi 2024-15.** Ses pages 4 et 5 (abrogation de la loi antérieure, entrée en vigueur) sont des images sans texte et n'ont pas été lues.

---

## 4. Volet B3 : émetteurs de monnaie électronique, crédit digital, IMF de grande taille

*Question 6 (suite) : droit d'un émetteur de monnaie électronique à prêter, cadre du nano-crédit, seuil de l'article 44.*

### 4.1 Émetteurs de monnaie électronique et établissements de paiement

| Règle | Texte et article | Statut |
|---|---|---|
| **Un émetteur de monnaie électronique ne peut pas accorder de crédit**, « sous quelle que forme que ce soit », ni rémunérer les fonds. En revanche, les fonds d'un crédit accordé **par une banque ou un SFD** peuvent servir à émettre de la monnaie électronique : la banque prête, le portefeuille mobile reçoit l'argent. | Instruction BCEAO n°008-05-2015 du 21/05/2015, art. 5 [R-047] | Lue |
| Les fonds reçus en contrepartie de la monnaie électronique sont placés sur un **compte dédié** auprès de banques ou de SFD, rapprochés chaque jour, et ne servent jamais à l'exploitation de l'émetteur. Au moins 75 % sont placés en dépôts à vue. | art. 32 à 34 [R-047] | Lue |
| Les partenariats d'un émetteur se limitent au traitement technique ou à la distribution de la monnaie électronique. Aucun rôle de distributeur de crédit n'y est prévu (constat de lecture). | art. 4, 16 et 17 [R-047] | Lue (absence de mandat de crédit = interprétation) |
| **Établissements de paiement** : interdiction d'accorder du crédit « de quelque manière que ce soit ». Les partenariats avec clause d'exclusivité sont interdits pour tous les prestataires de services de paiement. | Instruction n°001-01-2024 relative aux services de paiement, art. 7 et 8 [R-048] | Lue |
| L'Instruction n°001-01-2024 est en vigueur depuis le 23/01/2024 (date de signature en blanc dans le PDF). Depuis le 01/09/2025, seules les structures agréées peuvent fournir des services de paiement. Elle n'abroge pas expressément l'instruction de 2015, seulement les « dispositions antérieures contraires ». | art. 96 et 97 [R-048] ; [R-073], [R-074] | À vérifier (date et sort exact de l'instruction de 2015) |
| L'« agent bancaire » est une personne immatriculée auprès de la BCEAO, qui présente des opérations de banque pour le compte d'établissements de crédit. Le texte qui fixe son régime n'a pas été trouvé. | Instruction n°001-01-2024, art. 3 pt 2 [R-048] | Lue pour la définition ; régime à vérifier |

**Conséquence.** L'opérateur mobile ne peut pas être le prêteur (art. 5). Le montage observé dans l'axe A (opérateur, banque prêteuse, prestataire technique) correspond au seul schéma décrit par le texte : la banque ou le SFD prête. Un émetteur peut-il distribuer le crédit d'une banque, par exemple comme agent bancaire ? Ce n'est pas établi (interprétation).

### 4.2 Cadre du crédit digital et protection de la clientèle

- **Aucun texte de la BCEAO, de la Commission bancaire ou du Conseil des ministres de l'UMOA propre au crédit digital ou au nano-crédit n'a été trouvé** (recherches du 08/10/2026). Ce n'est pas une preuve d'absence, mais aucune des sources consultées, officielles ou de presse, n'en cite.
- La **Stratégie régionale d'inclusion financière 2025-2030** (adoptée le 03/04/2025) fait de la protection de la clientèle une priorité, sans texte d'application cité [R-075].
- En août 2026, la presse décrit un **débat sur le cadre prudentiel** des opérateurs et fintechs qui veulent prêter pour leur propre compte. Trois options sont évoquées : les mêmes règles que les banques, une catégorie « banque numérique », ou la séparation des activités. Aucune position officielle n'est citée [R-076] (confiance basse).
- **Protection de la clientèle** :
  - 19 services bancaires sont gratuits depuis le 01/10/2014, sur décision de la BCEAO après concertation avec la profession. Le numéro du texte n'a pas été trouvé [R-070], [R-071].
  - Une circulaire n°002-2020/CB/C du 18/09/2020 sur le traitement des réclamations a été identifiée par une tribune de 2021, vue seulement en extrait. Ni la tribune ni la circulaire n'ont été lues [R-079].
  - Le traité de l'UMOA ne contient pas de disposition propre à la protection des consommateurs [R-069].

### 4.3 IMF de grande taille (article 44)

| Règle | Texte et article | Statut |
|---|---|---|
| La BCEAO et la Commission bancaire contrôlent tout SFD dont l'activité atteint un seuil fixé par instruction de la BCEAO. | Loi uniforme portant réglementation des SFD (adoptée le 06/04/2007), art. 44 [R-037] ; loi béninoise n°2012-14 du 21/03/2012, art. 44 [R-049] | Confirmée (deux textes) |
| **Seuil** : encours de dépôts **ou** de crédits d'au moins **2 milliards FCFA au terme de deux exercices consécutifs**. Pour les réseaux mutualistes, il s'apprécie au niveau de la faîtière et des caisses affiliées. | Instruction n°007-06-2010 du 14/06/2010, art. 2 [R-038] | Lue |
| Pour un SFD de l'article 44, seuls changent le contrôle direct par la BCEAO et la Commission bancaire et le rythme de transmission des indicateurs (mensuel). Normes prudentielles et provisionnement sont les mêmes pour tous les SFD. | Instr. 010-08-2010, art. 4 ; Instr. 020-12-2010, art. 2 et 3 [R-037] | Lue |
| **Nouvelle loi béninoise sur la microfinance** : loi n°2025-14, adoptée le 24/06/2025 (173 articles, vocabulaire « institutions de microfinance », conseil d'administration obligatoire, capital minimum, exigences prudentielles renforcées, 12 mois de mise en conformité). Le texte officiel est un scan illisible. | [R-050], [R-051] | À vérifier : abrogation de la loi 2012-14 et article qui remplace l'art. 44 non lus |

Des lois sur la microfinance ont été adoptées la même année au Sénégal et au Burkina Faso, ce qui suggère une **nouvelle loi uniforme UMOA**. Aucune décision du Conseil des ministres n'a été trouvée pour le confirmer (hypothèse).

---

## 5. Volet B4 : bureaux d'information sur le crédit

*Question 7 : que prévoient les textes sur les bureaux d'information sur le crédit (couverture, obligation de consultation, consentement) ?*

**Textes.** Le texte régional est la **loi uniforme** portant réglementation des bureaux d'information sur le crédit (BIC), annexée à la Décision n°CM/UMOA/007/06/2013 du 28/06/2013. Elle est complétée par huit instructions BCEAO de 2015 (n°001, 002 et 003-01-2015 ; n°005, 006 et 007-05-2015 ; n°009 et 010-06-2015) [R-052]. Au Bénin, le projet de loi a été transmis à l'Assemblée nationale en novembre 2014 [R-054]. Il est devenu la **loi n°2016-36 du 23/01/2017**, modifiée par la **loi n°2020-08 du 23/04/2020** portant modernisation de la justice, une loi qui modifie plusieurs textes à la fois [R-055], [R-056]. Le texte béninois n'a pas été trouvé (erreur 404). **Les articles ci-dessous sont donc ceux de la loi uniforme.** Leur concordance avec la loi béninoise est à vérifier.

| Règle | Article (loi uniforme) | Statut |
|---|---|---|
| **Qui fournit des données au bureau** : établissements de crédit, SFD, mais aussi **opérateurs de téléphonie fixe et mobile** et **sociétés d'eau et d'électricité** pour l'historique de paiement. | art. 1er [R-052] | Confirmée [R-058] |
| **Obligation de consulter et de déclarer** : les établissements de crédit et les SFD supervisés par la BCEAO et la Commission bancaire doivent **consulter le bureau avant d'accorder un crédit**, verser le rapport au dossier et partager les données de tous leurs prêts. Pour les autres SFD et pour les grands facturiers, la participation est facultative. | art. 60 et 61 [R-052] | Lue (à vérifier dans la loi béninoise 2016-36) |
| Au Bénin, les établissements agréés doivent adhérer à un système de partage de l'information sur le crédit. | loi bancaire n°2024-14, art. 249 [R-059] (votée le 29/04/2024 [R-060]) | Lue |
| **Consentement** : toute collecte, consultation et diffusion exige le **consentement préalable, écrit et spécifique** du client. Il est inscrit dans la demande ou le contrat de crédit et vaut pendant toute la relation d'affaires. Un consentement en ligne est admis sous conditions. | art. 53 [R-052] ; Instruction n°002-01-2015, art. 2 et 3 [R-052] | Confirmée [R-053] |
| **Exception béninoise de 2020** : l'historique des crédits antérieurs au 23/01/2017 peut être partagé **sans consentement**. | art. 53 modifié par la loi 2020-08 [R-055] | À vérifier (contenu connu seulement par la presse [R-057]) |
| **Qui peut consulter** : seuls les « utilisateurs » liés au bureau par contrat, qui lui fournissent eux-mêmes des données (réciprocité). Motifs autorisés : octroi ou recouvrement d'un crédit, justice, supervision, demande du client, autre motif approuvé par la BCEAO. Le **marketing** est interdit. | art. 1er, 36, 43, 59 et 62 [R-052] | Lue |
| **Données interdites** : données sensibles, soldes et opérations des comptes d'épargne et de dépôt (sauf chèques impayés). | art. 53 al. 3 et 62 [R-052] | Lue |
| **Droits de l'emprunteur** : information préalable ; copie gratuite de son rapport une fois par an ; contestation (réponse du fournisseur sous 15 jours, correction par le bureau sous 10 jours, retrait de la consultation au-delà de 30 jours) ; **en cas de refus de crédit fondé même en partie sur le rapport, la banque doit l'en informer et lui remettre le rapport** ; diffusion des informations limitée à **5 ans**, puis archivage 5 ans. | art. 41, 44, 46, 47, 48 à 52 [R-052] | Lue |
| Le bureau peut vendre des **scores** comme service à valeur ajoutée, après autorisation de la BCEAO. | art. 1er et 33 pt 5 [R-052] | Confirmée [R-058] |
| Les bases du bureau ne peuvent pas être hébergées hors de l'UMOA. | art. 35 [R-052] | Lue |
| Bureau en activité : **Creditinfo West Africa**, agréé le 12/05/2015, actif au Bénin. Aucun second bureau n'a été trouvé. | grille tarifaire 2025 [R-058] | Lue (la liste officielle 2026 n'a pas été vérifiée) |

**Conséquence pour le projet (interprétation).** Un prestataire de scoring n'est pas « utilisateur » au sens de la loi : il ne peut ni consulter le bureau en son nom, ni utiliser ses rapports à d'autres fins. Il ne peut les traiter que pour le compte de la banque, qui reste tenue à la confidentialité (art. 43). La loi ne dit rien d'une transmission du rapport au sous-traitant de la banque : la question est à poser à la BCEAO ou au bureau.

---

## 6. Volet B5 : protection des données, secret bancaire, sous-traitance (questions 8 et 22)

*Question 8 : quelles règles encadrent l'usage de données alternatives et les décisions automatisées ? Question 22 (volet légal) : que permet la loi pour partager des données avec un prestataire ?*

**Textes.**
- Au Bénin : le **Livre V de la loi n°2017-20 du 20/04/2018 portant Code du numérique**, modifiée par la loi n°2020-35 du 06/01/2021, qui ne touche pas les articles cités ci-dessous [R-061], [R-062]. L'autorité de contrôle est l'**APDP**.
- Au niveau régional : l'**Acte additionnel CEDEAO A/SA.1/01/10** du 16/02/2010 [R-063]. Le Bénin a autorisé en janvier 2024 la ratification de la **Convention de l'Union africaine de Malabo** [R-064].

**Réserve importante :** le Code a été lu dans sa **version adoptée par l'Assemblée nationale le 13/06/2017**. La version promulguée n'a pas pu être téléchargée. Tous les articles du Code sont donc « Lus » sous cette réserve.

| Règle | Texte et article | Statut |
|---|---|---|
| **Bases légales** : consentement ; à défaut, obligation légale, mission d'intérêt public, **exécution d'un contrat ou mesures précontractuelles à la demande de la personne**, sauvegarde de ses intérêts. **Il n'y a pas de base « intérêt légitime »**, contrairement au RGPD européen. | Code du numérique, art. 389 [R-061] | Lue |
| **Données sensibles** interdites, sauf exceptions : origine, opinions, religion, santé, biométrie… Le numéro national d'identification et la biométrie exigent une autorisation de l'APDP. | art. 394 et 407 [R-061] | Lue |
| **Décision automatisée** : aucune décision produisant des effets juridiques ou affectant significativement une personne ne peut être prise **sur le seul fondement** d'un traitement automatisé évaluant sa personnalité. **Exception** : décision prise dans le cadre d'un contrat ou prévue par un texte, avec des mesures appropriées, et au minimum la possibilité pour la personne de « **faire valoir utilement son point de vue** ». Le texte ne parle pas expressément d'intervention humaine. | art. 401 [R-061] | Lue ; la CEDEAO (art. 35) pose la même interdiction, sans exception contractuelle [R-063] |
| **Droit à l'explication** : la personne peut demander l'existence d'une décision automatisée et des « **informations utiles concernant la logique sous-jacente** », ainsi que l'importance et les conséquences du traitement. Réponse sous 60 jours. | art. 437 [R-061] | Lue |
| **Analyse d'impact** obligatoire pour l'évaluation systématique par profilage qui débouche sur de telles décisions. | art. 428 [R-061] | Lue |
| **Formalités** : déclaration préalable à l'APDP par défaut. **Autorisation préalable** notamment pour : le transfert vers un État hors CEDEAO (pt 6) ; « les traitements automatisés susceptibles […] d'**exclure des personnes du bénéfice d'un […] contrat** en l'absence de toute disposition législative ou réglementaire » (pt 7). | art. 405 et 407 [R-061] | Lue. Application du pt 7 au scoring = interprétation, non confirmée par l'APDP |
| **Sous-traitant** : le responsable choisit un sous-traitant offrant des garanties suffisantes et signe un contrat écrit qui fixe ses obligations de sécurité et de confidentialité. Le sous-traitant n'agit que sur instruction. Il doit être déclaré à l'APDP. | art. 386 et 409 pt 10 [R-061] | Lue |
| **Transfert hors CEDEAO** : autorisation préalable de l'APDP, qui constate un niveau de protection équivalent. | art. 391 [R-061] | Lue ; la CEDEAO (art. 36) pose un principe voisin : protection suffisante et information préalable de l'autorité [R-063] |
| **Données télécom** : les opérateurs garantissent la confidentialité des données de trafic. Ils ne peuvent les utiliser pour des services à valeur ajoutée qu'avec le **consentement préalable et exprès** de l'abonné, pour une durée déterminée. Leur remise à un tiers pour du scoring n'est pas prévue. | art. 12, 33 à 36 [R-061] | Lue (application au scoring = interprétation) |
| **Secret bancaire** : toute personne liée à un établissement agréé y est tenue. **Dérogation** : transmission possible au tiers à qui l'établissement confie des « **fonctions opérationnelles** » par un contrat de prestation de services, ou avec l'**autorisation expresse** du client. Le destinataire reste tenu à la confidentialité. Les émetteurs de monnaie électronique sont soumis au même secret. **Les SFD relèvent d'un autre texte** (loi microfinance, non lue). | loi bancaire n°2024-14 du 02/09/2024, art. 68 et définition 37 [R-059] | Lue |
| **Sous-traitance bancaire** : approbation préalable du contrat par l'organe délibérant ; clauses d'accès pour la Commission bancaire, de sécurité et de confidentialité ; **toutes les données doivent être disponibles dans l'UMOA**, y compris les serveurs qui les stockent et les applications (à défaut, serveurs de secours dans l'Union) ; **tout projet de contrat doit être soumis au Secrétariat général de la Commission bancaire** avant sa mise en œuvre. Aucune règle propre au « cloud » n'a été trouvée. | circulaire n°04-2017/CB/C, art. 33 à 36 [R-033] ; définition de l'externalisation, circulaire n°03-2017/CB/C, art. 3 [R-034] | Lue (vigueur 2026 non vérifiée ; maintenue par l'art. 256 de la loi 2024-14 si elle n'est pas contraire) |
| La Commission bancaire peut contrôler sur place les « prestataires de services externalisés ». | loi 2024-14, art. 106 [R-059] | Lue |
| **Partage des données de compte** : les agrégateurs de comptes n'agissent que sur consentement explicite. Tout prestataire de paiement qui gère des comptes en ligne doit ouvrir une interface d'accès aux prestataires d'information sur les comptes, selon des modalités fixées par la BCEAO. | Instruction n°001-01-2024, art. 30 et 31 [R-048] ; loi 2024-14, art. 251 [R-059] | Lue (modalités BCEAO non trouvées) |

**Ce que la loi permet pour la question 22 (synthèse, interprétation à faire valider).** Un prestataire qui développe un outil de scoring pour une banque béninoise peut recevoir les données de la banque à quatre conditions :
1. un **contrat de prestation** qui couvre le secret bancaire (art. 68) et les obligations du sous-traitant (art. 386) ;
2. l'**hébergement des données et des applications dans l'UMOA**, ou à défaut des serveurs de secours dans l'Union avec réplication complète, et la **soumission préalable du contrat à la Commission bancaire** si la fonction est « essentielle ou importante » (circulaire 04-2017, art. 33) ;
3. une **déclaration, voire une autorisation, auprès de l'APDP**, faite par la banque en tant que responsable du traitement (art. 405 et 407) ;
4. pour les décisions de crédit, une **possibilité pour le client de faire valoir son point de vue**, et l'**explication de la logique** sur demande (art. 401 et 437).

Un **déploiement chez la banque**, sur ses serveurs et sous son contrôle, réduit fortement ces contraintes (interprétation). Le régime des **données anonymisées** n'a pas été étudié : dans les passages lus, le Code ne parle d'anonymisation que pour les données de trafic des opérateurs (art. 33).

---

## 7. Volet B6 : Bâle II et III, modèles de risque

*Question 9 : quelles exigences de Bâle II et III, appliquées dans l'UMOA, concernent les modèles de risque des banques ?*

| Règle | Texte et article | Statut |
|---|---|---|
| Bâle II et III sont transposés par le **dispositif prudentiel** applicable aux établissements de crédit et aux compagnies financières de l'UMOA, en vigueur au 01/01/2018, avec trois piliers. | Décision n°013/24/06/2016/CM/UMOA, préambule et § 495 [R-032] | Confirmée [R-031], [R-036] |
| **Risque de crédit : approche standard seulement.** Les actifs pondérés sont « déterminés selon l'approche standard » (§ 90). Le texte ne prévoit **aucune approche par notations internes (IRB)**, seulement des notations externes. Un score interne ne sert donc pas au calcul des fonds propres réglementaires. | dispositif § 90 et titre IV [R-032] | Lue. Indices concordants, par absence : le FMI ne mentionne aucun modèle interne [R-015], et la seule modification trouvée ne touche pas au risque de crédit [R-036] |
| La seule modification trouvée, l'**Avis n°010-08-2020** (Décision n°019 du 26/06/2020/CM/UMOA), décale d'un an le calendrier de transition à cause du Covid. Elle ne touche ni au risque de crédit ni aux modèles. Aucune révision vers Bâle III finalisé n'a été trouvée. | Avis BCEAO n°010-08-2020 [R-036] | Lue |
| **Pilier 2** : processus interne d'évaluation des fonds propres (ICAAP) obligatoire, avec des méthodologies d'évaluation du risque de crédit, individuelles et par portefeuille, qui tiennent compte de « l'historique des pertes, des prévisions économiques » ; contrôle de l'intégrité des données. | dispositif § 505, 516 à 530 [R-032] | Lue |
| **Gestion du risque de crédit** : critères d'octroi prudents ; politiques comportant « **un système approprié de notation ou de classement des crédits** » ; capacité de remboursement analysée à l'octroi, puis au moins chaque année ; processus, systèmes, outils et **données** (dont l'historique des pertes, la segmentation) pour évaluer le risque et les provisions ; système de classement **documenté** ; prise en compte d'informations prospectives. | circulaire n°04-2017/CB/C, art. 17 à 24 [R-033] | Lue dans une copie marquée « projet » (mise en ligne en 2018-02), dont l'en-tête porte le numéro définitif et la date d'adoption ; conformité avec la version signée à vérifier. La copie de 2018-03 n'a été lue que pour les art. 1 à 3, 33 à 38 et 57 |
| **Validation des modèles** : aucune obligation explicite de validation indépendante ni de backtesting d'un outil de scoring d'octroi. Ce qui existe : examen annuel, par l'audit interne et les commissaires aux comptes, de l'efficacité des systèmes de mesure des risques (art. 14) ; approbation par l'organe délibérant des **nouveaux produits, processus et systèmes** (art. 32). La seule validation de modèle prévue concerne la valorisation du portefeuille de négociation (art. 43). | circulaire n°04-2017/CB/C, art. 14, 23, 32 et 43 [R-033] | Lue dans la copie « projet » (absence constatée dans les deux textes lus) |

**Conséquence.** La réglementation n'impose pas de validation formelle d'un modèle de scoring, mais elle exige que les **systèmes de notation soient documentés, fondés sur des données fiables et approuvés par la gouvernance**. Une documentation, une validation et un test sur une période postérieure (out-of-time) restent la **bonne pratique** qui rendra l'outil acceptable pour une direction des risques et pour l'audit.

---

## 8. Enseignements croisés

1. **La cible « particuliers » simplifie la définition du défaut** (B1 et B6). Pour un particulier, une banque applique un seuil de **90 jours** et un défaut **par crédit** (clientèle de détail) [R-031], [R-032]. Le FMI juge la définition de l'UMOA plus souple que le standard international à 90 jours, à cause du seuil de 180 jours pour les PME et le secteur public, et estime que les créances en souffrance déclarées peuvent être sous-estimées [R-015]. Pour les particuliers, le seuil réglementaire est déjà de 90 jours. Une variable cible « 90 jours d'impayé sur le crédit » serait donc à la fois **réglementaire et comparable au standard international** (interprétation).
2. **Le crédit digital tel qu'il est tarifé se heurte à deux textes** (B2 et B3). Le TEG inclut les frais [R-043] et le plafond est de 14 ou 24 % [R-040], ce qui rend les frais de 9 à 14 % sur quelques jours difficilement compatibles. Par ailleurs, l'émetteur ne peut pas prêter lui-même [R-047]. Aucun texte propre au crédit digital ne résout cette tension (L-r2-1). Selon une lecture littérale de l'art. 7 de la loi 2024-15, à faire valider par un juriste, c'est un **risque juridique** pour quiconque y contribue sciemment, y compris un fournisseur de scoring.
3. **Les banques ont l'obligation de noter leurs crédits, mais pas de valider leurs modèles** (B6). La circulaire 04-2017 exige un système de notation documenté [R-033] (copie « projet » lue), et l'approche standard rend les modèles internes inutiles pour les fonds propres [R-032]. Un outil de scoring d'octroi répond donc à une **exigence de gestion des risques**, pas à une exigence de capital. Cela situe la valeur ajoutée du projet du côté de la qualité de l'octroi.
4. **Les données circulent par la banque, pas par le prestataire** (B4 et B5). Selon notre lecture (interprétation), le bureau de crédit, le secret bancaire, le Code du numérique et la circulaire sur la sous-traitance placent tous la banque comme seul responsable et seul utilisateur. Le prestataire n'agit que pour son compte, sous contrat, avec des données hébergées dans l'UMOA. Cela favorise un **déploiement chez la banque** plutôt qu'un service centralisé (Q-10).
5. **Les règles des SFD sont plus incertaines que celles des banques** (B1, B3 et B5). Une nouvelle loi béninoise de 2025 n'a pas pu être lue [R-050], et le texte qui fonde la « norme de 3 % » n'a pas été trouvé. Cibler d'abord les banques, comme l'oriente Daniela, repose donc sur un cadre **mieux établi**.

---

## 9. Recommandations

Aucune source n'étant encore vérifiée ensemble, ces recommandations préparent le point de décision 1 sans le trancher.

1. **Définition du défaut (Q-03)** : retenir pour les particuliers en banque « **au moins une échéance impayée depuis plus de 90 jours sur le crédit** », plus les cas de non-recouvrement probable si les données le permettent. Fondement : Instruction 026-11-2016, art. 8 et 11 [R-031]. Confiance haute (règle confirmée). *Alimente : Q-03, la variable cible du modèle (P5), la section « définitions » du PRD.*
2. **Traiter les créances restructurées comme un événement à part**, à ne pas confondre avec un retour au sain. Une restructuration est une créance en souffrance au sens réglementaire (art. 5) [R-031]. Le modèle devra trancher s'il la compte comme un défaut : à décider en P2, avec un professionnel. Confiance moyenne.
3. **Écarter le nano-crédit digital à frais élevés comme cible directe**, tant qu'un juriste n'a pas confirmé sa compatibilité avec le taux d'usure (TEG frais compris, art. 3 et 7 de la loi 2024-15) [R-043], [R-040]. Confiance moyenne. *Alimente : Q-01, l'analyse de risque du product brief.*
4. **Concevoir l'outil comme un système de notation pour l'octroi, documenté et validable**, pas comme un modèle de capital (approche standard seule) [R-032], [R-033]. Il faudra prévoir la documentation, l'explication des décisions (art. 437) et la possibilité pour le client de faire valoir son point de vue (art. 401) [R-061]. Confiance haute pour l'approche standard ; moyenne pour la circulaire (copie « projet » lue) et pour le Code du numérique (version adoptée lue). *Alimente : PRD (exigences non fonctionnelles), architecture.*
5. **Privilégier un déploiement chez la banque, avec des données hébergées dans l'UMOA**, et préparer le contrat de prestation (secret bancaire, sous-traitant, Commission bancaire) [R-059], [R-061], [R-033]. Confiance moyenne (interprétation). *Alimente : Q-10, architecture (P4).*
6. **Mettre à jour les documents du projet** :
   - la « norme de 3 % » des SFD doit être présentée comme une norme de référence de la BCEAO, pas comme une norme prudentielle [R-037], [R-065] ;
   - le plafond d'usure pour les banques est de 14 % depuis le 01/06/2026, et non plus de 15 % [R-040].

   Ces corrections concernent notamment le glossaire et l'axe A (proposition, non appliquée).
7. **Préparer le guide d'entretien (P1-T4) avec les questions juridiques ouvertes** : pratique réelle des banques sur les restructurations, transmission des rapports du bureau de crédit à un prestataire, déclaration à l'APDP des traitements de scoring, et position des banques prêteuses sur le coût du nano-crédit.

---

## 10. Questions ouvertes

| # | Question | Pourquoi elle reste ouverte | Pour y répondre |
|---|---|---|---|
| QO-B1 | Que contient la loi béninoise n°2025-14 sur la microfinance (abrogation de la loi 2012-14, contrôle des grandes IMF, secret, bureau de crédit, usure) ? | Texte officiel scanné, sans couche texte | Lecture visuelle ou OCR du PDF du SGG ; Journal officiel ; ANSSFD |
| QO-B2 | La version promulguée du Code du numérique diffère-t-elle de la version adoptée (art. 386, 389, 391, 401, 407, 437) ? | PDF officiel de 51 Mo non téléchargé | Téléchargement complet depuis sgg.gouv.bj ; décision de la Cour constitutionnelle de 2017 |
| QO-B3 | L'APDP a-t-elle une doctrine sur le scoring de crédit (autorisation au titre de l'art. 407 pt 7, norme simplifiée) ? | Non recherché | Site de l'APDP, demande directe |
| QO-B4 | Quel texte fonde la « norme de 3 % » des SFD ? | Annexe de l'Instruction 020-12-2010 illisible | Copie lisible de l'annexe ; question à la BCEAO |
| QO-B5 | Les perceptions forfaitaires (art. 4) existent-elles, et qui les fixe ? | Loi uniforme sur l'usure non trouvée ; sources contradictoires | Recueil BCEAO « conditions de banque » ; décrets béninois 2003-023 et 2020-072 |
| QO-B6 | Un texte encadre-t-il le crédit digital, la transparence tarifaire ou la protection des clients (au-delà de la gratuité de 2014 et des réclamations de 2020) ? | Aucun texte trouvé | Circulaire 002-2020/CB/C ; site de la BCEAO ; entretiens |
| QO-B7 | Le texte de la loi béninoise 2016-36 sur le bureau de crédit est-il identique à la loi uniforme (art. 53, 59, 60) ? | Texte introuvable sur le SGG | BCEAO, Creditinfo, Journal officiel |
| QO-B8 | Un rapport du bureau de crédit peut-il être transmis au prestataire technique d'une banque ? | La loi est muette | Question à la BCEAO ou à Creditinfo ; art. 59 (« autre motif approuvé par la Banque Centrale ») |
| QO-B9 | Quand les banques basculeront-elles en IFRS (et IFRS 9) ? Une décision UMOA de 2022 existe-t-elle ? | Textes non trouvés | Site de la BCEAO et de l'AMF-UMOA |
| QO-B10 | Les pages 4 et 5 de la loi 2024-15 (abrogation, entrée en vigueur) et la méthode d'annualisation du TEG | Pages scannées ; aucune méthode trouvée | Lecture visuelle du PDF ; instruction BCEAO sur le TEG |
| QO-B11 | Quel est le régime de l'agent bancaire, et un émetteur ou une fintech peut-il distribuer le crédit d'une banque ? | Non trouvé | Recueil BCEAO ; entretiens |

---

## 11. Sources utilisées

Les détails (lien, date de consultation, statut de vérification) sont dans la [bibliographie](../../REFERENCES.md). Toutes ont été consultées le 08/10/2026. [R-015] avait déjà été ajouté pour l'axe A.

| ID | Ce qu'elle appuie | Éditeur | Publication | Type | Confiance |
|---|---|---|---|---|---|
| [R-015] | Seconde source : 90/180 jours, non-recouvrement probable, pas d'IFRS 9, pas d'IRB | FMI | 2026-05 | primaire | haute |
| [R-031] | Défaut, classement, restructurées, contagion, provisionnement des banques | BCEAO | 2016-11 | primaire | haute |
| [R-032] | Dispositif prudentiel : Bâle, approche standard, clientèle de détail, pilier 2 | Conseil des ministres de l'UMOA / BCEAO | 2016-06 | primaire | haute |
| [R-033] | Gestion des risques : notation des crédits, données, externalisation | Commission bancaire de l'UMOA | 2017-09 | primaire | haute (vigueur 2026 non vérifiée) |
| [R-034] | Contrôle interne : définition de l'externalisation | Commission bancaire de l'UMOA | 2017-09 | primaire | haute |
| [R-035] | Guide d'application du PCB révisé : seconde source sur 026-11-2016, définition des PME, IFRS par l'OHADA | BCEAO | 2017-12 | primaire | haute |
| [R-036] | Avis 010-08-2020 : modification du calendrier seulement | BCEAO | 2020-08 | primaire | haute |
| [R-037] | Recueil des textes SFD : loi uniforme (art. 44), Instr. 010-08-2010, Instr. 020-12-2010 | BCEAO | 2017-11 | primaire | haute |
| [R-038] | Instruction 007-06-2010 : seuil de 2 milliards FCFA | BCEAO | 2010-06 | primaire | haute (vigueur probable) |
| [R-039] | Référentiel comptable des SFD : défaut et provisions | BCEAO | 2009 | primaire | haute (édition 2009) |
| [R-040] | Décision n°19 : taux d'usure 14 % et 24 % | Conseil des ministres de l'UMOA | 2026-01 | primaire | haute |
| [R-041] | Avis BCEAO 007-12-2025 sur le taux d'usure | BCEAO | 2026-01 | primaire | haute |
| [R-042] | Communiqué du Conseil des ministres : 15 % devient 14 %, 24 % maintenu | BCEAO | 2025-12 | primaire | haute |
| [R-043] | Loi béninoise 2024-15 sur l'usure : TEG, perceptions forfaitaires, sanctions | SGG Bénin | 2024-05 | primaire | haute (pages 4-5 non lues) |
| [R-044] | Seconde source sur la Décision n°19 et le TEG | Financial Afrik | 2026-07 | secondaire | haute |
| [R-045] | FAQ usure des SFD (2013, périmée) | BCEAO | inconnue | secondaire | moyenne |
| [R-046] | Taux de 18 et 27 % annoncés en 2024 (infirmé) | La Nouvelle Tribune | 2024-05 | secondaire | basse |
| [R-047] | Émetteurs de monnaie électronique : interdiction du crédit, cantonnement | BCEAO | 2015-05 | primaire | haute |
| [R-048] | Services de paiement : interdiction du crédit, agent bancaire, agrégateurs | BCEAO | 2024-01 | primaire | haute (date de signature en blanc) |
| [R-049] | Loi béninoise 2012-14 sur les SFD (art. 44) | SGG Bénin | 2012-03 | primaire | moyenne (OCR dégradé, vigueur douteuse) |
| [R-050] | Loi béninoise 2025-14 sur la microfinance (existence) | SGG Bénin | 2025-07 | primaire | basse (scan illisible) |
| [R-051] | Adoption de la loi 2025-14, contenu général | Benin Web TV | 2025-06 | secondaire | moyenne |
| [R-052] | Loi uniforme BIC, Instruction 002-01-2015 | BCEAO | 2013-06 | primaire | haute |
| [R-053] | Cadre légal du BIC, consentement | BCEAO | inconnue | primaire | haute |
| [R-054] | Transmission du projet de loi BIC (2014) | SGG Bénin | 2014-11 | primaire | haute |
| [R-055] | Loi 2020-08 : modification de la loi BIC 2016-36 | SGG Bénin | 2020-04 | primaire | haute (article 1er) |
| [R-056] | Décret 2020-198 : référence de la loi 2016-36 | SGG Bénin | 2020 | primaire | haute (visas) |
| [R-057] | Modification de 2020 de l'art. 53 (presse) | Financial Afrik | 2020-06 | secondaire | moyenne |
| [R-058] | Creditinfo West Africa : agrément, données des grands facturiers, scoring | Creditinfo West Africa | 2024-12 | primaire | moyenne |
| [R-059] | Loi bancaire 2024-14 : secret et dérogations, BIC, contrôles, interface de partage | République du Bénin (OQSF) | 2024-09 | primaire | haute (OCR) |
| [R-060] | Vote des lois bancaire, usure et affacturage le 29/04/2024 | Assemblée nationale du Bénin | 2024-04 | primaire | haute |
| [R-061] | Code du numérique, Livre V et Livre I (version adoptée) | Assemblée nationale du Bénin | 2017-06 | primaire | haute (version adoptée) |
| [R-062] | Loi 2020-35 modifiant le Code du numérique | SGG Bénin | 2021-01 | primaire | haute |
| [R-063] | Acte additionnel CEDEAO sur les données personnelles | Commission de la CEDEAO | 2010-02 | primaire | haute |
| [R-064] | Ratification de la Convention de Malabo par le Bénin | Osiris | 2024-01 | secondaire | moyenne |
| [R-065] | « Norme maximale de 3 % » des SFD (fin 2023) | BCEAO | 2024-04 | primaire | haute (non normatif) |
| [R-066] | Seuil de 5 % en 2009 | BCEAO | 2009 | primaire | haute |
| [R-067] | Seconde source sur 026-11-2016 | Carrefour Compta | 2018-06 | secondaire | moyenne |
| [R-068] | Directive 01/2020/CM/UEMOA (passage en perte) | Village de la Justice | 2022-01 | secondaire | moyenne |
| [R-069] | Protection des consommateurs dans l'UMOA : pas de disposition dans le traité | Financial Afrik | 2019-02 | secondaire | moyenne |
| [R-070] | Gratuité de 19 services bancaires (2014) | Financial Afrik | 2015-10 | secondaire | moyenne |
| [R-071] | Gratuité de services bancaires : liste approuvée | Abidjan.net | 2014-05 | secondaire | moyenne |
| [R-072] | Lois sur l'usure : mention obligatoire du TEG | CMS | 2015-12 | secondaire | moyenne |
| [R-073] | Fin de la transition des services de paiement au 31/08/2025 | Agence Ecofin | 2025-06 | secondaire | moyenne |
| [R-074] | Instruction 001-01-2024 : agréments et délai | Digital Mag CI | 2025 | secondaire | moyenne |
| [R-075] | Stratégie régionale d'inclusion financière 2025-2030 | AllAfrica (APS) | 2026-07 | secondaire | moyenne |
| [R-076] | Débat sur le cadre prudentiel du crédit des opérateurs et fintechs | Senego | 2026-08 | secondaire | basse |
| [R-077] | Formations BCEAO à IFRS 9 | COFEB (BCEAO) | 2021-09 | primaire | moyenne |
| [R-078] | Appel à consultants pour la transition vers les IFRS | bidsfactory (agrégateur) | 2026-05 | secondaire | basse (non retrouvé sur le site de la BCEAO) |
| [R-079] | Circulaire 002-2020/CB/C sur les réclamations (existence) | Financial Afrik | 2021-02 | secondaire | basse (extrait seulement) |

---

## 12. Dates de revérification

Pour une règle juridique, la méthode demande de vérifier sa vigueur à chaque usage déterminant. Le calcul ci-dessous part donc de la date de vérification (10/2026), avec un délai de 6 mois. Les acteurs (bureau de crédit agréé) ont un délai de 18 mois.

| Affirmation clé | À revérifier le |
|---|---|
| Bureau de crédit agréé : Creditinfo West Africa (grille 2025) | **déjà dépassé** (01/06/2026) |
| Règles bancaires de défaut, de classement et de provisionnement (Instr. 026-11-2016) | 01/04/2027 |
| Taux d'usure de 14 % et 24 % (Décision n°19) | 01/04/2027 |
| Statut des SFD : loi 2025-14 à la place de la loi 2012-14 | 01/04/2027 |
| Code du numérique, Livre V | 01/04/2027 |
| Absence de texte sur le crédit digital | 01/04/2027 |
| Transition du Plan comptable bancaire vers les IFRS | 01/04/2027 |

Revérifications prioritaires :
- **l'agrément du bureau de crédit pour 2026**, déjà dépassé ;
- **avant toute décision**, les questions ouvertes QO-B1 (loi microfinance 2025) et QO-B2 (Code du numérique promulgué).

---

## 13. Termes proposés pour le glossaire

Ces termes sont à ajouter ou à corriger dans le [glossaire](../../GLOSSAIRE.md) après validation par Daniela. Le glossaire n'a pas été modifié.

| Terme | Définition proposée | Sens à distinguer | Source |
|---|---|---|---|
| Défaut (sens réglementaire, banques) | Créance douteuse ou litigieuse : au moins une échéance impayée depuis plus de 90 jours (180 jours pour PME/PMI, États et organismes publics), ou non-paiement jugé probable | Académique : la variable cible du modèle. Pratique : à confirmer en entretien | [R-031] art. 8 |
| Créance en souffrance (**correction** de l'entrée actuelle) | Créances restructurées + créances douteuses ou litigieuses | L'entrée actuelle est juste sur la composition ; le seuil de 180 jours vise les PME/PMI, l'État et les organismes publics, pas tous les « autres » | [R-031] art. 5 et 8 |
| Créance douteuse ou litigieuse | Créance dont une échéance est impayée depuis plus de 90 jours (ou 180), ou dont le non-paiement est probable | | [R-031] art. 8 |
| Créance restructurée | Créance renégociée par des concessions envers un débiteur en difficulté ; retour en sain après 1 an sans impayé, puis 2 ans de probation | Faut-il la compter comme un défaut dans le modèle ? À décider | [R-031] art. 6 et 7 |
| Créance irrécouvrable | Créance aux droits éteints, ou douteuse non recouvrée au terme du 5e exercice | | [R-031] art. 13 |
| Contagion | Déclassement de tous les encours d'un débiteur dès qu'une créance devient douteuse ; ne s'applique pas à la clientèle de détail | Défaut « par client » (entreprises) contre défaut « par crédit » (détail) | [R-031] art. 11 |
| Clientèle de détail | Particulier ou PME/PMI, exposition d'au plus 0,2 % du portefeuille de détail et d'au plus 150 millions FCFA, consentement au partage avec le bureau de crédit | Pondérée à 75 % | [R-032] § 135 et 137 |
| PME/PMI (sens réglementaire) | Entreprise immatriculée dont le chiffre d'affaires hors taxes annuel n'excède pas 1 milliard FCFA | Pas de critère d'effectif | [R-035] (Décision n°29 du 29/09/2015) |
| Non-recouvrement probable (« unlikely to pay ») | Risque que le débiteur ne paie pas, indépendamment de tout impayé (procédure collective, faillite…) | | [R-031] art. 8 et 9 |
| Provisionnement calendaire | Provisions fixées par l'ancienneté du déclassement (banques : 20 %, 50 % à 3 mois, 100 % à 9 mois ; SFD : 40 %, 80 %, 100 %) | Contraire du modèle des pertes attendues d'IFRS 9 | [R-031] art. 16 ; [R-039] |
| IFRS 9 | Norme comptable internationale de provisionnement fondée sur les pertes attendues (trois stades) | Non appliquée par les banques de l'UMOA en 2026 | [R-015] |
| Norme de 3 % (SFD) (**correction** de l'entrée actuelle) | Norme de référence citée par la BCEAO pour le taux brut de dégradation du portefeuille des SFD | **Pas une norme prudentielle** des règles des SFD ; base juridique non trouvée | [R-037], [R-065] |
| Taux d'usure | Taux maximum qu'un prêt peut atteindre, TEG compris : 14 % l'an pour les banques, 24 % pour les établissements financiers et les IMF (depuis le 01/06/2026) | | [R-040] art. 2 |
| TEG (taux effectif global) | Coût total du crédit, frais et rémunérations de toute nature inclus, impôts exclus | Taux nominal (intérêt seul) : sous-estime le coût | [R-043] art. 3 |
| Approche standard (Bâle) | Calcul des fonds propres avec des pondérations fixées par le régulateur | Seule approche autorisée dans l'UMOA ; l'approche IRB (modèles internes) n'existe pas | [R-032] § 90 |
| ICAAP (pilier 2) | Processus interne d'évaluation de l'adéquation des fonds propres | | [R-032] § 505 |
| Article 44 (SFD) | Article de la loi sur les SFD qui soumet au contrôle de la BCEAO et de la Commission bancaire les SFD dont l'activité atteint un seuil fixé par instruction : 2 milliards FCFA de dépôts ou de crédits deux exercices de suite (Instruction 007-06-2010, art. 2) | Loi béninoise de 2012 peut-être remplacée en 2025 | [R-037], [R-038] |
| Émetteur de monnaie électronique (EME) (**complément**) | Établissement agréé pour émettre de la monnaie électronique ; **interdit de crédit**, mais peut verser le crédit d'une banque ou d'un SFD | | [R-047] art. 5 |
| Bureau d'information sur le crédit (BIC) (**complément** de l'entrée actuelle) | Organisme agréé qui collecte l'historique de crédit et de paiement et délivre des rapports aux établissements, avec le consentement préalable du client ; consultation obligatoire avant tout crédit pour les banques et SFD supervisés | Un seul bureau en activité : Creditinfo West Africa | [R-052] art. 53 et 60 ; [R-058] |
| Utilisateur (BIC) | Établissement lié par contrat au bureau, qui lui fournit des données et peut le consulter | Un prestataire de scoring n'en est pas un | [R-052] art. 1er et 36 |
| Décision individuelle automatisée | Décision prise sur le seul fondement d'un traitement automatisé ; interdite au Bénin sauf contrat ou texte, avec droit de faire valoir son point de vue | Pas de « droit à l'intervention humaine » au sens strict | [R-061] art. 401 |
| Sous-traitant (données) | Personne qui traite des données pour le compte du responsable du traitement, sous contrat écrit et sur instruction | La banque est le responsable du traitement, le prestataire le sous-traitant | [R-061] art. 386 |
| APDP | Autorité de protection des données à caractère personnel du Bénin (8 membres) | | [R-062] |
| Externalisation | Fait de confier durablement à un tiers des tâches opérationnelles essentielles ou importantes ; soumise à la Commission bancaire et à l'hébergement dans l'UMOA | | [R-033] art. 3 et 33 ; [R-034] |
| Secret bancaire | Obligation de confidentialité des établissements agréés ; dérogations pour un prestataire chargé de fonctions opérationnelles ou avec l'accord exprès du client | | [R-059] art. 68 |
