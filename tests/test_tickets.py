def test_crea_ticket_restituisce_201_e_stato_aperto(client, ticket_base):
    r = client.post("/tickets", json=ticket_base)
    assert r.status_code == 201
    body = r.json()
    assert body["id"] > 0
    assert body["stato"] == "aperto"


def test_titolo_troppo_corto_restituisce_422(client, ticket_base):
    ticket_base["titolo"] = "VPN"
    r = client.post("/tickets", json=ticket_base)
    assert r.status_code == 422


def test_descrizione_vuota_restituisce_422(client, ticket_base):
    ticket_base["descrizione"] = "   "
    r = client.post("/tickets", json=ticket_base)
    assert r.status_code == 422


def test_leggi_ticket_inesistente_restituisce_404(client):
    r = client.get("/tickets/999")
    assert r.status_code == 404


def test_leggi_ticket_creato(client, ticket_base):
    creato = client.post("/tickets", json=ticket_base).json()
    r = client.get(f"/tickets/{creato['id']}")
    assert r.status_code == 200
    assert r.json()["titolo"] == ticket_base["titolo"]


def test_elenco_filtrato_per_stato(client, ticket_base):
    client.post("/tickets", json=ticket_base)
    r = client.get("/tickets", params={"stato": "aperto"})
    assert r.status_code == 200
    assert len(r.json()) == 1
    r = client.get("/tickets", params={"stato": "chiuso"})
    assert r.json() == []
