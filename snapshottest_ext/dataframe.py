"""
store pandas as msgpack
"""

from io import BytesIO

import pandas as pd
from snapshottest.formatter import Formatter
from snapshottest.formatters import BaseFormatter


def pandas_to_bytes(df: pd.DataFrame) -> str:
    output = BytesIO()
    df.to_msgpack(output)
    json_str = output.getvalue()
    output.close()
    return json_str


def bytes_to_pandas(raw_bytes) -> pd.DataFrame:
    in_fh = BytesIO(raw_bytes)
    df = pd.read_msgpack(in_fh)
    in_fh.close()
    return df


class PandasSnapshot(object):
    def __init__(self, value):
        self.value = value


class PandasFormatter(BaseFormatter):
    def can_format(self, value):
        """
        dispatcher, decide which format to use
        https://github.com/syrusakbary/snapshottest/blob/master/snapshottest/formatter.py
        @staticmethod
        def get_formatter(value):
            for formatter in Formatter.formatters:
                if formatter.can_format(value):
                    return formatter
        :param value:
        :return:
        """
        return isinstance(value, PandasSnapshot)

    """
        def store(self, data):
            formatter = Formatter.get_formatter(data)
            data = formatter.store(self, data)
            self.module[self.test_name] = data
            
        def assert_match(self, value, name=''):
            self.curr_snapshot = name or self.snapshot_counter
            self.visit()
            if self.update:
                self.store(value)
            else:
                try:
                    prev_snapshot = self.module[self.test_name]
                except SnapshotNotFound:
                    self.store(value)  # first time this test has been seen
                else:
                    try:
                        self.assert_value_matches_snapshot(value, prev_snapshot)
                    except AssertionError:
                        self.fail()
                        raise

    """

    def store(self, formatter, value: PandasSnapshot):
        """ store pd.DataFrame as bytes in snapshot file"""
        return pandas_to_bytes(value.value)

    #def get_imports(self):
    #    """not useful in this one, because we do not deserialize from the bytes directly"""
    #    return ('pandasFormatter', 'PandasSnapshot'),

    def assert_value_matches_snapshot(self, test, test_value: PandasSnapshot, snapshot_value):
        """
        :param test:
        :param test_value: the value in snapshot.assert_mach(value)
        :param snapshot_value: the value of format.store (after load)
        """
        prev_df = bytes_to_pandas(snapshot_value)  # deserialize from bytes to pd.DataFrame
        pd.testing.assert_frame_equal(test_value.value, prev_df)


Formatter.register_formatter(PandasFormatter())
