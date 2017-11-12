from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def getDistanceMatrix(list_of_stories):
  vectorizer = TfidfVectorizer(max_df=0.8, max_features=1000,
                              min_df=0.1, encoding='latin-1',
                              stop_words='english', analyzer='word',
                              ngram_range=(1,3))
  
  tf_mat = vectorizer.fit_transform(list_of_stories)
  dist_mat = 1 - cosine_similarity(tf_mat)
  return dist_mat
  
  
  


  
