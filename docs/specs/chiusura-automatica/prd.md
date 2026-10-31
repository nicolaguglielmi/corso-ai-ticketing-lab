# PRD: chiusura automatica dei ticket risolti

Esempio di PRD prodotto con la skill /prd di riferimento sulla richiesta docs/richieste/chiusura-automatica.md. Usatelo come modello di forma, non come soluzione del lab sulla classificazione.

## Problema

Il processo prevede che un ticket risolto senza risposta per 5 giorni lavorativi passi a chiuso. Oggi si fa a mano e viene dimenticato.

## Obiettivo

Ogni notte i ticket risolti da più di 5 giorni lavorativi senza risposta del richiedente passano a chiuso, con un commento automatico.

## Criteri di accettazione

| ID | Criterio | Test |
| --- | --- | --- |
| AC-1 | Dato un ticket risolto da 6 giorni lavorativi senza commenti del richiedente, quando gira la chiusura, allora diventa chiuso | `risolto_da_6_giorni_viene_chiuso` |
| AC-2 | Dato un ticket risolto da 4 giorni lavorativi, quando gira la chiusura, allora resta risolto | `risolto_da_4_giorni_resta_risolto` |
| AC-3 | Dato un ticket risolto con un commento del richiedente dopo la risoluzione, quando gira la chiusura, allora resta risolto | `risposta_del_richiedente_blocca_la_chiusura` |
| AC-4 | Dato un ticket chiuso in automatico, allora ha un commento "Chiuso automaticamente dopo 5 giorni lavorativi senza risposta" | `chiusura_automatica_aggiunge_commento` |
| AC-5 | I sabati e le domeniche non contano come giorni lavorativi | `weekend_non_conta_nei_5_giorni` |

## Casi di errore

| ID | Situazione | Comportamento |
| --- | --- | --- |
| ERR-1 | Il job si interrompe a metà | Alla ripartenza chiude solo i ticket ancora risolti, senza duplicare commenti |

## Domande aperte (da far emergere in demo)

- I festivi contano? Quale calendario?
- Il richiedente viene avvisato prima della chiusura?
- Il campo "data di risoluzione" oggi non esiste: serve aggiungerlo.

## Issue risultanti

1. Aggiungi la data di risoluzione al cambio di stato (AC-1, AC-2).
2. Funzione di calcolo dei giorni lavorativi (AC-5).
3. Job di chiusura con commento automatico e idempotenza (AC-1, AC-3, AC-4, ERR-1).
