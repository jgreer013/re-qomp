import sys
import file_parse as fp
import story_importance as si
import distance_metric as dm
import read_answer_set as ras
import tensor_functionality as tenf



usage = """Usage:   python main.py <userStoryFileName.txt> <filterWord> <resultsFileName>
  <userStoryFileName.txt> is the name of the user story file to be read.
  <filterWord> is the word used to show user stories pertinent to that word.
  <resultsFileName> is the name of the result file."""


def main():
  fName = ""
  filterWord = ""
  
  #print "Reading Answer Set Files"
  answer_set = ras.getAnswerSet("AnswerSetMetadata.txt")
  answer_set.extend(ras.getAnswerSet("AnswerSetWorkgroup.txt"))
  
  #print "Reading Input Files"
  # Attempt to read argument
  try:
    fName = sys.argv[1]
  except:
    print("Error: No filename given")
    print(usage)
    return
    
  try:
    filterWord = sys.argv[2]
  except:
    filterWord = ""
    
  userStories = fp.parseFile(fName)
  userStories = si.getRelevantStories(userStories, filterWord)
  
  orderedStories = []
  for story in sorted(userStories.keys()):
    orderedStories.append(userStories[story])
    
  #print "Generating TFIDF Vectors" 
  tf_mat = dm.getTFIDFVectors(orderedStories)
    
  dist_mat = dm.getDistanceMatrix(tf_mat)
  
  #print "Generating Training Sets"
  training_set = ras.generateTrainingSets(userStories, tf_mat, answer_set)
  
  test_set = ras.generateTrainingSets(userStories, tf_mat, answer_set)
  
  #print "Training Sets Generated: " + str(len(training_set))
  
  #final_predictions = tenf.trainTF(training_set, training_set)
  
  threshold = 0.9
  
  # Print out vals
  for i in xrange(len(test_set)):
    a = i / (len(orderedStories)-1)
    b = i % (len(orderedStories)-1)
    if (b >= a):
      b = b + 1
      
    val = test_set[i][2]
    
    if (val[1] == 1 and b > a):
      print str(a+1) + "," + str(b+1)
    
  
  # Rebuild results from one dimensional array
  """
  for i in xrange(len(orderedStories)):
    for j in xrange(len(orderedStories)):
      count = i*46+j-1
      if (i != j):
        print str(i) + ' ' + str(j) + ' ' + str(count)"""
  
    
  
  
  
  
  
  
if __name__ == "__main__": 
  main()
