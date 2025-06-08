import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

import pandas as pd
from modules import exercise4
from modules import exercise3


def test_suavitza_senyal_values(tmp_path):
    df = pd.DataFrame({'dia':[pd.Timestamp('2020-01-01')+pd.Timedelta(days=i) for i in range(5)], 'nivell_perc':[10,20,30,40,50]})
    suau = exercise4.suavitza_senyal(df, window=5, poly=2)
    file = tmp_path / 'img.png'
    exercise4.grafica_suavitzada(df, suau, file)
    assert file.exists()
    assert len(suau) == 5
