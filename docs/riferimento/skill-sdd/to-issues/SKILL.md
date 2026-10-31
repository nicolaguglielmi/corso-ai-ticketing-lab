---
name: to-issues
description: Scompone un design in issue piccole e tracciabili ai criteri del PRD. Usala dopo /to-design, prima di iniziare a implementare.
---

# Issue da un design

## Input

La cartella di una feature, per esempio `docs/specs/classificazione/`, con `prd.md` e `design.md`.

## Passi

1. Leggi PRD e design.
2. Scomponi il lavoro in issue da al massimo mezza giornata ciascuna. Se un'issue è più grande, dividila.
3. Per ogni issue usa il formato di `docs/templates/issue.md`: titolo all'imperativo, criteri del PRD coperti, test da scrivere prima, condizioni di "fatto".
4. Crea un'issue separata per ogni caso di errore del PRD (ERR-n), compreso il caso in cui un servizio esterno non risponde.
5. Alla fine aggiungi una tabella di copertura: ogni AC-n ed ERR-n del PRD con le issue che lo coprono. Se un criterio non è coperto, segnalalo.

## Output

`docs/specs/<feature>/issues.md`, in ordine di esecuzione.

## Regole

- Non scrivere codice.
- Ogni issue ha almeno un test con un nome preciso.
- Nessun criterio del PRD può restare senza issue.
