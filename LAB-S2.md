# Sessione 2: lab

Oggi costruite il vostro flusso spec-driven: tre skill di Claude Code che trasformano una richiesta in PRD, design e issue. Poi lo usate sulla prima feature IA del ticketing, la classificazione automatica.

Tempo di lab: 50 minuti di lab 2.1, 50 di lab 2.2 e 30 di esercizio individuale. Coppie nelle breakout room, una persona scrive e l'altra rivede; ai checkpoint vi scambiate.

## Prima di iniziare (5 minuti)

Se avete ancora modifiche della sessione 1 non salvate, prima fate commit sul branch `<nome>/s1`. Poi:

```bash
cd corso-ai-ticketing-lab
git fetch --tags
git checkout -b <nome>/s2 s2-start
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q                        # 20 test verdi
```

Il punto di partenza contiene una soluzione dei lab della sessione 1: la trovate descritta in `SOLUZIONI-S1.md`.

**Se vi bloccate qui**

- `git fetch` non raggiunge GitHub: scaricate lo zip https://github.com/nicolaguglielmi/corso-ai-ticketing-lab/archive/refs/tags/s2-start.zip
- Non avete il clone della sessione 1: seguite il README da capo, poi `git checkout -b <nome>/s2 s2-start`.
- Ambiente mancante: la coppia lavora sul PC di chi ce l'ha.

Materiali che userete: `docs/templates/` (PRD, design, issue, scheletro di skill) e `docs/richieste/` (le richieste del product owner).

---

## Lab 2.1: le tre skill SDD (50 minuti, coppie)

**Obiettivo.** Rendere ripetibile il flusso richiesta → PRD → design → issue con tre skill, ognuna con una sola responsabilità.

### Passi

1. **Skill `/prd` (15 min).** Partendo da `docs/templates/skill-scheletro.md`, create `.claude/skills/prd/SKILL.md`. La skill prende una richiesta in linguaggio naturale e scrive `docs/specs/<feature>/prd.md` usando `docs/templates/prd.md`. Se mancano attori, vincoli o criteri di accettazione, **deve fare domande invece di inventarli**.

   **Checkpoint alle 15:25: scambio dei ruoli.**
2. **Skill `/to-design` (12 min).** Legge il PRD e scrive `design.md` nella stessa cartella, usando `docs/templates/design.md`. Se il PRD non ha criteri di accettazione verificabili, si ferma e lo dice.
3. **Skill `/to-issues` (12 min).** Dal design scrive `issues.md`: issue piccole, al massimo mezza giornata ciascuna, ognuna con i criteri del PRD che soddisfa (AC-1, AC-2...) e il test da scrivere prima. Formato in `docs/templates/issue.md`.
4. **Prova sulla richiesta vaga (6 min).** Riaprite Claude Code e lanciate:
   > /prd voglio che i ticket urgenti vadano più veloci

   La skill deve fare domande, non scrivere un PRD inventato.

### Consegna

Le tre skill in `.claude/skills/`, con commit sul branch `<nome>/s2`.

### Fatto quando

- digitando `/` in Claude Code compaiono `prd`, `to-design` e `to-issues`;
- sulla richiesta vaga `/prd` fa almeno due domande;
- ogni `SKILL.md` sta sotto le 60 righe.

### Se vi bloccate

- La skill non compare: controllate il percorso esatto (`.claude/skills/<nome>/SKILL.md`), il frontmatter con `name` e `description`, poi chiudete e riaprite Claude Code.
- La skill c'è ma non viene usata come vi aspettate: richiamatela in modo esplicito ("usa la skill prd per questa richiesta") e rendete più precisa la `description`.
- Il tempo stringe: completate bene `/prd` e fate `/to-design` e `/to-issues` in versione minima. Le migliorate nel lab 2.2.

### Sfida per chi finisce prima

1. Aggiungete a `/prd` una checklist che segnala i criteri non verificabili, per esempio "veloce", "intuitivo", "corretto" senza soglia.
2. Create una quarta skill `/review-spec` che rilegge un PRD e restituisce i problemi in una tabella: criterio, problema, proposta.

---

## Lab 2.2: classificazione automatica fino ai task (50 minuti, coppie)

**Obiettivo.** Usare il vostro flusso su una richiesta vera, incompleta come quelle reali.

### Passi

1. **PRD (15 min).** Lanciate `/prd` sulla richiesta in `docs/richieste/classificazione-automatica.md`. Rispondete alle domande come farebbe la product owner; per i dubbi che restano, chiedete al docente, che fa da product owner.
2. **Revisione (10 min).** Rileggete il PRD in coppia:
   - ogni criterio è misurabile e ha il nome di un test?
   - ci sono i casi di errore?
   - cosa succede se il modello non risponde, risponde male o non è sicuro?
   - quali dati del ticket possono uscire verso un servizio esterno?

   **Checkpoint alle 16:55: scambio dei ruoli.**
3. **Design e issue (15 min).** Lanciate `/to-design` e `/to-issues` sul PRD.
4. **Scambio con un'altra coppia (10 min).** Il docente vi abbina a un'altra stanza: ognuna legge `issues.md` dell'altra e segnala almeno un'issue di cui non si capisce come scrivere il test. Scrivete le segnalazioni in `NOTE.md`.

### Consegna

`docs/specs/classificazione/` con `prd.md`, `design.md` e `issues.md`, con commit sul branch.

### Fatto quando

- il PRD ha almeno 5 criteri di accettazione e almeno 1 caso di errore;
- ogni issue è collegata ad almeno un criterio;
- c'è almeno un'issue dedicata a cosa succede quando il modello non risponde.

### Se vi bloccate

- Le vostre skill non funzionano ancora bene: usate i prompt equivalenti nel documento dei prompt della lezione, con gli stessi template. Il flusso conta più dello strumento.
- Il PRD esce lunghissimo: chiedete di ridurlo a una pagina tenendo criteri e casi di errore.
- La coppia con cui fare lo scambio non ha ancora le issue: scambiatevi il PRD invece delle issue.

### Sfida per chi finisce prima

1. Aggiungete al PRD una sezione "fuori ambito" con almeno tre richieste plausibili che questa versione non copre.
2. Fate girare `/review-spec`, se l'avete creata, sul PRD dell'altra coppia.

---

## Esercizio individuale 2: PRD di una pagina (30 minuti)

Da soli, scrivete `docs/specs/classificazione/prd-<nome>.md`: un PRD di una pagina, partendo da quello di coppia ma rivisto senza aiuto.

- almeno 5 criteri di accettazione verificabili e almeno 1 caso di errore;
- accanto a ogni criterio, il nome del test che lo verificherà, per esempio `ticket_senza_testo_restituisce_errore`;
- nessun criterio con parole come "veloce", "semplice" o "corretto" senza una soglia.

**Se finite prima.** Scegliete un criterio e scrivete davvero il test in `tests/`, anche se fallisce: è il primo passo della sessione 4.

Prima della chiusura:

```bash
git add -A
git commit -m "Sessione 2: skill SDD e specifica della classificazione"
```
