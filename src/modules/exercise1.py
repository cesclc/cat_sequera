"""Funcions de l'exercici 1: carregar el dataset i EDA."""
from pathlib import Path
import pandas as pd


def carrega_dataset(path: Path) -> pd.DataFrame:
    """Carrega el dataset en un DataFrame.

    Parameters
    ----------
    path: Path
        Ruta al fitxer CSV.

    Returns
    -------
    pd.DataFrame
        DataFrame amb les dades carregades.
    """
    df = pd.read_csv(path, sep=";")
    return df


def mostra_head(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna les cinc primeres files."""
    return df.head()


def columnes(df: pd.DataFrame) -> list[str]:
    """Retorna la llista de columnes."""
    return list(df.columns)


def info_dataframe(df: pd.DataFrame) -> str:
    """Retorna la informació del DataFrame."""
    buffer = []
    df.info(buf=buffer)
    return "\n".join(str(line) for line in buffer)
