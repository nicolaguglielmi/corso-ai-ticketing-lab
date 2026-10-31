# Sessione 3: lab

Oggi riprendiamo lo Spec-Driven Development con calma: un ripasso, la demo dal PRD alle issue e i due lab della sessione 2 fatti per intero. Il design del componente (lab 3.1 e 3.2) passa alla prossima sessione.

Tempo di lab: 50 minuti di lab 2.1 e 70 di lab 2.2. Coppie nelle breakout room, una persona scrive e l'altra rivede; ai checkpoint vi scambiate.

| Orario | Attività |
| --- | --- |
| 14:00 | Domande e dove eravamo |
| 14:10 | Ripasso: dal vibe coding alla specifica |
| 14:25 | Demo: dalla richiesta alle issue, e com'è fatta una skill |
| 14:45 | Pausa caffè |
| 14:55 | Lab 2.1: le skill SDD |
| 15:45 | Plenaria: cosa avete costruito |
| 16:00 | Pausa lunga |
| 16:30 | Lab 2.2: la classificazione, dalla richiesta alle issue |
| 17:40 | Plenaria: due PRD a confronto |
| 17:55 | Chiusura e compiti |

## Prima di iniziare (5 minuti, dentro il lab 2.1)

Se avete modifiche della sessione 2 non salvate, prima fate commit sul branch `<nome>/s2`. Poi:

```bash
cd corso-ai-ticketing-lab
git fetch --tags
git checkout -b <nome>/s3 s3-start
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q                        # tutti verdi
```

Novità nel repository:

| File | Cosa contiene |
| --- | --- |
| `docs/riferimento/` | Skill SDD di riferimento, non attive, e come attivarle |
| `docs/richieste/classificazione-risposte-po.md` | Le risposte di Laura, la product owner, alle domande più probabili |
| `data/golden_dataset.json` | 40 ticket con categoria e priorità attese. Alcuni sono difficili di proposito |
| `data/risposte_registrate.json` | Le risposte grezze di un modello sui 40 ticket, alcune malformate di proposito |
| `docs/stime-costo-latenza.md` | Volumi, token, prezzi e latenze di esercitazione per l'ADR |
| `docs/templates/adr.md` | Template dell'ADR |
| `prompts/` | Cartella vuota: qui vanno i prompt versionati |

**Se vi bloccate qui**

- `git fetch` non raggiunge GitHub: scaricate lo zip https://github.com/nicolaguglielmi/corso-ai-ticketing-lab/archive/refs/tags/s3-start.zip
- Ambiente mancante: la coppia lavora sul PC di chi ce l'ha.

Regola d'aula: **nessun diff si accetta senza averlo letto.**

---

---

## Lab 2.1: le skill SDD (50 minuti, coppie)

**Obiettivo.** Avere tre skill `/prd`, `/to-design`, `/to-issues` che funzionano e che sapete spiegare. Servono per il lab 2.2 e per tutto il resto del corso.

### Strada A: avete scritto le skill a casa

1. Portate le vostre skill nel branch di oggi:
   ```bash
   git checkout <nome>/s2 -- .claude/skills
   ```
2. Riaprite Claude Code e provate `/prd` sulla richiesta vaga:
   > /prd voglio che i ticket urgenti vadano più veloci
3. Confrontate le vostre skill con quelle in `docs/riferimento/skill-sdd/`: la `description`, cosa succede quando mancano informazioni, i controlli prima di scrivere. Migliorate almeno una cosa per skill.
4. Passate alla sfida qui sotto.

### Strada B: le scrivete oggi

1. **Skill `/prd` (20 min).** Partendo da `docs/templates/skill-scheletro.md`, create `.claude/skills/prd/SKILL.md`. La skill prende una richiesta e scrive `docs/specs/<feature>/prd.md` usando `docs/templates/prd.md`. Se mancano attori, vincoli o criteri, **fa al massimo 5 domande invece di inventare**. Ogni criterio ha accanto il nome di un test. Sotto le 60 righe.

   **Checkpoint alle 15:20: scambio dei ruoli.**
2. **Skill `/to-design` (10 min).** Legge un PRD e scrive `design.md` nella stessa cartella con `docs/templates/design.md`. Se il PRD non ha almeno 3 criteri verificabili o nessun caso di errore, si ferma e dice cosa manca. Non scrive codice.
3. **Skill `/to-issues` (10 min).** Dal PRD e dal design scrive `issues.md` con issue da al massimo mezza giornata, nel formato di `docs/templates/issue.md`, ognuna con i criteri che copre e il test da scrivere prima. In fondo, la tabella di copertura criteri-issue.
4. **Prova (10 min).** Riaprite Claude Code e lanciate `/prd` sulla richiesta vaga qui sopra.

### Fatto quando

- digitando `/` compaiono `prd`, `to-design` e `to-issues`;
- sulla richiesta vaga `/prd` fa almeno due domande invece di scrivere subito il PRD;
- sapete dire in una frase quando si attiva ciascuna skill.

### Se vi bloccate

- La skill non compare digitando `/`: controllate che il file si chiami esattamente `SKILL.md` e che il frontmatter abbia `name` e `description`, poi riaprite Claude Code.
- Una skill non funziona dopo 10 minuti: copiate quella di riferimento (`cp -R docs/riferimento/skill-sdd/<nome> .claude/skills/`) e passate alla successiva. La vostra la sistemate a casa.

### Sfida per chi finisce prima

Create `.claude/skills/review-spec/SKILL.md`: rilegge un PRD e restituisce una tabella con criterio, problema e proposta. Segnala le parole come veloce, semplice, intuitivo o corretto senza una soglia numerica. Non modifica il PRD. La userete nel lab 2.2.

---

## Lab 2.2: la classificazione, dalla richiesta alle issue (70 minuti, coppie)

**Obiettivo.** La specifica completa della classificazione automatica, verificabile, con i casi di errore e le issue. È la base del design e del codice delle prossime sessioni.

### Passi

1. **PRD (25 min).**
   > /prd docs/richieste/classificazione-automatica.md

   Quando la skill fa domande, rispondete come farebbe Laura: le sue risposte sono in `docs/richieste/classificazione-risposte-po.md`. Se una domanda non ha risposta lì, chiedete al docente.

   **Checkpoint alle 16:55: scambio dei ruoli.**
2. **Revisione (15 min).** Chi non ha scritto il PRD lo rilegge con la checklist della spec efficace:
   - problema con un numero, attori, input e output con un esempio, vincoli;
   - ogni criterio con una soglia e il nome di un test;
   - i casi "il modello non risponde", "risponde con un formato sbagliato", "non è sicuro";
   - il vincolo di Laura sui P1 proposti come P3 o P4;
   - i dati che escono verso il modello.

   Se avete la skill `/review-spec`: `/review-spec docs/specs/classificazione/prd.md`. Correggete il PRD.
3. **Design (15 min).**
   > /to-design docs/specs/classificazione/prd.md

   Controllate: c'è un componente per ogni caso di errore del PRD?
4. **Issue (15 min).**
   > /to-issues docs/specs/classificazione/

   Controllate la tabella di copertura: c'è un criterio senza issue? Ogni fallback ha la sua issue?
5. **Commit.**
   ```bash
   git add -A && git commit -m "Lab 2.2: PRD, design e issue della classificazione"
   ```

### Consegna

`docs/specs/classificazione/prd.md`, `design.md` e `issues.md` nel branch `<nome>/s3`.

### Fatto quando

- il PRD ha almeno 5 criteri di accettazione e almeno 2 casi di errore;
- c'è un criterio sui P1 sottovalutati;
- ogni criterio compare nella tabella di copertura delle issue.

### Se vi bloccate

- La skill scrive il PRD senza fare domande: ditele "Prima di scrivere fammi le domande su quello che manca".
- Il PRD è lunghissimo: "Riduci docs/specs/classificazione/prd.md a una pagina, tenendo tutti i criteri e i casi di errore".
- Le skill non funzionano: stesso flusso senza skill.
  > Leggi docs/richieste/classificazione-automatica.md, docs/richieste/classificazione-risposte-po.md e docs/templates/prd.md. Scrivi docs/specs/classificazione/prd.md con almeno 5 criteri dato/quando/allora, ognuno con il nome di un test, e almeno 2 casi di errore.

### Per chi finisce prima

Aggiungete al PRD una sezione "Fuori ambito" con almeno tre richieste plausibili che questa versione non copre. Poi guardate `data/golden_dataset.json`: quali ticket metterebbero in difficoltà i vostri criteri?

---

## Compiti per venerdì 13/11

**Esercizio individuale: un PRD di una pagina, da soli (30 minuti).** Prendete la richiesta vaga "voglio che i ticket urgenti vadano più veloci" e scrivete a mano `docs/specs/urgenti/prd-<nome>.md` con il template `docs/templates/prd.md`: problema con un numero, almeno 3 criteri dato/quando/allora con il nome di un test, almeno un caso di errore. Le informazioni che mancano scrivetele come domande aperte. Claude Code solo alla fine, per controllare:

> Rileggi docs/specs/urgenti/prd-<nome>.md. Per ogni criterio dimmi solo se è verificabile e se ha il nome di un test. Non riscriverlo.

Se non avete finito i lab di oggi, completateli prima: la prossima sessione parte dal vostro PRD, dal design e dalle issue della classificazione.

Prima della chiusura:

```bash
git add -A
git commit -m "Sessione 3: skill SDD e specifica della classificazione"
```

---

## Prossima sessione: design del componente

Queste attività erano previste per oggi e si fanno venerdì 13/11, partendo dalla vostra specifica della classificazione. Potete leggerle in anticipo.

### Lab 3.1: schema della risposta e prompt v1 (50 minuti, coppie)

**Obiettivo.** Decidere cosa deve restituire il modello e scrivere il primo prompt come file versionato. Prima di scrivere codice che chiama il modello, sapete già cosa accettare e cosa rifiutare.

#### Passi

1. **Schema (10 min).** In `app/classificazione/schema.py` definite con Pydantic la risposta del modello:
   - `categoria`: una delle 6 di `docs/categorie.md`;
   - `priorita`: da P1 a P4;
   - `sintesi`: al massimo 300 caratteri;
   - `bozza_risposta`: testo;
   - `confidenza`: da 0 a 1;
   - `motivazione`: breve.

   Aggiungete una funzione che riceve il **testo grezzo** del modello e restituisce la proposta validata, oppure `None` se il testo non è valido.
2. **Esempi e test (15 min).** Scrivete 8 esempi: 5 validi e 3 non validi (categoria inesistente, confidenza 1,4, campo mancante). Poi un test che verifica che il validatore li distingua. Prima il test, deve fallire; poi il codice.

   **Checkpoint a metà: scambio dei ruoli.**
3. **Prompt v1 (10 min).** Scrivete `prompts/classificazione_v1.md`:
   - istruzioni e formato di risposta richiesto;
   - una riga di definizione per ogni categoria e per ogni priorità;
   - il testo del ticket racchiuso tra delimitatori e **trattato come dato**, non come istruzioni.
4. **Prova su 5 ticket (15 min).** Scegliete 5 ticket da `data/golden_dataset.json`, almeno 2 con una nota "caso dubbio" o "prompt injection". Fate da modello con Claude Code:
   > Applica il prompt in prompts/classificazione_v1.md al ticket G18 di data/golden_dataset.json. Rispondi solo con il JSON richiesto dal prompt.

   Passate ogni risposta al vostro validatore e annotate in `docs/specs/classificazione/errori-v1.md` una tabella: ticket, atteso, ottenuto, ipotesi sulla causa.

#### Consegna

Schema, test del validatore, `prompts/classificazione_v1.md` e tabella degli errori nel branch `<nome>/s3`.

#### Fatto quando

- il validatore distingue correttamente 8 esempi su 8 e `pytest` è verde;
- il prompt è un file in `prompts/`, non una stringa nel codice;
- la tabella degli errori ha 5 righe.

#### Se vi bloccate

- Non sapete da dove partire con lo schema: "Leggi docs/categorie.md e app/models.py. Proponimi uno schema Pydantic per la risposta del modello con questi campi: … Non scrivere ancora il validatore".
- Il validatore non riesce a leggere una risposta con testo prima del JSON: è normale, succede anche con i modelli veri. Decidete in coppia: si rifiuta o si prova a estrarre il JSON? Scrivetelo nel design.
- Non riuscite a usare Claude Code come modello: usate `data/risposte_registrate.json`, che contiene la risposta grezza registrata per ogni ticket.

#### Per chi finisce prima

1. Passate al validatore tutte le 40 risposte di `data/risposte_registrate.json`. Quante sono valide? Quante proposte sono giuste? Quante hanno un P1 sottovalutato?
2. Scrivete la regola di fallback per la confidenza bassa: sotto quale soglia il ticket va in coda manuale senza proposta? Usate le risposte registrate per scegliere il numero.


### Lab 3.2: design e issue dei fallback (25 minuti, coppie)

**Obiettivo.** Mettere nel design dove si valida, cosa succede quando qualcosa va storto e cosa si scrive nei log. Poi le issue per la sessione 4.

#### Passi

1. **Design (10 min).** Aggiornate `docs/specs/classificazione/design.md` con un diagramma di sequenza: ticket, mascheramento dei dati, adapter del provider, modello, validazione, coda dell'operatore. Aggiungete almeno due rami di errore. Potete farlo scrivere a Claude Code in Mermaid:
   > Aggiungi a docs/specs/classificazione/design.md un diagramma di sequenza Mermaid con il percorso normale e i rami di errore per timeout, output non valido e confidenza bassa.
2. **Log (5 min).** Nel design, una tabella di cosa si scrive nei log per ogni richiesta: latenza, token in ingresso e in uscita, esito della validazione, versione del prompt e del modello. Mai il testo del ticket.
3. **Issue (10 min).**
   > /to-issues docs/specs/classificazione/

   Controllate che ci sia una issue separata per ogni fallback: timeout, output non valido, provider non disponibile, confidenza bassa.

#### Consegna

`design.md` aggiornato e `issues.md` nel branch `<nome>/s3`.

#### Fatto quando

- il diagramma ha almeno due rami di errore;
- ci sono issue separate per timeout, output non valido e provider non disponibile.

#### Se vi bloccate

- Il diagramma Mermaid non si legge: va bene anche un elenco numerato dei passi con i rami di errore.
- `/to-issues` produce issue troppo grandi: "Dividi ogni issue che richiede più di mezza giornata".

#### Per chi finisce prima

Scrivete nel design la strategia per cambiare provider: cosa cambia nel codice e cosa resta uguale. Dove sta la validazione: dentro l'adapter o fuori? Perché?

### ADR: chiamata sincrona o coda

Scrivete `docs/adr/ADR-001-<nome>.md` partendo da `docs/templates/adr.md`: chiamata sincrona o coda asincrona per la classificazione?

1. Con i numeri di `docs/stime-costo-latenza.md` calcolate il costo per ticket, il costo mensile e la latenza vista dal richiedente e dall'operatore nei due casi.
2. Confrontate i numeri con i vincoli di Laura.
3. Decidete, citando almeno uno dei numeri come motivo.

**Fatto quando** i numeri sono calcolati, con il calcolo scritto, e la decisione cita almeno un numero.
