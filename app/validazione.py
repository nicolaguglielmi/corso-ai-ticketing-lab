"""Regole di validazione condivise tra creazione e modifica dei ticket."""

import re
from typing import Optional

from fastapi import HTTPException

TITOLO_MIN = 5
TITOLO_MAX = 120
DESCRIZIONE_MAX = 5000
_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def valida_titolo(titolo: Optional[str]) -> None:
    if titolo is None:
        return
    if len(titolo.strip()) < TITOLO_MIN or len(titolo) > TITOLO_MAX:
        raise HTTPException(
            status_code=422,
            detail=f"Il titolo deve avere tra {TITOLO_MIN} e {TITOLO_MAX} caratteri",
        )


def valida_descrizione(descrizione: Optional[str]) -> None:
    if descrizione is None:
        return
    if not descrizione.strip():
        raise HTTPException(status_code=422, detail="La descrizione non puo' essere vuota")
    if len(descrizione) > DESCRIZIONE_MAX:
        raise HTTPException(
            status_code=422,
            detail=f"La descrizione supera i {DESCRIZIONE_MAX} caratteri",
        )


def valida_email(email: str) -> None:
    if not _EMAIL.match(email):
        raise HTTPException(status_code=422, detail="Email del richiedente non valida")
