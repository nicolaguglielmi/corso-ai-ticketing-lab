---
name: to-design
description: Produce il design tecnico a partire da un PRD approvato in docs/specs. Usala dopo /prd, quando il PRD ha criteri di accettazione verificabili.
---

# Design da un PRD

## Input

Il percorso di un PRD, per esempio `docs/specs/classificazione/prd.md`.

## Passi

1. Leggi il PRD. Se non ci sono almeno 3 criteri di accettazione verificabili o non c'è nessun caso di errore, **fermati** e dì cosa manca: si torna a `/prd`.
2. Leggi `CLAUDE.md` e i file di `app/` coinvolti, per proporre modifiche coerenti con il codice esistente.
3. Compila `docs/templates/design.md` e scrivi `design.md` nella stessa cartella del PRD.
4. Nella tabella degli errori, collega ogni errore al criterio ERR-n o AC-n del PRD.
5. Nella sezione dati e privacy, indica quali campi del ticket escono verso servizi esterni e quali finiscono nei log.

## Output

`docs/specs/<feature>/design.md` e un riepilogo in chat con le decisioni aperte.

## Regole

- Non scrivere codice.
- Ogni componente nuovo deve avere un motivo nella tabella delle decisioni.
- Se una scelta dipende da informazioni che non hai (volumi, costi), mettila tra le decisioni aperte invece di sceglierla tu.
