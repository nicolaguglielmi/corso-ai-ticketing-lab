# Ticketing interno: repository del corso

Repository del corso "Design e integrazione di soluzioni IA-enabled". Contiene un sistema di ticketing interno, per ora **senza IA**: API REST in Python con FastAPI e SQLite. Nelle prossime sessioni ci aggiungeremo il componente che propone categoria, priorità e bozza di risposta.

## Requisiti

- Python 3.11 o superiore
- Git
- Claude Code installato e autenticato

## Scaricare il repository

La prima volta:

```bash
git clone https://github.com/nicolaguglielmi/corso-ai-ticketing-lab.git
cd corso-ai-ticketing-lab
git checkout -b <nome>/s1 s1-start
```

Ogni lezione ha un punto di partenza (`s1-start`, `s2-start` e così via) che si aggiunge al repository prima dell'incontro. Il tag di una lezione contiene anche le soluzioni dei lab precedenti, così chi resta indietro riparte allineato:

```bash
git fetch --tags
git checkout -b <nome>/s2 s2-start
```

Calendario, avvisi e materiali sono nell'agenda del corso:
https://docs.google.com/document/d/1LLEUcFKwNrcOZavjMW7vbQtu0467KHFGSmE2YHINh3w/edit?usp=sharing

## Avvio

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
pytest                                   # la suite deve essere verde
python scripts/carica_esempi.py          # carica 20 ticket di esempio
uvicorn app.main:app --reload            # API su http://127.0.0.1:8000/docs
```

## Struttura

```
app/        codice dell'API
tests/      test automatici (pytest)
docs/       processo di supporto, categorie, architettura, base di conoscenza (kb/)
data/       ticket di esempio con categoria e priorità attese
scripts/    utilità
LAB-S1.md   istruzioni dei lab della sessione 1
NOTE.md     il tuo diario di lab
```

## Lab di oggi

Le istruzioni sono in [LAB-S1.md](LAB-S1.md).
