"""Funcions de l'exercici 4: suavitzat del senyal."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter

from .exercise3 import configura_ax, guarda_figura


def suavitza_senyal(
    df: pd.DataFrame, window: int = 1500, poly: int = 3
) -> pd.Series:
    """Aplica el filtre Savitzky-Golay al senyal de percentatge."""
    filt = savgol_filter(df['nivell_perc'], window_length=window, polyorder=poly)
    return pd.Series(filt, index=df.index)


def grafica_suavitzada(df: pd.DataFrame, suau: pd.Series, path: Path) -> None:
    """Dibuixa la gràfica original i la suavitzada."""
    fig, ax = plt.subplots()
    ax.plot(df['dia'], df['nivell_perc'], label='Original', alpha=0.5)
    ax.plot(df['dia'], suau, label='Suavitzat', linewidth=3)
    configura_ax(ax)
    ax.legend()
    guarda_figura(fig, path)
