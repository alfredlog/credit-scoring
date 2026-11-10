import pandas as pd

def load_applications(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def target_rate(df: pd.DataFrame) -> float:
    print(df.mean())
    return df["TARGET"].mean()

def missing_report(df: pd.DataFrame) -> pd.DataFrame:
    missing_ratio = df.isnull().mean(axis=0)

    report = pd.DataFrame({
        "missing_ratio": missing_ratio
    })

    return report.sort_values(
        by="missing_ratio",
        ascending=False
    )

def flag_thin_file(app: pd.DataFrame, bureau: pd.DataFrame) -> pd.DataFrame:
    app = app.copy()
    app["has_bureau"] = app["SK_ID_CURR"].isin(bureau["SK_ID_CURR"])
    return app