# Sessione 4: lab

Oggi la specifica della classificazione diventa un componente: prima il design (cosa deve restituire il modello, il primo prompt, cosa succede quando sbaglia), poi il primo codice, scritto test prima, con un provider simulato al posto del modello vero.

Tempo di lab: 50 minuti di lab 3.1, 30 di lab 3.2 e 60 di lab 4.1. Coppie nelle breakout room, una persona scrive e l'altra rivede; ai checkpoint vi scambiate.

| Orario | Attività |
| --- | --- |
| 14:00 | Domande, compiti e dove eravamo |
| 14:10 | Design di un componente IA |
| 14:35 | Demo: con e senza schema, output malformato |
| 14:45 | Lab 3.1: schema della risposta e prompt v1 |
| 15:35 | Plenaria: la tabella degli errori |
| 15:45 | Pausa |
| 15:55 | Lab 3.2: design e issue dei fallback |
| 16:25 | Test prima del codice, con un provider simulato |
| 16:35 | Pausa |
| 16:45 | Lab 4.1: provider simulato e fallback |
| 17:45 | Plenaria, chiusura e compiti |

## Prima di iniziare (5 minuti, dentro il lab 3.1)

Prima fate commit di quello che resta sul branch `<nome>/s3`. Poi partite dal nuovo punto e portate con voi skill e specifiche:

```bash
cd corso-ai-ticketing-lab
git fetch --tags
git checkout -b <nome>/s4 s4-start
git checkout <nome>/s3 -- .claude/skills docs/specs
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q                        # tutti verdi
```

Se il secondo `git checkout` dice che un percorso non esiste, vuol dire che su `<nome>/s3` non avete fatto commit di skill o specifiche: va bene, usate i riferimenti qui sotto.

Se la vostra specifica è in una cartella con un altro nome (per esempio `docs/specs/classificazione-automatica/`), usate quel percorso in tutti i comandi di oggi al posto di `docs/specs/classificazione/`.

Le decisioni di Laura sulle domande delle vostre skill (soglia, nuovi tentativi, sintesi e bozza, dati sanitari, misura) sono in fondo a `docs/richieste/classificazione-risposte-po.md`: valgono per tutti. Se il vostro PRD ne contraddice una, correggetelo prima del lab 3.1.

Novità nel repository:

| File | Cosa contiene |
| --- | --- |
| `docs/riferimento/specs/classificazione/prd.md` | Il PRD di riferimento della classificazione, la soluzione del lab 2.2 |
| `app/classificazione/provider.py` | Il confine con il modello: l'interfaccia del provider e i suoi errori |
| `LAB-S4.md` | Queste istruzioni |

Se il vostro PRD della classificazione non è completo, partite da quello di riferimento:

```bash
mkdir -p docs/specs/classificazione
cp docs/riferimento/specs/classificazione/prd.md docs/specs/classificazione/prd.md
```

Restano utili: `data/golden_dataset.json` (40 ticket etichettati), `data/risposte_registrate.json` (risposte grezze di un modello, alcune malformate di proposito), `docs/stime-costo-latenza.md` e `docs/templates/adr.md`.

**Se vi bloccate qui**

- `git fetch` non raggiunge GitHub: scaricate lo zip https://github.com/nicolaguglielmi/corso-ai-ticketing-lab/archive/refs/tags/s4-start.zip
- Ambiente mancante: la coppia lavora sul PC di chi ce l'ha.

Regola d'aula: **nessun diff si accetta senza averlo letto.**

---

## Lab 3.1: schema della risposta e prompt v1 (50 minuti, coppie)

**Obiettivo.** Decidere cosa deve restituire il modello e scrivere il primo prompt come file versionato. Prima di scrivere codice che chiama il modello, sapete già cosa accettare e cosa rifiutare.

### Passi

1. **Schema (10 min).** In `app/classificazione/schema.py` definite con Pydantic la risposta del modello:
   - `categoria`: una delle 6 di `docs/categorie.md`;
   - `priorita`: da P1 a P4;
   - `sintesi`: al massimo 300 caratteri;
   - `bozza_risposta`: testo;
   - `confidenza`: da 0 a 1;
   - `motivazione`: breve.

   Aggiungete una funzione che riceve il **testo grezzo** del modello e restituisce la proposta validata, oppure `None` se il testo non è valido.
2. **Esempi e test (15 min).** Scrivete 8 esempi: 5 validi e 3 non validi (categoria inesistente, confidenza 1,4, campo mancante). Poi un test che verifica che il validatore li distingua. Prima il test, deve fallire; poi il codice.

   **Checkpoint alle 15:10: scambio dei ruoli.**
3. **Prompt v1 (10 min).** Scrivete `prompts/classificazione_v1.md`:
   - istruzioni e formato di risposta richiesto;
   - una riga di definizione per ogni categoria e per ogni priorità;
   - il testo del ticket racchiuso tra delimitatori e **trattato come dato**, non come istruzioni.
4. **Prova su 5 ticket (15 min).** Scegliete 5 ticket da `data/golden_dataset.json`, almeno 2 con una nota "caso dubbio" o "prompt injection". Fate da modello con Claude Code:
   > Applica il prompt in prompts/classificazione_v1.md al ticket G18 di data/golden_dataset.json. Rispondi solo con il JSON richiesto dal prompt.

   Passate ogni risposta al vostro validatore e annotate in `docs/specs/classificazione/errori-v1.md` una tabella: ticket, atteso, ottenuto, ipotesi sulla causa.

### Consegna

Schema, test del validatore, `prompts/classificazione_v1.md` e tabella degli errori nel branch `<nome>/s4`.

### Fatto quando

- il validatore distingue correttamente 8 esempi su 8 e `pytest` è verde;
- il prompt è un file in `prompts/`, non una stringa nel codice;
- la tabella degli errori ha 5 righe.

### Se vi bloccate

- Non sapete da dove partire con lo schema: "Leggi docs/categorie.md e app/models.py. Proponimi uno schema Pydantic per la risposta del modello con questi campi: … Non scrivere ancora il validatore".
- Il validatore non riesce a leggere una risposta con testo prima del JSON: è normale, succede anche con i modelli veri. Decidete in coppia: si rifiuta o si prova a estrarre il JSON? Scrivetelo nel design.
- Non riuscite a usare Claude Code come modello: usate `data/risposte_registrate.json`, che contiene la risposta grezza registrata per ogni ticket.

### Per chi finisce prima

1. Passate al validatore tutte le 40 risposte di `data/risposte_registrate.json`. Quante sono valide? Quante proposte sono giuste? Quante hanno un P1 sottovalutato?
2. Scrivete la regola di fallback per la confidenza bassa: sotto quale soglia il ticket va in coda manuale senza proposta? Usate le risposte registrate per scegliere il numero.


## Lab 3.2: design e issue dei fallback (30 minuti, coppie)

**Obiettivo.** Mettere nel design dove si valida, cosa succede quando qualcosa va storto e cosa si scrive nei log. Poi le issue che implementerete nel lab 4.1.

### Passi

1. **Design (12 min).** Aggiornate `docs/specs/classificazione/design.md` con un diagramma di sequenza: ticket, mascheramento dei dati, adapter del provider, modello, validazione, coda dell'operatore. Aggiungete almeno due rami di errore. Potete farlo scrivere a Claude Code in Mermaid:
   > Aggiungi a docs/specs/classificazione/design.md un diagramma di sequenza Mermaid con il percorso normale e i rami di errore per timeout, output non valido e confidenza bassa.
2. **Log (5 min).** Nel design, una tabella di cosa si scrive nei log per ogni richiesta: latenza, token in ingresso e in uscita, esito della validazione, versione del prompt e del modello. Mai il testo del ticket.
3. **Issue (13 min).**
   > /to-issues docs/specs/classificazione/

   Controllate che ci sia una issue separata per ogni fallback: timeout, output non valido, provider non disponibile, confidenza bassa.

### Consegna

`design.md` aggiornato e `issues.md` nel branch `<nome>/s4`.

### Fatto quando

- il diagramma ha almeno due rami di errore;
- ci sono issue separate per timeout, output non valido e provider non disponibile.

### Se vi bloccate

- Il diagramma Mermaid non si legge: va bene anche un elenco numerato dei passi con i rami di errore.
- `/to-issues` produce issue troppo grandi: "Dividi ogni issue che richiede più di mezza giornata".

### Per chi finisce prima

Scrivete nel design la strategia per cambiare provider: cosa cambia nel codice e cosa resta uguale. Dove sta la validazione: dentro l'adapter o fuori? Perché?

---

## Lab 4.1: provider simulato e fallback, test prima del codice (60 minuti, coppie)

**Obiettivo.** Il primo codice del componente: un servizio che chiede la proposta al modello e, quando qualcosa va storto, manda il ticket in coda manuale invece di bloccarsi. Il modello vero non serve: lo sostituisce un provider simulato che risponde come gli dite voi. Ogni comportamento ha un test che avete visto fallire prima di scrivere il codice.

Partite dalle issue del lab 3.2 e da `app/classificazione/provider.py`, che definisce il contratto: il provider riceve il prompt e restituisce il testo grezzo, oppure solleva `TimeoutProvider` o `ProviderNonDisponibile`.

### Passi

1. **Provider simulato (15 min).** Prima il test, in `tests/test_provider_simulato.py`:
   - `provider_simulato_restituisce_output_configurato`: configurato con un testo, lo restituisce;
   - `provider_simulato_solleva_errore_configurato`: configurato con `TimeoutProvider`, lo solleva;
   - il provider ricorda l'ultimo prompt ricevuto (serve al passo 3).

   Il test deve fallire. Poi scrivete `app/classificazione/provider_simulato.py`.
2. **Servizio con i fallback (25 min).** In `app/classificazione/servizio.py` una funzione che riceve titolo, descrizione e un provider, costruisce il prompt da `prompts/classificazione_v1.md`, chiama il provider, valida la risposta con il vostro validatore del lab 3.1 e restituisce un esito: proposta, oppure manuale con il motivo. Un test alla volta, ognuno visto fallire:
   - `risposta_valida_produce_una_proposta`;
   - `timeout_del_provider_porta_a_stato_manuale`;
   - `provider_non_disponibile_porta_a_stato_manuale`;
   - `output_non_valido_porta_a_stato_manuale`;
   - `confidenza_bassa_porta_a_stato_manuale`.

   Per le risposte usate quelle vere di `data/risposte_registrate.json`: G01 è valida, G05 è troncata, G20 ha confidenza 0,35.

   **Checkpoint alle 17:15: scambio dei ruoli.**
3. **Cosa esce verso il modello (10 min).** Un test che verifica che il prompt ricevuto dal provider simulato contenga il titolo e non contenga l'email del richiedente.
4. **Prova sulle risposte registrate (10 min).** Passate al servizio i 40 ticket del golden dataset, ognuno con un provider simulato che restituisce la sua risposta registrata. Quante proposte, quante in coda manuale, quante categorie giuste? Annotate i numeri in `docs/specs/classificazione/errori-v1.md`.

### Consegna

Provider simulato, servizio e test nel branch `<nome>/s4`, `pytest` verde.

### Fatto quando

- ogni fallback del design ha il suo test, e l'avete visto fallire prima del codice;
- nessun errore del provider arriva al chiamante: il risultato è sempre una proposta o il ticket in coda manuale;
- il prompt esce dal file in `prompts/`, non da una stringa nel codice.

### Se vi bloccate

- Non sapete come configurare il provider simulato: "Scrivi in tests/ un test per una classe ProviderSimulato che si costruisce con una risposta oppure con un errore da sollevare, e che rispetta l'interfaccia in app/classificazione/provider.py. Non scrivere ancora la classe: il test deve fallire."
- Il vostro validatore del lab 3.1 non è pronto: chiedete al docente quello di riferimento e andate avanti con il servizio.
- Claude Code scrive test e codice insieme: fermatelo e chiedete "solo il test, poi lancia pytest e mostrami che fallisce".

### Per chi finisce prima

1. Aggiungete un test per un ticket che contiene un numero di telefono nella descrizione: il prompt non deve contenerlo. Poi il codice che lo maschera.
2. Aggiungete al servizio il log di ogni richiesta, con esito e latenza, senza il testo del ticket. Un test che lo verifica.

---

## Compiti per venerdì 20/11

**Esercizio individuale: ADR con costo e latenza (45 minuti, da soli).** Scrivete `docs/adr/ADR-001-<nome>.md` partendo da `docs/templates/adr.md`: chiamata sincrona o coda asincrona per la classificazione?

1. Con i numeri di `docs/stime-costo-latenza.md` calcolate il costo per ticket, il costo mensile e la latenza vista dal richiedente e dall'operatore nei due casi.
2. Confrontate i numeri con i vincoli di Laura.
3. Decidete, citando almeno uno dei numeri come motivo.

**Fatto quando** i numeri sono calcolati, con il calcolo scritto, e la decisione cita almeno un numero.

Se non avete finito il lab 4.1, completatelo prima: la prossima sessione misura il componente sul golden dataset e confronta due versioni del prompt.

Prima della chiusura:

```bash
git add -A
git commit -m "Sessione 4: design, prompt v1, provider simulato e fallback"
```
