"""Test aggiunti come soluzione del lab 1.1: endpoint senza copertura e problemi trovati nella sfida."""

from app import config


def _crea(client, ticket_base, **extra):
    r = client.post("/tickets", json={**ticket_base, **extra})
    assert r.status_code == 201
    return r.json()


# --- modifica -------------------------------------------------------------


def test_modifica_titolo(client, ticket_base):
    t = _crea(client, ticket_base)
    r = client.patch(f"/tickets/{t['id']}", json={"titolo": "VPN bloccata da casa"})
    assert r.status_code == 200
    assert r.json()["titolo"] == "VPN bloccata da casa"


def test_modifica_con_titolo_corto_restituisce_422(client, ticket_base):
    t = _crea(client, ticket_base)
    r = client.patch(f"/tickets/{t['id']}", json={"titolo": "VPN"})
    assert r.status_code == 422


def test_modifica_ticket_inesistente_restituisce_404(client):
    r = client.patch("/tickets/999", json={"titolo": "Titolo valido"})
    assert r.status_code == 404


# --- stati ----------------------------------------------------------------


def test_presa_in_carico(client, ticket_base):
    t = _crea(client, ticket_base)
    r = client.post(f"/tickets/{t['id']}/stato", json={"stato": "in_lavorazione"})
    assert r.status_code == 200
    assert r.json()["stato"] == "in_lavorazione"


def test_aperto_non_si_chiude_senza_presa_in_carico(client, ticket_base):
    t = _crea(client, ticket_base)
    r = client.post(f"/tickets/{t['id']}/stato", json={"stato": "chiuso"})
    assert r.status_code == 409


def test_chiuso_e_definitivo(client, ticket_base):
    t = _crea(client, ticket_base)
    for stato in ["in_lavorazione", "risolto", "chiuso"]:
        assert client.post(f"/tickets/{t['id']}/stato", json={"stato": stato}).status_code == 200
    r = client.post(f"/tickets/{t['id']}/stato", json={"stato": "aperto"})
    assert r.status_code == 409


# --- commenti -------------------------------------------------------------


def test_aggiungi_e_leggi_commenti(client, ticket_base):
    t = _crea(client, ticket_base)
    r = client.post(f"/tickets/{t['id']}/commenti", json={"autore": "operatore1", "testo": "Preso in carico"})
    assert r.status_code == 201
    r = client.get(f"/tickets/{t['id']}/commenti")
    assert [c["testo"] for c in r.json()] == ["Preso in carico"]


def test_commento_su_ticket_inesistente_restituisce_404(client):
    r = client.post("/tickets/999/commenti", json={"autore": "operatore1", "testo": "?"})
    assert r.status_code == 404


# --- ricerca e statistiche --------------------------------------------------


def test_ricerca_per_testo(client, ticket_base):
    _crea(client, ticket_base)
    _crea(client, ticket_base, titolo="Stampante inceppata al piano 2")
    r = client.get("/tickets", params={"q": "Stampante"})
    assert len(r.json()) == 1


def test_ricerca_non_permette_sql_injection(client, ticket_base):
    _crea(client, ticket_base)
    r = client.get("/tickets", params={"q": "zzz%' OR 1=1) --"})
    assert r.status_code == 200
    assert r.json() == []


def test_statistiche(client, ticket_base):
    _crea(client, ticket_base)
    _crea(client, ticket_base, categoria="rete")
    r = client.get("/stats")
    assert r.json()["per_stato"] == {"aperto": 2}
    assert r.json()["per_categoria"]["rete"] == 1


# --- email e cancellazione --------------------------------------------------


def test_email_senza_dominio_restituisce_422(client, ticket_base):
    ticket_base["email_richiedente"] = "@"
    assert client.post("/tickets", json=ticket_base).status_code == 422


def test_cancellazione_senza_token_restituisce_403(client, ticket_base):
    t = _crea(client, ticket_base)
    assert client.delete(f"/tickets/{t['id']}").status_code == 403


def test_cancellazione_con_token(client, ticket_base):
    t = _crea(client, ticket_base)
    r = client.delete(f"/tickets/{t['id']}", headers={"X-Admin-Token": config.ADMIN_TOKEN})
    assert r.status_code == 204
    assert client.get(f"/tickets/{t['id']}").status_code == 404
