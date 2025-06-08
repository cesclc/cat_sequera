import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

import pandas as pd
from modules import exercise2


def test_reanomena_columnes():
    df = pd.DataFrame({'Dia': ['2020-01-01'], 'Estacio': ['Emb']})
    out = exercise2.reanomena_columnes(df)
    assert 'dia' in out.columns


def test_neteja_nom_estacio():
    nom = 'Embassament de Darnius Boadella (Darnius)'
    assert exercise2.neteja_nom_estacio(nom) == 'Darnius Boadella'

def test_filtra_baells():
    df = pd.DataFrame({'estacio': ['La Baells', 'Foix'], 'dia': ['2020-01-01', '2020-01-02']})
    out = exercise2.filtra_baells(df)
    assert len(out) == 1
