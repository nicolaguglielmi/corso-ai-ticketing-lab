---
name: prd
description: Trasforma una richiesta in linguaggio naturale in un PRD con criteri di accettazione verificabili. Usala quando arriva una nuova richiesta di funzionalità, prima di qualsiasi design o codice.
---

# PRD da una richiesta

## Input

Una richiesta in linguaggio naturale, scritta nel messaggio o in un file di `docs/richieste/`.

## Passi

1. Leggi la richiesta e `docs/processo-supporto.md`, `docs/categorie.md`: le regole di business stanno lì.
2. Controlla se la richiesta dice chi sono gli attori, quale problema misurabile risolve, i vincoli (tempi, costi, dati) e come si capisce che funziona.
3. Se manca anche uno di questi elementi, **fermati e fai al massimo 5 domande**, numerate. Non inventare numeri, soglie o attori.
4. Con le risposte, compila `docs/templates/prd.md` e scrivi `docs/specs/<feature>/prd.md` (`<feature>` in minuscolo, con trattini).
5. Ogni criterio di accettazione è nella forma dato / quando / allora e ha accanto il nome di un test, per esempio `ticket_senza_testo_restituisce_errore`.
6. Rileggi i criteri: se uno contiene "veloce", "semplice", "intuitivo", "corretto" senza soglia, riscrivilo con un numero o chiedi la soglia.

## Output

`docs/specs/<feature>/prd.md` e un riepilogo in chat: criteri scritti, domande ancora aperte.

## Regole

- Non scrivere design, codice o issue: è compito di altre skill.
- Almeno un caso di errore per ogni dipendenza esterna (servizi, modelli, rete).
- Se la richiesta contraddice `docs/`, segnalalo nelle domande aperte.
