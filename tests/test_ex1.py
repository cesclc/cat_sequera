import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

from pathlib import Path
from modules import exercise1


def test_carrega_dataset():
    df = exercise1.carrega_dataset(Path(__file__).resolve().parents[1]/'data/embassaments.csv')
    assert not df.empty


def test_columnes():
    df = exercise1.carrega_dataset(Path(__file__).resolve().parents[1]/'data/embassaments.csv')
    cols = exercise1.columnes(df)
    assert 'Dia' in cols or 'dia' in cols
