import random
import numpy

# Returns a list A of lists B, with each B containing pairs of test case numbers
def getAnswerSet(answer_set_filename):
  pairs = []
  with open(answer_set_filename,'r') as f:
    for line in f:
      pair = line.strip().split(',')
      pairs.append(pair)
    
  return pairs
  
def generateTrainingSets(story_dict, tfidf_mat, list_of_answers):
  training_set = []
  story_nums = sorted(story_dict.keys())
  for s1 in story_nums:
    for s2 in story_nums:
      if (s1 != s2):
        for pair in list_of_answers:
          p1 = int(pair[0])
          p2 = int(pair[1])
          TruePair = False
          if ((p1 == s1 and p2 == s2) or (p2 == s1 and p1 == s2)):
            training_set.append( (tfidf_mat[s1-1,:].toarray(), tfidf_mat[s2-1,:].toarray(), [0, 1])  )
            #training_set.append( (tfidf_mat[s2-1,:].toarray(), tfidf_mat[s1-1,:].toarray(), [0, 1])  )
            TruePair = True
            break;
         
        if (TruePair == False):
          training_set.append( (tfidf_mat[s1-1,:].toarray(), tfidf_mat[s2-1,:].toarray(), [1, 0])  )
          #training_set.append( (tfidf_mat[s2-1,:].toarray(), tfidf_mat[s1-1,:].toarray(), [1, 0])  )
    
  return training_set
  

def getRandomBatch(training_set, amount):
  batch = random.sample(training_set, amount)
  x = []
  y = []
  for row in batch:
    x.append(numpy.append(row[0],row[1]))
    y.append(row[2])
    
  x = numpy.asarray(x)
  y = numpy.asarray(y)
  return (x, y)
  
def getNonRandomBatch(training_set, amount):
  x = []
  y = []
  for row in training_set:
    x.append(numpy.append(row[0],row[1]))
    y.append(row[2])
    
  x = numpy.asarray(x)
  y = numpy.asarray(y)
  return (x, y)
  
