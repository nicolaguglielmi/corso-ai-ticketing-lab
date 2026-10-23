# Architettura (versione base)

Il ticketing è una API REST in Python con FastAPI e persistenza su SQLite.

```
client (portale interno, email gateway)
        |
        v
  FastAPI app/main.py  ---> SQLite (tickets, commenti)
        |
        v
      log applicativi
```

## Moduli

- `app/main.py`: endpoint REST e validazione degli input.
- `app/models.py`: modelli Pydantic, categorie, priorità e stati.
- `app/db.py`: connessione e schema SQLite.
- `app/config.py`: configurazione e regole di transizione degli stati.

## Endpoint

| Metodo | Percorso | Descrizione |
| --- | --- | --- |
| POST | /tickets | Apre un ticket |
| GET | /tickets/{id} | Legge un ticket |
| GET | /tickets?stato=&q= | Elenca e cerca i ticket |
| PATCH | /tickets/{id} | Modifica titolo, descrizione, categoria, priorità |
| POST | /tickets/{id}/stato | Cambia lo stato secondo le regole del processo |
| POST | /tickets/{id}/commenti | Aggiunge un commento |
| GET | /tickets/{id}/commenti | Elenca i commenti |
| GET | /stats | Conteggi per stato e categoria |
| DELETE | /tickets/{id} | Cancella un ticket (solo amministratori) |

## Evoluzione prevista nel corso

Nelle prossime sessioni si aggiunge un componente IA che propone categoria, priorità, sintesi e bozza di risposta. L'operatore approva sempre prima dell'invio.
