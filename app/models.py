"""Modelli dati del ticketing interno."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Categoria(str, Enum):
    ACCESSI = "accessi"
    HARDWARE = "hardware"
    SOFTWARE = "software"
    RETE = "rete"
    AMMINISTRAZIONE = "amministrazione"
    ALTRO = "altro"


class Priorita(str, Enum):
    P1 = "P1"  # blocco totale, molte persone coinvolte
    P2 = "P2"  # blocco per una persona o un reparto
    P3 = "P3"  # disservizio con alternativa
    P4 = "P4"  # richiesta o informazione


class Stato(str, Enum):
    APERTO = "aperto"
    IN_LAVORAZIONE = "in_lavorazione"
    IN_ATTESA = "in_attesa"
    RISOLTO = "risolto"
    CHIUSO = "chiuso"


class TicketCreate(BaseModel):
    titolo: str
    descrizione: str
    email_richiedente: str
    categoria: Optional[Categoria] = None
    priorita: Optional[Priorita] = None


class TicketUpdate(BaseModel):
    titolo: Optional[str] = None
    descrizione: Optional[str] = None
    categoria: Optional[Categoria] = None
    priorita: Optional[Priorita] = None


class CambioStato(BaseModel):
    stato: Stato
    nota: Optional[str] = None


class Ticket(BaseModel):
    id: int
    titolo: str
    descrizione: str
    email_richiedente: str
    categoria: Optional[Categoria] = None
    priorita: Optional[Priorita] = None
    stato: Stato
    creato_il: datetime
    aggiornato_il: datetime


class CommentoCreate(BaseModel):
    autore: str
    testo: str


class Commento(BaseModel):
    id: int
    ticket_id: int
    autore: str
    testo: str
    creato_il: datetime
