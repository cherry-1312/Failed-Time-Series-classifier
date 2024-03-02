import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df_features = pd.read_csv('extracted_features_filtered.csv')

df_ids = df_features['index']
df_features = df_features.drop(columns=['index'])  

feature_columns = df_features.columns.difference(['cluster'])
df_features[feature_columns] = df_features[feature_columns].apply(pd.to_numeric, errors='coerce')

n_clusters = 5

kmeans = KMeans(n_clusters=n_clusters)
df_features['cluster'] = kmeans.fit_predict(df_features)


pca = PCA(n_components=2)
df_features['x'] = pca.fit_transform(df_features.iloc[:, :-1])[:, 0]  
df_features['y'] = pca.fit_transform(df_features.iloc[:, :-1])[:, 1]  

df_result = pd.concat([df_ids, df_features], axis=1)

plt.scatter(df_result['x'], df_result['y'], c=df_result['cluster'])

for i, txt in enumerate(df_result['index']):
    plt.annotate(txt, (df_result['x'].iloc[i], df_result['y'].iloc[i]))

plt.title('K-Means Clustering')
plt.show()










