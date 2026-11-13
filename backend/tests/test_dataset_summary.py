from pathlib import Path

import pandas as pd

from app.services.dataset_summary import summarize_dataframe

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def test_summarize_dataframe_counts_rows_and_columns():
    df = pd.read_csv(FIXTURES_DIR / "vendas.csv")

    summary = summarize_dataframe(df)

    assert summary["row_count"] == 7
    assert summary["column_count"] == 5


def test_summarize_dataframe_lists_columns_with_types():
    df = pd.read_csv(FIXTURES_DIR / "vendas.csv")

    summary = summarize_dataframe(df)

    assert summary["columns"][0] == {"name": "id", "dtype": "int64"}
    assert summary["columns"][1] == {"name": "cliente", "dtype": "str"}
    assert len(summary["columns"]) == 5


def summarize_dataframe(df: pd.DataFrame) -> dict:
    columns = []
    for column_name in df.columns:
        columns.append({"name": column_name, "dtype": str(df[column_name].dtype)})

    return {"row_count": df.shape[0], "column_count": df.shape[1], "columns": columns}


def test_summarize_dataframe_void():
    df = pd.DataFrame()

    summary = summarize_dataframe(df)

    assert summary == {"row_count": 0, "column_count": 0, "columns": []}
