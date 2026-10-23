import pytest
from fastapi.testclient import TestClient

from app import config


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "DB_PATH", str(tmp_path / "test.db"))
    from app.main import app

    with TestClient(app) as c:
        yield c


@pytest.fixture()
def ticket_base():
    return {
        "titolo": "VPN non si connette da casa",
        "descrizione": "Da stamattina il client VPN restituisce errore di autenticazione.",
        "email_richiedente": "mario.rossi@example.com",
    }
