import pandas as pd
from src.data import target_rate, missing_report, flag_thin_file

def test_target_rate():
    assert target_rate(pd.DataFrame({"TARGET": [0, 0, 0, 1]})) == 0.25

def test_missing_report():
    df = pd.DataFrame({"a": [1, None, None, 4], "b": [1, 2, 3, 4]})
    rep = missing_report(df)
    assert list(rep.index) == ["a", "b"]
    assert rep.loc["a", "missing_ratio"] == 0.5

def test_flag_thin_file():
    app = pd.DataFrame({"SK_ID_CURR": [1, 2, 3]})
    bureau = pd.DataFrame({"SK_ID_CURR": [1, 1, 3]})
    out = flag_thin_file(app, bureau)
    assert list(out["has_bureau"]) == [True, False, True]
    assert len(out) == 3
    assert not "has_bureau" in app.columns