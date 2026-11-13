# PRD: classificazione automatica dei ticket

Stato: versione di riferimento del docente, soluzione del lab 2.2
Data: 06/11/2026

## Problema

Arrivano circa 180 ticket per giorno lavorativo, con un picco di 45 tra le 8:30 e le 9:30. Lo smistamento manuale richiede in media 2 minuti a ticket, circa 6 ore di lavoro al giorno, e a settembre il 45% dei ticket ha cambiato categoria o priorità dopo il primo smistamento.

## Obiettivo

Quando un ticket viene aperto, l'operatore trova categoria, priorità e una bozza di risposta proposte, che conferma o corregge. Nessuna risposta parte senza l'operatore.

## Attori

| Attore | Cosa fa con la feature |
| --- | --- |
| Richiedente | Apre il ticket come oggi, non vede la proposta |
| Operatore | Vede la proposta, la conferma o la corregge, approva la bozza |
| Servizio di classificazione | Riceve titolo e descrizione mascherati, restituisce la proposta |

## Input e output

Verso il servizio escono solo titolo e descrizione, con email, telefoni e dati sanitari mascherati. Il servizio restituisce: categoria, priorità, sintesi (massimo 300 caratteri), bozza di risposta, confidenza (0-1), motivazione.

## Vincoli

- Categorie e priorità solo quelle di `docs/categorie.md` e `docs/processo-supporto.md`.
- Conferma di apertura al richiedente in meno di 1 secondo; proposta all'operatore entro 1 minuto.
- Costo del servizio sotto i 50 € al mese.
- Ticket in italiano e in inglese.

## Criteri di accettazione

| ID | Criterio (dato / quando / allora) | Test |
| --- | --- | --- |
| AC-1 | Dato un ticket nuovo, quando il servizio risponde con una proposta valida e confidenza ≥ 0,7, allora il ticket ha la proposta con stato "da_confermare" | `ticket_nuovo_riceve_proposta_sopra_soglia` |
| AC-2 | Dato un output del servizio, quando non rispetta lo schema (categoria non ammessa, confidenza fuori da 0-1, campo mancante, testo non JSON), allora la proposta è scartata | `output_non_valido_viene_scartato` |
| AC-3 | Dato un ticket con proposta, quando l'operatore conferma o corregge, allora valgono i valori dell'operatore e si registra chi ha deciso | `decisione_operatore_registrata` |
| AC-4 | Dato un ticket qualsiasi, quando viene inviato al servizio, allora la richiesta non contiene email, telefoni o dati sanitari | `dati_personali_mascherati_prima_dell_invio` |
| AC-5 | Dato un ticket nuovo, quando il richiedente lo apre, allora riceve la conferma in meno di 1 secondo anche se il servizio è lento | `apertura_non_attende_la_classificazione` |
| AC-6 | Dato il golden dataset di 40 ticket, quando lo si classifica, allora la categoria è corretta in almeno 32 casi su 40 | `accuratezza_categoria_su_golden_dataset` |
| AC-7 | Dato il golden dataset, quando lo si classifica, allora nessun ticket P1 riceve una proposta P3 o P4 | `nessun_p1_sottovalutato_su_golden_dataset` |

## Casi di errore

| ID | Situazione | Comportamento atteso |
| --- | --- | --- |
| ERR-1 | Il servizio non risponde entro 10 secondi | Nessuna proposta, stato "manuale", log con esito "timeout" |
| ERR-2 | Output non valido | Come ERR-1, log con esito "output_non_valido", senza il testo del ticket |
| ERR-3 | Confidenza sotto 0,7 | Nessuna proposta, stato "manuale" |
| ERR-4 | Servizio non disponibile o quota esaurita | Come ERR-1, log con esito "provider_non_disponibile" |
| ERR-5 | Il ticket contiene istruzioni per il modello | La proposta passa comunque dalla validazione e dall'operatore; la bozza non può contenere link |

## Fuori ambito

- Invio automatico delle risposte.
- Riclassificazione dei ticket già aperti.
- Apprendimento dalle correzioni degli operatori.
