import pandas as pd
from snapshottest_ext.dataframe import PandasSnapshot
import pathlib


def test_format(snapshot):
    HERE = pathlib.Path(__file__).parent
    df = pd.read_csv(HERE / 'orders.csv', parse_dates =['Date'])
    print(df)
    snapshot.assert_match(PandasSnapshot(df))
