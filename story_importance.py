import file_parse as fp


# Returns a list of relevant user stories based on the relevant string
# String is assumed to be one word for this assignment
def getRelevantStories(list_of_stories, relevantString):
  
  # Normalize string using same mechanism as read-in lines
  normString = fp.preProcessStory(fp.preProcessLine(relevantString))
  relevantStories = []
  
  # Find all user stories relevant by checking if string is contained
  # Basic method which can be expanded upon later for other uses
  for story in list_of_stories:
    wordList = story.split(" ")
    for word in wordList:
      if (word.find(normString) != -1):
        relevantStories.append(story)
        break;
        
  return relevantStories
    
