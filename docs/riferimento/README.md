# Materiali di riferimento

## skill-sdd/

Una versione di riferimento delle skill del lab 2.1: `prd`, `to-design`, `to-issues` e `review-spec` (la sfida). Non sono attive: Claude Code carica solo le skill in `.claude/skills/`.

Se nella sessione 2 non avete finito le vostre skill, attivate queste:

```bash
mkdir -p .claude/skills
cp -R docs/riferimento/skill-sdd/* .claude/skills/
```

Riaprite Claude Code e digitate `/`: devono comparire `prd`, `to-design`, `to-issues` e `review-spec`.

Se avete scritto le vostre, confrontatele con queste: guardate soprattutto la `description`, che decide quando la skill si attiva, e cosa fa la skill quando mancano informazioni.

## Esempio di PRD

`docs/specs/chiusura-automatica/prd.md` è un PRD prodotto con la skill `/prd` di riferimento sulla richiesta della chiusura automatica: un esempio di forma per criteri, test e casi di errore.
