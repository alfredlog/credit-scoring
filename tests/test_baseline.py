import pandas as pd
from src.baseline import split, evaluate

def test_split_is_stratified():
    df = pd.DataFrame({"x": range(100), "TARGET": [1]*10 + [0]*90})
    X_tr, X_te, y_tr, y_te = split(df, test_size=0.2)
    assert len(X_te) == 20
    assert y_te.mean() == 0.1
    assert "TARGET" not in X_tr.columns

def test_evaluate_groups():
    y = pd.Series([0, 1, 0, 1, 0, 1])
    s = pd.Series([0.1, 0.9, 0.2, 0.8, 0.7, 0.3])
    g = pd.Series([True, True, True, True, False, False])
    rep = evaluate(y, s, g)
    assert rep.loc["has_bureau", "roc_auc"] == 1.0
    assert rep.loc["thin_file", "roc_auc"] == 0.0
    assert rep.loc["all", "n"] == 6