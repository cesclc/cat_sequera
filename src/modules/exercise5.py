"""Funcions de l'exercici 5: càlcul de períodes de sequera."""
from typing import List

import pandas as pd


def calcula_periodes(df: pd.DataFrame, suau: pd.Series, llindar: float = 60.0) -> List[List[float]]:
    """Calcula els períodes on el senyal suavitzat està per sota del llindar."""
    en_sequera = suau < llindar
    periodes = []
    inici = None
    for idx, en in en_sequera.items():
        if en and inici is None:
            inici = df.loc[idx, 'dia_decimal']
        elif not en and inici is not None:
            fi = df.loc[idx - 1, 'dia_decimal']
            periodes.append([float(inici), float(fi)])
            inici = None
    if inici is not None:
        fi = df.loc[en_sequera.index[-1], 'dia_decimal']
        periodes.append([float(inici), float(fi)])
    return periodes
