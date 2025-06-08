"""Funcions de l'exercici 4: suavitzat del senyal."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter

from .exercise3 import ALUMNE


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
    ax.set_xlabel('Temps (any)')
    ax.set_ylabel('Volum (%)')
    ax.set_title('Embassament de La Baells', fontsize=18, pad=15)
    ax.text(0.5, 1.04, ALUMNE, transform=ax.transAxes,
            ha='center', va='top', fontsize=10)
    ax.legend()
    ax.grid()
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)
