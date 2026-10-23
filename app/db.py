"""Persistenza essenziale su SQLite."""

import sqlite3
from contextlib import contextmanager

from app import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    descrizione TEXT NOT NULL,
    email_richiedente TEXT NOT NULL,
    categoria TEXT,
    priorita TEXT,
    stato TEXT NOT NULL DEFAULT 'aperto',
    creato_il TEXT NOT NULL,
    aggiornato_il TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS commenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER NOT NULL REFERENCES tickets(id),
    autore TEXT NOT NULL,
    testo TEXT NOT NULL,
    creato_il TEXT NOT NULL
);
"""


def init_db() -> None:
    with get_conn() as conn:
        conn.executescript(SCHEMA)


@contextmanager
def get_conn():
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()
