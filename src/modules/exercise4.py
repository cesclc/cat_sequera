"""Funcions de l'exercici 4: suavitzat del senyal."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter

from .exercise3 import ALUMNE


def suavitza_senyal(df: pd.DataFrame, window: int = 1500, poly: int = 3) -> pd.Series:
    """Aplica el filtre Savitzky-Golay al senyal de percentatge."""
    return pd.Series(savgol_filter(df['nivell_perc'], window_length=window, polyorder=poly), index=df.index)


def grafica_suavitzada(df: pd.DataFrame, suau: pd.Series, path: Path) -> None:
    """Dibuixa la gràfica original i la suavitzada."""
    plt.figure()
    plt.plot(df['dia'], df['nivell_perc'], label='Original', alpha=0.5)
    plt.plot(df['dia'], suau, label='Suavitzat', linewidth=3)
    plt.xlabel('Data')
    plt.ylabel('%')
    plt.title('Volum La Baells')
    plt.suptitle(ALUMNE)
    plt.legend()
    plt.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(path)
    plt.close()
