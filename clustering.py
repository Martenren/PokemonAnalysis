from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def stat_clustering(df_stat):
    X = df_stat.drop(['id', 'name'], axis=1)
    y_pred = KMeans(n_clusters=5, random_state=42).fit_predict(X)

    df_stat['Cluster'] = y_pred

    pca = PCA(n_components=2)
    df_stat[['x', 'y']] = pca.fit_transform(X)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_stat, x='x', y='y', c=y_pred)
    plt.title("K-Means Clustering of Pokémon (based on stats)")
    plt.show()

    print(df_stat.groupby('Cluster')[df_stat.drop(['id', 'name'], axis=1).columns.values].mean().to_string())

    print(df_stat['name'][df_stat['Cluster'] == 0].to_string())