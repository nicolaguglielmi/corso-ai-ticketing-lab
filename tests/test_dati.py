"""Controlli sui dati di esercitazione della sessione 3."""

import json
from pathlib import Path

from app.models import Categoria, Priorita

DATI = Path(__file__).resolve().parent.parent / "data"


def carica(nome):
    return json.loads((DATI / nome).read_text(encoding="utf-8"))


def test_golden_dataset_ha_40_ticket_con_id_unici():
    golden = carica("golden_dataset.json")
    assert len(golden) == 40
    assert len({t["id"] for t in golden}) == 40


def test_golden_dataset_usa_solo_categorie_e_priorita_ammesse():
    categorie = {c.value for c in Categoria}
    priorita = {p.value for p in Priorita}
    for t in carica("golden_dataset.json"):
        assert t["categoria_attesa"] in categorie, t["id"]
        assert t["priorita_attesa"] in priorita, t["id"]


def test_ogni_ticket_del_golden_ha_una_risposta_registrata():
    golden = {t["id"] for t in carica("golden_dataset.json")}
    risposte = carica("risposte_registrate.json")["risposte"]
    assert set(risposte) == golden
    assert all(isinstance(r, str) for r in risposte.values())
