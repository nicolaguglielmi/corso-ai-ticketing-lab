# Ticketing interno

API REST in Python (FastAPI + SQLite) per il ticketing del supporto interno. Repository del corso "Design e integrazione di soluzioni IA-enabled".

## Comandi

- Installazione: `python -m venv .venv`, attivare l'ambiente, `pip install -r requirements.txt`
- Test: `pytest -q` (deve restare verde dopo ogni modifica)
- Avvio: `uvicorn app.main:app --reload` (documentazione su /docs)
- Dati di esempio: `python scripts/carica_esempi.py`

## Struttura

- `app/main.py` endpoint, `app/models.py` modelli, `app/validazione.py` regole sugli input, `app/config.py` configurazione e transizioni di stato
- `docs/` processo di supporto, categorie, base di conoscenza: sono la fonte delle regole di business
- `docs/specs/<feature>/` specifiche prodotte con il flusso SDD

## Convenzioni

- Nomi di funzioni, variabili e test in italiano
- Ogni modifica al comportamento ha un test; prima il test, poi il codice
- Nessun dato personale (email, telefono) nei log
- Le regole di business stanno in `docs/`: se il codice le contraddice, segnalalo prima di cambiare qualcosa

## Cose da non fare

- Non modificare `docs/` senza chiedere
- Non accettare modifiche senza aver fatto girare `pytest`
- Non introdurre nuove dipendenze senza dirlo
