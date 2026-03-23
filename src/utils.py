import pandas as pd

def find_column(df, possible_names):
    for name in possible_names:
        for col in df.columns:
            if name.lower() in col.lower():
                return col
    return None


def map_columns(df):
    return {
        "player": find_column(df, ["player", "name"]),
        "team": find_column(df, ["team"]),
        "kills": find_column(df, ["kills"]),
        "damage": find_column(df, ["damage"]),
        "placement": find_column(df, ["placement", "place"]),
        "match": find_column(df, ["match", "game"])
    }


def clean_data(df, cols):
    df = df.dropna(subset=[
        cols["player"],
        cols["kills"],
        cols["damage"]
    ])
    df = df[df[cols["damage"]] >= 0]
    return df