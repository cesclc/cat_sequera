"""Programa principal per executar els exercicis de la PAC."""
from __future__ import annotations

import argparse
from pathlib import Path

# Importa els mòduls utilitzant imports relatius per garantir
# que funcionin tant en execucions locals com quan es fa
# ``python -m src.main``
from .modules import exercise1, exercise2, exercise3, exercise4, exercise5


DATA_PATH = Path(__file__).resolve().parent.parent / 'data' / 'embassaments.csv'
IMG_DIR = Path(__file__).resolve().parent.parent / 'img'


DEF_IMG = IMG_DIR / 'labaells_Francesc_Lucas_Carbo.png'
DEF_IMG_SMOOTH = IMG_DIR / 'labaells_smoothed_Francesc_Lucas_Carbo.png'


def exec_ex1() -> None:
    """Executa les tasques de l'exercici 1 i retorna el ``DataFrame``.

    Carrega el dataset i mostra per pantalla informació bàsica.
    """
    df = exercise1.carrega_dataset(DATA_PATH)
    print(exercise1.mostra_head(df))
    print(exercise1.columnes(df))
    print(exercise1.info_dataframe(df))


    return df


def exec_ex2(df):
    """Executa l'exercici 2 sobre el ``DataFrame`` rebut.

    Reanomena columnes, neteja els noms de les estacions i filtra
    exclusivament les dades de La Baells.
    """
    df = exercise2.reanomena_columnes(df)
    print(exercise2.valors_unics_estacio(df))
    df = exercise2.aplica_neteja_noms(df)
    df = exercise2.filtra_baells(df)
    return df


def exec_ex3(df):
    """Executa l'exercici 3 i retorna el ``DataFrame`` actualitzat.

    Converteix les dates, mostra el rang temporal, afegeix la
    representació decimal i genera la gràfica corresponent.
    """
    df = exercise3.converteix_datetime(df)
    antig, nova = exercise3.rang_dates(df)
    print(f"Data inicial: {antig}, data final: {nova}")
    df = exercise3.afegeix_decimal(df)
    exercise3.grafica_volum(df, DEF_IMG)
    return df


def exec_ex4(df):
    """Executa l'exercici 4 i torna la sèrie suavitzada."""
    suau = exercise4.suavitza_senyal(df, window=1500, poly=3)
    exercise4.grafica_suavitzada(df, suau, DEF_IMG_SMOOTH)
    return suau


def exec_ex5(df, suau):
    """Executa l'exercici 5 i mostra els períodes de sequera."""
    periodes = exercise5.calcula_periodes(df, suau)
    formatats = [[ini.strftime("%d/%m/%Y"), fi.strftime("%d/%m/%Y")] for ini, fi in periodes]
    print("Períodes de sequera:", formatats)
    return periodes


def main(args: argparse.Namespace) -> None:
    """Punt d'entrada del programa.

    Executa de manera seqüencial els exercicis indicats
    per l'argument ``-ex`` de la línia d'ordres.
    """
    df = None
    suau = None
    if args.ex is None or args.ex >= 1:
        df = exec_ex1()
    if args.ex is None or args.ex >= 2:
        df = exec_ex2(df)
    if args.ex is None or args.ex >= 3:
        df = exec_ex3(df)
    if args.ex is None or args.ex >= 4:
        suau = exec_ex4(df)
    if args.ex is None or args.ex >= 5:
        exec_ex5(df, suau)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PAC Baells")
    parser.add_argument("-ex", type=int, help="Número d'exercici a executar")
    main(parser.parse_args())
