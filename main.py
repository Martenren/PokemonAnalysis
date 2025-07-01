import pandas as pd
import numpy as np

import re

import clustering
import create_sub_dataframes
import visualization

if __name__ == '__main__':
    df = pd.read_csv('pokemon_data.csv')
    print(df.head())
    print(df.info())
    print(df.shape)
    print(df.isnull().sum())

    df.drop(df[df["name"] == "eternatus-eternamax"].index, inplace=True)

    stats = df["stats"].to_numpy()

    sums = np.array([sum(map(int, re.findall(r'\d+', stats))) for stats in stats])

    df["total_stats"] = sums

    df_stat = create_sub_dataframes.stat_dataframe(df, stats)

    df_types = create_sub_dataframes.type_dataframe(df)

    visualization.type_plot(df, 3)

    visualization.stat_correlation_plot(df_stat)

    clustering.stat_clustering(df_stat)