import sys, pathlib; sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
import pandas as pd
from modules.exercise3 import to_year_fraction
from modules.exercise4 import suavitza_senyal
from modules.exercise5 import calcula_periodes


def test_to_year_fraction():
    date = pd.Timestamp('2020-07-02')
    val = to_year_fraction(date.to_pydatetime())
    assert 2020.49 < val < 2020.51


def test_suavitza_senyal():
    df = pd.DataFrame({'nivell_perc': [80, 82, 85]})
    suau = suavitza_senyal(df, window=3, poly=1)
    assert len(suau) == 3


def test_calcula_periodes():
    df = pd.DataFrame({'dia_decimal': [2020.0, 2021.0, 2022.0]})
    suau = pd.Series([70, 50, 70])
    periodes = calcula_periodes(df, suau, llindar=60)
    assert periodes == [[2021.0, 2021.0]]
