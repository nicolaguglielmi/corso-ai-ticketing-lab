"""Carica i ticket di esempio nel database locale.

Uso: python scripts/carica_esempi.py
I ticket vengono creati senza categoria e priorita': quelle attese restano nel file
come etichette per gli esercizi di classificazione delle prossime sessioni.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402

FILE = Path(__file__).resolve().parent.parent / "data" / "tickets_esempio.json"


def main() -> None:
    esempi = json.loads(FILE.read_text(encoding="utf-8"))
    with TestClient(app) as client:
        for e in esempi:
            r = client.post(
                "/tickets",
                json={
                    "titolo": e["titolo"],
                    "descrizione": e["descrizione"],
                    "email_richiedente": e["email_richiedente"],
                },
            )
            esito = "ok" if r.status_code == 201 else f"errore {r.status_code}: {r.text}"
            print(f"{e['id_esempio']} {e['titolo'][:50]:<50} {esito}")


if __name__ == "__main__":
    main()
