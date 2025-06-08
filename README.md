# Projecte Seqüera

Aquest projecte resol la PAC 4 de Programació per a la ciència de dades.
Conté diverses funcions per analitzar l'evolució del volum d'aigua al pantà de
La Baells.

## Instal·lació

```bash
pip install -r requirements.txt
```

## Execució

```bash
python -m src.main
```

Per executar un exercici concret:

```bash
python -m src.main -ex 3
```

## Tests

```bash
pytest --cov
```

## Documentació

```bash
pdoc --html src -o doc
```

## Linter

```bash
pylint src
```
