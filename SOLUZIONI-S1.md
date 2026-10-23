# Soluzioni della sessione 1

Questo punto di partenza (`s2-start`) contiene una soluzione di riferimento dei lab della sessione 1. Non è l'unica possibile: confrontatela con il vostro branch `<nome>/s1`.

## Lab 1.1

| Cosa | Dove |
| --- | --- |
| Test per gli endpoint scoperti: modifica, stati, commenti, ricerca, statistiche, cancellazione | `tests/test_flussi.py` |
| Refactoring: la validazione di titolo, descrizione ed email sta in un punto solo | `app/validazione.py` |

## Problemi della sfida corretti

| Problema | Correzione | Test |
| --- | --- | --- |
| SQL injection nella ricerca `q` | Query con parametri al posto della f-string | `test_ricerca_non_permette_sql_injection` |
| Transizioni di stato contrarie al processo | `aperto` passa solo a `in_lavorazione`, `chiuso` è definitivo | `test_aperto_non_si_chiude_senza_presa_in_carico`, `test_chiuso_e_definitivo` |
| Commento su ticket inesistente accettato | Controllo dell'esistenza del ticket, risposta 404 | `test_commento_su_ticket_inesistente_restituisce_404` |
| Validazione email debole | Espressione regolare minima | `test_email_senza_dominio_restituisce_422` |

## Problemi lasciati di proposito

Due problemi restano nel codice perché li affrontiamo nella sessione 6 su sicurezza e privacy:

- il token amministrativo scritto in `app/config.py`;
- il log che stampa l'email del richiedente in `crea_ticket`.

## Lab 1.2

- `CLAUDE.md` di riferimento, sotto le 40 righe.
- `.mcp.json` con il server Git configurato a livello di progetto.
