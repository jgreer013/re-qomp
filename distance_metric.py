from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_distances


def getDistanceMatrix(list_of_stories):
  vectorizer = TfidfVectorizer(max_df=0.5, max_features=2000,
                              min_df=0.25, encoding='latin-1',
                              stop_words='english', analyzer='word',
                              ngram_range=(1,3))
  
  tf_mat = vectorizer.fit_transform(list_of_stories)
  #dist_mat = euclidean_distances(tf_mat)
  dist_mat = cosine_distances(tf_mat)
  return dist_mat
  
  
  


  
