from sklearn.cluster import AgglomerativeClustering



def multinomClustering(distance_matrix):
  return AgglomerativeClustering(n_clusters=2, linkage='ward')
