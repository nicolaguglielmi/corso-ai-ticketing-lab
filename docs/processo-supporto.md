# Processo di supporto interno

## Ciclo di vita di un ticket

| Stato | Significato | Stati successivi ammessi |
| --- | --- | --- |
| aperto | Ticket ricevuto, non ancora preso in carico | in_lavorazione |
| in_lavorazione | Un operatore ci sta lavorando | in_attesa, risolto |
| in_attesa | Serve un'informazione dal richiedente o da un fornitore | in_lavorazione, risolto |
| risolto | Soluzione comunicata, in attesa di conferma | chiuso, in_lavorazione |
| chiuso | Ticket concluso | nessuno |

Regole:

1. Un ticket **chiuso è definitivo**. Se il problema si ripresenta si apre un nuovo ticket che cita il precedente.
2. Un ticket aperto non si chiude senza passare da `in_lavorazione`: serve sempre una presa in carico.
3. Un ticket risolto senza risposta del richiedente per 5 giorni lavorativi passa a chiuso.

## Priorità e tempi di risposta

| Priorità | Quando | Prima risposta | Risoluzione |
| --- | --- | --- | --- |
| P1 | Blocco totale di un servizio, più persone coinvolte | 30 minuti | 4 ore |
| P2 | Blocco per una persona o un reparto, senza alternativa | 2 ore | 1 giorno lavorativo |
| P3 | Disservizio con alternativa disponibile | 1 giorno lavorativo | 3 giorni lavorativi |
| P4 | Richiesta, informazione, piccola modifica | 2 giorni lavorativi | 5 giorni lavorativi |

## Risposte al richiedente

Ogni risposta al richiedente è scritta o approvata da un operatore. Nessuna risposta parte in automatico.

## Dati personali

Nei ticket possono comparire dati personali (email, telefono, a volte dati sanitari per richieste di postazioni adattate). Non vanno copiati nei log applicativi né inoltrati a servizi esterni senza autorizzazione.
