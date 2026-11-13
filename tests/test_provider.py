"""Il contratto del provider: gli errori del servizio esterno hanno una radice comune."""

from app.classificazione.provider import ErroreProvider, ProviderNonDisponibile, TimeoutProvider


def test_errori_del_provider_hanno_una_radice_comune():
    assert issubclass(TimeoutProvider, ErroreProvider)
    assert issubclass(ProviderNonDisponibile, ErroreProvider)
