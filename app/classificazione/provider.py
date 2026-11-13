"""Confine con il servizio che classifica i ticket.

Il contratto viene dal design della classificazione: il provider riceve il testo del
prompt già pronto e restituisce il testo grezzo del modello, senza validarlo.
La validazione sta fuori dal provider, così cambiare provider non cambia i controlli.
"""

from typing import Protocol


class ErroreProvider(Exception):
    """Errore del servizio esterno. Il chiamante non deve mai propagarlo all'utente."""


class TimeoutProvider(ErroreProvider):
    """Il servizio non ha risposto entro il tempo massimo."""


class ProviderNonDisponibile(ErroreProvider):
    """Il servizio è giù, rifiuta la richiesta o ha esaurito la quota."""


class ClassificatoreProvider(Protocol):
    def classifica(self, testo_prompt: str) -> str:
        """Invia il prompt al modello e restituisce la sua risposta grezza.

        Solleva TimeoutProvider o ProviderNonDisponibile se il servizio non risponde.
        """
        ...
