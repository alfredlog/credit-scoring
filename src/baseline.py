import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score

def split(df: pd.DataFrame, target="TARGET", test_size=0.2, seed=42):
    # TODO: geschichtete Aufteilung → X_train, X_test, y_train, y_test
    # Tipp: Parameter stratify=
    ...

def build_model(X: pd.DataFrame) -> Pipeline:
    # TODO:
    # numerische Spalten:  SimpleImputer(strategy="median", add_indicator=True) → StandardScaler
    # kategoriale Spalten (dtype object): SimpleImputer(strategy="most_frequent") → OneHotEncoder(handle_unknown="ignore")
    # beides in einen ColumnTransformer, danach LogisticRegression(max_iter=1000)
    ...

def evaluate(y_true, y_score, has_bureau) -> pd.DataFrame:
    # TODO: Zeilen (Index) = "all", "thin_file", "has_bureau"
    # Spalten = roc_auc, pr_auc, n, default_rate
    ...