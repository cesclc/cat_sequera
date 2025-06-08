import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

import pandas as pd
from modules import exercise3


def test_converteix_datetime():
    df = pd.DataFrame({'dia': ['2020-01-01', '2019-01-01']})
    out = exercise3.converteix_datetime(df)
    assert out['dia'].dtype.kind == 'M'
    assert out.iloc[0, 0].year == 2019
