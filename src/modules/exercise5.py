"""Funcions de l'exercici 5: càlcul de períodes de sequera."""
from typing import List

import pandas as pd


def calcula_periodes(df: pd.DataFrame, suau: pd.Series, llindar: float = 60.0) -> List[List[pd.Timestamp]]:
    """Calcula els períodes on el senyal suavitzat està per sota del llindar.

    Retorna una llista amb les dates d'inici i fi de cada període en format
    ``pd.Timestamp``.
    """
    en_sequera = suau < llindar
    periodes: List[List[pd.Timestamp]] = []
    inici: pd.Timestamp | None = None
    for idx, en in en_sequera.items():
        if en and inici is None:
            inici = df.loc[idx, 'dia']
        elif not en and inici is not None:
            fi = df.loc[idx - 1, 'dia']
            periodes.append([inici, fi])
            inici = None
    if inici is not None:
        fi = df.loc[en_sequera.index[-1], 'dia']
        periodes.append([inici, fi])
    return periodes
