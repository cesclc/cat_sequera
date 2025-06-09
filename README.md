# Projecte Embassament La Baells

Aquest repositori conté el codi utilitzat a la PAC 4 de *Programació per a la ciència de dades*. L'objectiu és analitzar l'evolució del volum d'aigua a l'embassament de **La Baells** a partir de les dades històriques disponibles.

## Requisits

* Python 3.10 o superior
* Les dependències indicades al fitxer `requirements.txt`

## Instal·lació

```bash
pip install -r requirements.txt
```

## Ús bàsic

Per executar tots els exercicis de manera consecutiva:

```bash
python -m src.main
```
Cal utilitzar l'opció `-m` per executar-lo com a mòdul i assegurar que els
imports relatius funcionen correctament.

També es pot indicar un exercici concret amb l'opció `-ex`:

```bash
python -m src.main -ex 3
```

Les gràfiques generades es desen a la carpeta `img/`.

## Proves

Per executar la bateria de tests i veure la cobertura:

```bash
pytest --cov
```

## Generar documentació

La documentació dels mòduls es pot generar amb **pdoc**:

```bash
pdoc --html src -o doc
```

## Qualitat del codi

Aquest projecte utilitza **pylint** per comprovar l'estil de codi:

```bash
pylint src
```
