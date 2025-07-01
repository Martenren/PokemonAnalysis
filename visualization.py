import matplotlib.pyplot as plt
import seaborn as sns

def base_stats_plot(df):
    sns.countplot(x=df["total_stats"])
    plt.show()

def height_weight_plot(df):
    sns.scatterplot(x=df["height"], y=df["weight"])
    plt.show()

def type_plot(df, limit_count=None):
    _df = df.copy()
    type_counts = _df["types"].value_counts()
    rotation = 90
    if limit_count is not None:
        top_types = type_counts[type_counts > limit_count]
        _df["types"] = _df["types"].apply(lambda x: x if x in top_types else "uncommon types")
        if limit_count > 2:
            rotation = 30
    type_order = _df["types"][_df["types"] != "uncommon types"].value_counts().index
    plt.figure(figsize=(80, 12))
    ax = sns.countplot(x=_df["types"][_df["types"] != "uncommon types"], palette='rainbow', hue=_df["types"],
                       order=type_order, legend=False)
    ax.tick_params(axis='x', rotation=rotation)
    for c in ax.containers:
        ax.bar_label(c, fmt=lambda x: f'{int(x)}')
    plt.show()

def stat_correlation_plot(df_stat):
    plt.figure(figsize=(15, 10))
    sns.heatmap(df_stat.drop(['id', 'name'], axis=1).corr(), annot=True, cmap="YlGnBu")
    plt.show()