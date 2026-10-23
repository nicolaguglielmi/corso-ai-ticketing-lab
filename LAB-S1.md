# Sessione 1: lab

Oggi lavorate per più di metà del tempo: 55 minuti di lab 1.1, 40 di lab 1.2 e 30 di esercizio individuale. I lab si fanno in coppia nelle stanze separate (breakout room) della piattaforma: una persona condivide lo schermo e scrive, l'altra rivede e prende appunti. Al checkpoint vi scambiate.

Ognuno lavora comunque sul proprio clone del repository e alla fine consegna sul proprio branch.

## Prima di iniziare (5 minuti)

```bash
git clone https://github.com/nicolaguglielmi/corso-ai-ticketing-lab.git
cd corso-ai-ticketing-lab
git checkout -b <nome>/s1 s1-start
python -m venv .venv && source .venv/bin/activate   # su Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

Se `pytest` non è verde, scrivetelo in chat subito. Piano B: la coppia lavora sul PC di chi ha l'ambiente funzionante.

Regola d'aula: **nessun diff si accetta senza averlo letto.**

---

## Lab 1.1: esplorazione del repository con Claude Code (55 minuti, coppie)

**Obiettivo.** Capire un codice che non conoscete usando Claude Code, e imparare a verificare quello che vi dice.

### Passi

1. **Orientarsi (10 min).** Avviate `claude` nella cartella del progetto e chiedete come è organizzato. Prompt di partenza:
   > Spiegami com'è organizzato questo repository: moduli, percorso di una richiesta "apri ticket" dall'endpoint al database, dove sono le regole sugli stati.
2. **Verificare (10 min).** Aprite almeno due file citati nella risposta. Nel `NOTE.md` scrivete una cosa corretta e una imprecisa o mancante. Confrontate anche il codice con `docs/processo-supporto.md`: tornano?
3. **Un test che serve davvero (15 min).** Chiedete a Claude Code di trovare un endpoint senza test e di scriverne uno. Fate girare `pytest`. Poi rompete a mano il codice di quell'endpoint (per esempio cambiate il codice di risposta) e controllate che il test fallisca. Annullate la modifica.

   **Checkpoint a metà lab: scambio dei ruoli.**
4. **Refactoring con review (15 min).** Nel file `app/main.py` la validazione di titolo e descrizione compare due volte. Chiedete di estrarla in un punto solo. **Leggete il diff prima di accettarlo** e fate girare i test.
5. **Diario (5 min).** Completate la sezione del lab 1.1 in `NOTE.md`: prompt usati, cosa ha funzionato, dove avete dovuto correggere.

### Consegna

Branch `<nome>/s1` con il nuovo test, il refactoring e `NOTE.md`.

### Fatto quando

- `pytest` è verde;
- il nuovo test fallisce quando rompete il codice a mano;
- in `NOTE.md` c'è il motivo per cui avete accettato il diff del refactoring.

### Sfida per chi finisce prima

Nel repository ci sono **almeno 5 problemi lasciati di proposito**: sicurezza, privacy, regole di business che non tornano con la documentazione, bug. Quanti ne trovate con Claude Code? Per ognuno scrivete in `NOTE.md` il file, la riga e come lo avete verificato. Attenzione: vale solo se lo avete verificato voi, non se lo ha detto il modello.

---

## Lab 1.2: CLAUDE.md e primo server MCP (40 minuti, coppie)

**Obiettivo.** Dare a Claude Code il contesto del progetto e collegarlo a una fonte esterna con permessi limitati.

### Passi

1. **CLAUDE.md (15 min).** Lanciate `/init` dentro Claude Code e riducete il file a quello che serve davvero, **massimo 40 righe**:
   - comandi per installare, testare, avviare;
   - convenzioni (lingua dei nomi, test con pytest, niente dati personali nei log);
   - cose da non fare, per esempio "non modificare `docs/` senza chiedere".
2. **Server MCP (10 min).** Collegate uno dei due server, a livello di progetto:
   - filesystem limitato alla cartella `docs/` (serve Node.js):
     ```bash
     claude mcp add --scope project docs -- npx -y @modelcontextprotocol/server-filesystem ./docs
     ```
   - oppure Git sul repository (serve `uv`):
     ```bash
     claude mcp add --scope project git -- uvx mcp-server-git --repository .
     ```
   Riaprite Claude Code e controllate con `/mcp` che il server risulti collegato.
3. **Usarlo (10 min).** Fate tre domande che passano dal server. Esempi:
   > Quali articoli della base di conoscenza parlano di VPN e che differenza c'è tra i due casi?

   > Secondo docs/categorie.md, in che categoria va una stampante che non stampa solo da un PC?

   > Mostrami gli ultimi commit e i file che hanno toccato.
4. **Fuori perimetro (5 min).** Chiedete un'operazione fuori da quello che il server consente, per esempio leggere `app/config.py` tramite il server filesystem. Annotate cosa succede e perché.

### Consegna

`CLAUDE.md` e `.mcp.json` versionati nel branch.

### Fatto quando

- `/mcp` mostra il server collegato;
- `CLAUDE.md` sta sotto le 40 righe e il comando di test che contiene funziona.

### Sfida per chi finisce prima

Aggiungete a `CLAUDE.md` due regole nate dagli errori del lab 1.1 e verificate che Claude Code le rispetti.

---

## Esercizio individuale 1: mappa dei componenti (30 minuti)

Da soli, scrivete `docs/mappa-<nome>.md`, una pagina:

1. i componenti del ticketing e il percorso di un ticket dall'apertura alla risposta;
2. **tre punti** in cui l'IA può aiutare, ognuno con il **dato** che servirebbe per misurarne l'effetto (per esempio: tempo medio di classificazione manuale, percentuale di ticket riclassificati);
3. **due rischi** da verificare, ognuno con il **dato** che servirebbe per verificarlo.

Usate pure i 20 ticket di `data/tickets_esempio.json` per ragionare su casi concreti: alcuni sono volutamente difficili.

**Fatto quando** ogni punto e ogni rischio ha una misura concreta, non un aggettivo.

Fate commit e push sul vostro branch prima della chiusura.
