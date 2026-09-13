import pandas as pd

def clean_data(data):
    cleaned = {}

    for name, df in data.items():
        df = df.copy()
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        # Remove exact duplicate rows
        df = df.drop_duplicates()

        # Standardize object/string columns
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].astype("string").str.strip()

        # Convert known date columns
        for col in df.columns:
            if col.endswith("_date"):
                df[col] = pd.to_datetime(df[col], errors="coerce")

        # Fill numeric missing values with median
        for col in df.select_dtypes(include="number").columns:
            if df[col].isna().any():
                df[col] = df[col].fillna(df[col].median())

        cleaned[name] = df

    return cleaned
