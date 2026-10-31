# Stime di costo e latenza per la classificazione

Dati per l'ADR della sessione 3. **Sono valori di esercitazione**, scelti per avere numeri realistici e conti semplici: non sono il listino né le prestazioni di un provider reale. Prima di una decisione vera, si misurano sul provider scelto.

## Volume

| Voce | Valore |
| --- | --- |
| Ticket per giorno lavorativo | 180 |
| Picco orario (8:30-9:30) | 45 ticket |
| Giorni lavorativi al mese | 21 |

## Token per ticket

| Voce | Valore medio |
| --- | --- |
| Token in ingresso (istruzioni del prompt + testo del ticket) | 900 |
| Token in uscita (JSON con proposta e bozza di risposta) | 220 |

## Prezzi di esercitazione

| Voce | Prezzo |
| --- | --- |
| Token in ingresso | 3,00 € per milione |
| Token in uscita | 15,00 € per milione |

## Latenza del modello

| Voce | Valore |
| --- | --- |
| p50 | 2,4 secondi |
| p95 | 7,5 secondi |
| Timeout previsto nel design | 10 secondi |

## Vincoli del product owner

Da `docs/richieste/classificazione-risposte-po.md`:

- conferma di apertura al richiedente in meno di 1 secondo;
- proposta all'operatore entro 1 minuto;
- budget massimo 50 € al mese.

## Formule

- Costo per ticket = token in ingresso × prezzo in ingresso + token in uscita × prezzo in uscita
- Costo mensile = costo per ticket × ticket al giorno × giorni lavorativi
- Latenza vista dal richiedente: con chiamata sincrona include quella del modello, con coda asincrona no.
