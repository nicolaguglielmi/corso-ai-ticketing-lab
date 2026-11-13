# Risposte del product owner sulla classificazione automatica

Da: Laura, responsabile del supporto interno
Oggetto: Re: domande sulla classificazione

Ciao,
rispondo alle domande che mi avete mandato. Se vi serve altro chiedete al docente, che fa le mie veci in aula.

**Quanti ticket arrivano?** Circa 180 per giorno lavorativo. Il picco è tra le 8:30 e le 9:30, con una quarantina di ticket in un'ora.

**Quanto costa oggi lo smistamento?** In media 2 minuti a ticket. A settembre il 45% dei ticket ha cambiato categoria o priorità dopo il primo smistamento.

**Quando funziona?** Mi basta che la categoria sia giusta in almeno 8 casi su 10. Una cosa però non la accetto: un ticket P1 proposto come P3 o P4. Un'urgenza sottovalutata è il problema peggiore, molto più di una categoria sbagliata.

**E se il sistema non è sicuro?** Meglio nessuna proposta che una sbagliata. Il ticket resta nella coda manuale come oggi e l'operatore lo smista a mano.

**Quali dati possono uscire verso un servizio esterno?** Titolo e descrizione. L'email del richiedente e i numeri di telefono mai. Nei ticket per le postazioni adattate a volte ci sono dati sanitari: vanno mascherati prima di uscire.

**Il richiedente deve aspettare?** No. Quando apre il ticket deve vedere la conferma come oggi, in meno di un secondo. La proposta per l'operatore può arrivare dopo, entro un minuto.

**E la bozza di risposta?** La vede e la approva sempre l'operatore. Non parte niente in automatico.

**Lingue?** Ogni tanto arrivano ticket in inglese dai colleghi stranieri: vanno gestiti.

**Budget?** Massimo 50 euro al mese per il servizio di classificazione.

**Scadenza?** Fine mese era un desiderio. Mi va bene una prima versione che funziona con un servizio simulato, poi colleghiamo quello vero.

Laura

---

## Seconda risposta, dopo le domande delle skill (06/11)

Ciao,
le vostre skill mi hanno fatto domande precise. Le decisioni valgono per tutti:

1. **Soglia di confidenza**: 0,7 come punto di partenza. Va verificata sul golden dataset e la rivediamo con i numeri.
2. **Servizio non disponibile, timeout, JSON non valido o categoria fuori elenco**: nessun nuovo tentativo in questa versione. Il ticket va subito nella coda manuale, come per la confidenza bassa, e l'esito si scrive nel log, senza il testo del ticket.
3. **Sintesi e bozza di risposta** fanno parte di questa versione. La bozza la vede e la approva sempre l'operatore: niente invio automatico, e niente link nella bozza.
4. **Dati sanitari**: non c'è una regola già definita. Per questa versione basta una lista di termini (invalidità, certificato medico, patologia, legge 104, malattia) più tutti i ticket sulle postazioni adattate. Email e numeri di telefono si mascherano sempre.
5. **Come si misura**: categoria giusta in almeno 32 ticket su 40, e nessun P1 proposto come P3 o P4. I ticket finiti in coda manuale contano come non classificati correttamente. Per l'inglese niente soglia separata: c'è un solo ticket nel golden dataset, basta che sia classificato correttamente.

Laura
