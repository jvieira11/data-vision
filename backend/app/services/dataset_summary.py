import pandas as pd


def summarize_dataframe(df: pd.DataFrame) -> dict:
    columns = []
    for column_name in df.columns:
        columns.append({"name": column_name, "dtype": str(df[column_name].dtype)})

    return {"row_count": df.shape[0], "column_count": df.shape[1], "columns": columns}
