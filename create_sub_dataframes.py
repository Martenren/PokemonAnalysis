import numpy as np
import pandas as pd

def stat_dataframe(df, stats):
    x = (np.array([row.split(', ') for row in stats]))
    rows = [dict(item.split('=') for item in row) for row in x]

    df_stat = pd.DataFrame(rows).astype(int)
    df_stat.insert(0, "name", df["name"])
    df_stat.insert(0, "id", df["id"])

    df_stat["id"].astype("Int64")

    return df_stat

def type_dataframe(df):
    types = ([row.split(', ') for row in df["types"].to_numpy()])
    df_types = pd.DataFrame(types).astype(str)
    df_types.insert(0, "name", df["name"])
    df_types.insert(0, "id", df["id"])

    return df_types