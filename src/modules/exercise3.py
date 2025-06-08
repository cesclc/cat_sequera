"""Funcions de l'exercici 3: transformacions temporals i gràfiques."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


ALUMNE = "Francesc Lucas Carbo"


def converteix_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """Converteix la columna dia a tipus datetime i ordena."""
    df['dia'] = pd.to_datetime(df['dia'], dayfirst=True)
    df = df.sort_values('dia').reset_index(drop=True)
    return df


def rang_dates(df: pd.DataFrame) -> tuple[pd.Timestamp, pd.Timestamp]:
    """Retorna la data més antiga i la més nova."""
    return df['dia'].min(), df['dia'].max()


def to_year_fraction(date: datetime) -> float:
    """Converteix una data en el seu equivalent decimal."""
    year_start = datetime(year=date.year, month=1, day=1)
    next_year_start = datetime(year=date.year + 1, month=1, day=1)
    year_length = (next_year_start - year_start).total_seconds()
    seconds_into_year = (date - year_start).total_seconds()
    return date.year + seconds_into_year / year_length


def afegeix_decimal(df: pd.DataFrame) -> pd.DataFrame:
    """Afegeix la columna dia_decimal."""
    df['dia_decimal'] = df['dia'].apply(lambda d: to_year_fraction(d.to_pydatetime()))
    return df


def grafica_volum(df: pd.DataFrame, path: Path) -> None:
    """Genera la gràfica del volum/percentatge al llarg del temps."""
    fig, ax = plt.subplots()
    ax.plot(df['dia'], df['nivell_perc'])
    ax.set_xlabel('Data')
    ax.set_ylabel('%')
    ax.set_title('Volum La Baells', fontsize=18, pad=15)
    ax.text(0.5, 0.93, ALUMNE, transform=ax.transAxes,
            ha='center', va='top', fontsize=12)
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)
