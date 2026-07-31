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


