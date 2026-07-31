Salut ! Voici le rappel.

## Nommage des branches

**Structure** : `<type>/<description-courte-en-kebab-case>`

| Préfixe | Usage |
|---|---|
| `feature/` | Nouvelle fonctionnalité |
| `fix/` | Correction de bug |
| `hotfix/` | Correction urgente en production |
| `refactor/` | Réorganisation sans changement de comportement |
| `docs/` | Documentation uniquement |
| `chore/` | Tâches techniques (dépendances, config CI) |

Exemples adaptés à ton projet :
```
feature/gestion-dedup-agent-telephone
fix/administration-trigger-mairie-unique
docs/mpd-mise-a-jour
```

**Approche recommandée** : trunk-based, branches courtes parties de `main`, fusionnées rapidement — pas besoin de Git Flow complet (`develop`/`release/`) vu la taille du projet.

## Messages de commit — Conventional Commits

**Structure**

```
<type>(<scope>): <description courte à l'impératif, sans majuscule ni point final>

<corps optionnel : pourquoi ce changement>
```

**Types courants** : `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`

**Le `scope`** = l'app Django ou le module concerné.

Exemples :
```
feat(gestion): ajouter la déduplication des agents par téléphone
fix(securite): corriger le namespace djdt manquant dans urls.py
docs(database): mettre à jour le MPD avec la règle mairie unique
```

**Règles clés** :
- Impératif ("ajouter", pas "ajout de" ni "ajouté")
- Un commit = un changement logique
- Le corps explique le **pourquoi**, pas le **quoi** (le diff montre déjà le quoi)

Besoin d'un message de commit précis pour un changement qu'on vient de faire ?

#####################################

Voici des exemples tirés directement de ton propre projet — plus parlants qu'un exemple générique, puisque tu reconnaîtras le contexte.

## Exemple 1 — Une nouvelle fonctionnalité

**Branche** : `feature/gestion-pipeline-extraction-am`

**Commit** :
```
feat(gestion): ajouter le pipeline d'extraction OCR/parsing des AM

Ajoute extraction.py (OCR via Tesseract, lecture directe Word/PDF) et
parsing.py (extraction des champs par expressions régulières, calibré
sur le gabarit réel des AM). Permet à la commande extraire_document de
transformer une photo/scan en Autorisation structurée.
```

## Exemple 2 — Une correction de bug

**Branche** : `fix/config-debug-toolbar-namespace`

**Commit** :
```
fix(config): enregistrer les URLs de debug_toolbar dans urls.py

Le middleware était actif dans settings/dev.py mais ses URLs n'étaient
jamais incluses, provoquant une NoReverseMatch sur le namespace 'djdt'
à chaque page en mode DEBUG.
```

## Exemple 3 — Une modification de schéma

**Branche** : `feature/gestion-document-model`

**Commit** :
```
feat(gestion): ajouter le modèle Document et la FK obligatoire sur Autorisation

Une Autorisation ne peut désormais exister que si elle découle d'un
Document source (photo/scan/Word) validé -- document_id passe en
unique + not null, cohérent avec le pivot du projet vers l'extraction
de documents existants plutôt que la saisie directe.
```

## Exemple 4 — Une amélioration de robustesse

**Branche** : `fix/gestion-ampliation-dedup-floue`

**Commit** :
```
fix(gestion): brancher find_or_create_ampliation dans extraire_document

La fonction de déduplication approximative (difflib) existait déjà
mais n'était appelée nulle part -- deux ampliations proches ("Gendarmerie"
vs "gendarmeries") créaient donc des doublons au lieu de fusionner.
```

## Exemple 5 — Une tâche de maintenance

**Branche** : `chore/requirements-tesseract-deps`

**Commit** :
```
chore(requirements): ajouter pytesseract, Pillow, pdfplumber, python-docx

Dépendances du pipeline d'extraction. Nécessite aussi le binaire
tesseract-ocr + le pack de langue fra, installé séparément (hors pip).
```

**Le fil conducteur** : chaque message répond à *"pourquoi ce changement a été fait"*, pas juste *"qu'est-ce qui a changé"* — le `git diff` montre déjà le quoi.

