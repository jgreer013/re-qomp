



def parseFile(filename):
  f = open(filename, 'r')
  stories = []
  
  prevLine = "stop"
  currStory = ""
  for line in f:
    #print("Line:", line)
    
    if ((line == '\r\n' and prevLine == '\r\n') or 
        (line == '\n' and prevLine == '\n')):
      currStory = preProcessStory(currStory)
      stories.append(currStory)
      currStory = ""
    else:
      currStory += preProcessLine(line)
      if (currStory[-1] != " "):
        currStory += " "
    
    
    prevLine = line
    
  currStory = preProcessStory(currStory)
  stories.append(currStory)
    
  return stories
  
  
  
  
def preProcessStory(story):
  story = story.strip().lower()
  return story
  
def preProcessLine(line):
  line = line.strip('\n').strip('\r').replace(":", '')
  return line
