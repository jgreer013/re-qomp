import sys
import file_parse as fp
import story_importance as si
import distance_metric as dm



usage = """Usage:   python main.py <userStoryFileName.txt> <filterWord> <resultsFileName>
  <userStoryFileName.txt> is the name of the user story file to be read.
  <filterWord> is the word used to show user stories pertinent to that word.
  <resultsFileName> is the name of the result file."""


def main():
  fName = ""
  filterWord = ""
  
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
  if (filterWord != ""):
    userStories = si.getRelevantStories(userStories, "Workgroup")
    
  dist_mat = dm.getDistanceMatrix(userStories)
  #print(dist_mat[0])
  
  threshold = 0.01
  
  for i in xrange(len(dist_mat)):
    for j in xrange(i, len(dist_mat)):
      if (i != j and dist_mat[i][j] <= threshold):
        print(str(i+1) + "," + str(j+1))
  
    
  
  
  
  
  
  
if __name__ == "__main__": 
  main()
