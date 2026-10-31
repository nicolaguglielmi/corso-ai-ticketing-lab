---
name: review-spec
description: Rilegge un PRD e segnala criteri non verificabili, casi di errore mancanti e contraddizioni con docs/. Usala prima di passare al design o per rivedere la specifica di un'altra persona.
---

# Revisione di una specifica

## Input

Il percorso di un PRD.

## Passi

1. Leggi il PRD e i file di `docs/` citati o pertinenti.
2. Per ogni criterio di accettazione verifica: è nella forma dato / quando / allora? Ha una soglia misurabile? Ha il nome di un test?
3. Verifica che ci sia almeno un caso di errore per ogni dipendenza esterna.
4. Cerca contraddizioni con `docs/processo-supporto.md` e `docs/categorie.md`.

## Output

Una tabella in chat: ID del criterio o sezione, problema, proposta di riscrittura. In fondo, un giudizio in una riga: pronto per il design oppure no.

## Regole

- Non modificare il PRD: proponi, non correggere.
- Se non trovi problemi, dillo in una riga senza inventarne.
