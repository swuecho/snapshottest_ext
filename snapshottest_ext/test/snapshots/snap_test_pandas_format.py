# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_format 1'] = b'PAR1\x15\x04\x15\x14\x15\x18L\x15\x04\x15\x04\x12\x00\x00\n$\x01\x00\x00\x00a\x01\x00\x00\x00c\x15\x00\x15\x12\x15\x16,\x15\x04\x15\x04\x15\x06\x15\x06\x1c6\x00(\x01c\x18\x01a\x00\x00\x00\t \x02\x00\x00\x00\x04\x01\x01\x03\x02&\x88\x01\x1c\x15\x0c\x195\x04\x00\x06\x19\x18\x05col 1\x15\x02\x16\x04\x16x\x16\x80\x01&<&\x08\x1c6\x00(\x01c\x18\x01a\x00\x19,\x15\x04\x15\x04\x15\x02\x00\x15\x00\x15\x04\x15\x02\x00\x00\x00\x15\x04\x15\x14\x15\x18L\x15\x04\x15\x04\x12\x00\x00\n$\x01\x00\x00\x00b\x01\x00\x00\x00d\x15\x00\x15\x12\x15\x16,\x15\x04\x15\x04\x15\x06\x15\x06\x1c6\x00(\x01d\x18\x01b\x00\x00\x00\t \x02\x00\x00\x00\x04\x01\x01\x03\x02&\x80\x03\x1c\x15\x0c\x195\x04\x00\x06\x19\x18\x05col 2\x15\x02\x16\x04\x16x\x16\x80\x01&\xb4\x02&\x80\x02\x1c6\x00(\x01d\x18\x01b\x00\x19,\x15\x04\x15\x04\x15\x02\x00\x15\x00\x15\x04\x15\x02\x00\x00\x00\x15\x02\x19<5\x00\x18\x06schema\x15\x04\x00\x15\x0c%\x02\x18\x05col 1%\x00L\x1c\x00\x00\x00\x15\x0c%\x02\x18\x05col 2%\x00L\x1c\x00\x00\x00\x16\x04\x19\x1c\x19,&\x88\x01\x1c\x15\x0c\x195\x04\x00\x06\x19\x18\x05col 1\x15\x02\x16\x04\x16x\x16\x80\x01&<&\x08\x1c6\x00(\x01c\x18\x01a\x00\x19,\x15\x04\x15\x04\x15\x02\x00\x15\x00\x15\x04\x15\x02\x00\x00\x00&\x80\x03\x1c\x15\x0c\x195\x04\x00\x06\x19\x18\x05col 2\x15\x02\x16\x04\x16x\x16\x80\x01&\xb4\x02&\x80\x02\x1c6\x00(\x01d\x18\x01b\x00\x19,\x15\x04\x15\x04\x15\x02\x00\x15\x00\x15\x04\x15\x02\x00\x00\x00\x16\xf0\x01\x16\x04&\x08\x16\x80\x02\x14\x00\x00\x19,\x18\x06pandas\x18\x9e\x04{"index_columns": [{"kind": "range", "name": null, "start": 0, "stop": 2, "step": 1}], "column_indexes": [{"name": null, "field_name": null, "pandas_type": "unicode", "numpy_type": "object", "metadata": {"encoding": "UTF-8"}}], "columns": [{"name": "col 1", "field_name": "col 1", "pandas_type": "unicode", "numpy_type": "object", "metadata": null}, {"name": "col 2", "field_name": "col 2", "pandas_type": "unicode", "numpy_type": "object", "metadata": null}], "creator": {"library": "pyarrow", "version": "6.0.0"}, "pandas_version": "1.4.3"}\x00\x18\x0cARROW:schema\x18\xf8\x07//////ACAAAQAAAAAAAKAA4ABgAFAAgACgAAAAABBAAQAAAAAAAKAAwAAAAEAAgACgAAAFQCAAAEAAAAAQAAAAwAAAAIAAwABAAIAAgAAAAIAAAAEAAAAAYAAABwYW5kYXMAAB4CAAB7ImluZGV4X2NvbHVtbnMiOiBbeyJraW5kIjogInJhbmdlIiwgIm5hbWUiOiBudWxsLCAic3RhcnQiOiAwLCAic3RvcCI6IDIsICJzdGVwIjogMX1dLCAiY29sdW1uX2luZGV4ZXMiOiBbeyJuYW1lIjogbnVsbCwgImZpZWxkX25hbWUiOiBudWxsLCAicGFuZGFzX3R5cGUiOiAidW5pY29kZSIsICJudW1weV90eXBlIjogIm9iamVjdCIsICJtZXRhZGF0YSI6IHsiZW5jb2RpbmciOiAiVVRGLTgifX1dLCAiY29sdW1ucyI6IFt7Im5hbWUiOiAiY29sIDEiLCAiZmllbGRfbmFtZSI6ICJjb2wgMSIsICJwYW5kYXNfdHlwZSI6ICJ1bmljb2RlIiwgIm51bXB5X3R5cGUiOiAib2JqZWN0IiwgIm1ldGFkYXRhIjogbnVsbH0sIHsibmFtZSI6ICJjb2wgMiIsICJmaWVsZF9uYW1lIjogImNvbCAyIiwgInBhbmRhc190eXBlIjogInVuaWNvZGUiLCAibnVtcHlfdHlwZSI6ICJvYmplY3QiLCAibWV0YWRhdGEiOiBudWxsfV0sICJjcmVhdG9yIjogeyJsaWJyYXJ5IjogInB5YXJyb3ciLCAidmVyc2lvbiI6ICI2LjAuMCJ9LCAicGFuZGFzX3ZlcnNpb24iOiAiMS40LjMifQAAAgAAAEAAAAAEAAAA2P///wAAAQUQAAAAGAAAAAQAAAAAAAAABQAAAGNvbCAyAAAAyP///xAAFAAIAAYABwAMAAAAEAAQAAAAAAABBRAAAAAcAAAABAAAAAAAAAAFAAAAY29sIDEAAAAEAAQABAAAAA==\x00\x18\x1fparquet-cpp-arrow version 6.0.0\x19,\x1c\x00\x00\x1c\x00\x00\x00"\x07\x00\x00PAR1'
