import pandas as pd
from dataframe import PandasSnapshot


def test_format(snapshot):
    df = pd.DataFrame([['x', 'b'], ['c', 'd']],
                      columns=['col 1', 'col 2'])
    print(df)
    snapshot.assert_match(PandasSnapshot(df))
