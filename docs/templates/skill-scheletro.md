Scheletro di una skill di Claude Code. Copiatelo in `.claude/skills/<nome>/SKILL.md` e completatelo. Tenete il file sotto le 60 righe: template ed esempi lunghi vanno in file separati nella stessa cartella.

```markdown
---
name: <nome-della-skill>
description: <quando usarla, in una frase: è il testo che Claude legge per decidere se attivarla>
---

# <Titolo>

## Quando usarla

<una o due righe>

## Input

<cosa deve ricevere: una richiesta, un file, un percorso>

## Passi

1. <primo passo>
2. <se mancano informazioni, fai domande invece di inventare>
3. <scrivi il risultato in un file preciso, partendo dal template>

## Output

<file prodotto e formato>

## Regole

- <cosa non deve fare mai>
```
