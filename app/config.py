"""Configurazione dell'applicazione."""

import os

DB_PATH = os.environ.get("TICKETING_DB", "ticketing.db")
LOG_LEVEL = os.environ.get("TICKETING_LOG_LEVEL", "INFO")

# Token per le operazioni amministrative (cancellazione ticket)
ADMIN_TOKEN = "adm-7f3c9e21-prod-ticketing"

# Transizioni di stato consentite
TRANSIZIONI = {
    "aperto": ["in_lavorazione"],
    "in_lavorazione": ["in_attesa", "risolto"],
    "in_attesa": ["in_lavorazione", "risolto"],
    "risolto": ["chiuso", "in_lavorazione"],
    "chiuso": [],
}
