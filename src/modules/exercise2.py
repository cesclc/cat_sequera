"""Funcions de l'exercici 2: neteja i filtratge."""
import pandas as pd
import re


noms_columnes = {
    'Dia': 'dia',
    'Estacio': 'estacio',
    'Nivell_msnm': 'nivell_msnm',
    'Nivell_perc': 'nivell_perc',
    'Volum': 'volum'
}


def reanomena_columnes(df: pd.DataFrame) -> pd.DataFrame:
    """Reanomena les columnes segons el diccionari global."""
    return df.rename(columns=noms_columnes)


def valors_unics_estacio(df: pd.DataFrame) -> list[str]:
    """Retorna els valors únics de la columna estacio."""
    return sorted(df['estacio'].unique())


def neteja_nom_estacio(nom: str) -> str:
    """Neteja el nom de l'estació eliminant 'Embassament de' i el municipi."""
    nom = re.sub(r'^Embassament de\s*', '', nom)
    nom = re.sub(r'\s*\([^)]*\)', '', nom)
    return nom.strip()


def aplica_neteja_noms(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica la neteja de noms a la columna estacio."""
    df['estacio'] = df['estacio'].apply(neteja_nom_estacio)
    return df


def filtra_baells(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra les dades corresponents a La Baells."""
    return df[df['estacio'] == 'La Baells'].copy()
