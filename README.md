# Ticketing interno: repository del corso

Repository del corso "Design e integrazione di soluzioni IA-enabled". Contiene un sistema di ticketing interno, per ora **senza IA**: API REST in Python con FastAPI e SQLite. Nelle prossime sessioni ci aggiungeremo il componente che propone categoria, priorità e bozza di risposta.

## Requisiti

- Python 3.11 o superiore
- Git
- Claude Code installato e autenticato

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
