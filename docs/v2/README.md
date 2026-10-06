# Documentation V2 : Scoring de crédit adapté au contexte UEMOA

Ce dossier contient toute la documentation de la version 2 du projet.
La documentation de la V1 est conservée dans [`docs/v1/`](../v1/) comme référence historique.

**Porteuse du projet :** Daniela Samo
**Démarrage V2 :** 25 septembre 2026

---

## Par où commencer ?

| Si tu veux... | Ouvre |
|---|---|
| Savoir où on en est et ce qui vient ensuite | [00_FICHE_SUIVI.md](00_FICHE_SUIVI.md) |
| Relire la vision, les motivations et le cadrage de départ | [01_CADRAGE_INITIAL.md](01_CADRAGE_INITIAL.md) |
| Comprendre les limites de la V1 et ce qu'il faut corriger | [02_DIAGNOSTIC_V1.md](02_DIAGNOSTIC_V1.md) |
| Retrouver pourquoi une décision a été prise | [CARNET.md](CARNET.md) |
| Vérifier le sens exact d'un terme | [GLOSSAIRE.md](GLOSSAIRE.md) |
| Retrouver une source | [REFERENCES.md](REFERENCES.md) |
| Suivre l'étude de contexte (P1) | [00_QUESTIONS_DE_RECHERCHE.md](initiative-uemoa-pilote-benin/00_QUESTIONS_DE_RECHERCHE.md) |

## Organisation des documents

```
docs/v2/
├── README.md               Ce fichier : index et règles de documentation
├── 00_FICHE_SUIVI.md       Tableau de bord : phases, tâches, questions ouvertes, journal des sessions
├── 01_CADRAGE_INITIAL.md   Vision, contexte, réponses de cadrage, liens formation et carrière
├── 02_DIAGNOSTIC_V1.md     Analyse critique de la V1 (points forts, défauts, références au code)
├── CARNET.md               Registre des décisions (D-001, D-002, ...) avec justification
├── GLOSSAIRE.md            Termes clés : définitions réglementaire, académique et pratique
├── REFERENCES.md           Bibliographie unique (identifiants R-xxx), sources vérifiées
└── initiative-uemoa-pilote-benin/
    ├── 00_QUESTIONS_DE_RECHERCHE.md   Questions de l'étude P1 et suivi des axes
    └── research-<axe>/, brief-..., prd-...   Livrables produits par BMAD
```

Les livrables BMAD (étude, brief, PRD, architecture) sont rangés dans le dossier de l'initiative active (décision D-008).

## Règles de documentation

1. **Rien ne se perd.** Toute information donnée en séance (idée, contrainte, contact, source) est reportée dans le document concerné le jour même.
2. **Toute décision a une entrée dans le carnet** : ce qui est décidé, pourquoi, les alternatives écartées, qui a validé.
3. **La fiche de suivi est mise à jour à chaque fin de session** (statut des tâches et journal).
4. **Les dates sont absolues** (jj/mm/aaaa), jamais « hier » ou « la semaine prochaine ».
5. **Toute affirmation factuelle sur le contexte (chiffre, loi, acteur) est sourcée et datée.** Sans source, elle est marquée « à vérifier ».
6. **Daniela valide avant toute action** ; c'est elle qui exécute les commandes.

## Versions et Git

| Élément | Emplacement |
|---|---|
| V1 figée | Tag Git `v1.0` (branche `main`) |
| Travaux V2 | Branche Git `v2` |
| Documentation V1 | `docs/v1/` (étude, rapport d'avancement, captures d'écran) |
| Documentation V2 | `docs/v2/` |
