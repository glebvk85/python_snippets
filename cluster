num_clusters = 5

# Метод к-средних - KMeans
from sklearn.cluster import KMeans

km = KMeans(n_clusters=num_clusters)
idx = km.fit(X)
clusters = km.labels_.tolist()

print(clusters)

# MiniBatchKMeans
from sklearn.cluster import MiniBatchKMeans

mbk = MiniBatchKMeans(init='random', n_clusters=num_clusters) #(init='k-means++', ‘random’ or an ndarray)
mbk.fit_transform(X)
miniclusters = mbk.labels_.tolist()
print (miniclusters)

# DBSCAN
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_
print(labels)

# Аггломеративная класстеризация
from sklearn.cluster import AgglomerativeClustering

agglo1 = AgglomerativeClustering(n_clusters=num_clusters, affinity='euclidean') #affinity можно выбрать любое или попробовать все по очереди: cosine, l1, l2, manhattan
answer = agglo1.fit_predict(X.toarray())
print(answer)
