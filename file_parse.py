


# Function to parse user story file
# Input: User Story Filename as a string (i.e. "UCRATE-47-USs.txt")
def parseFile(filename):
  f = open(filename, 'r')
  stories = []
  
  prevLine = "stop"
  currStory = ""
  
  # Iterate through all lines in the file
  for line in f:
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
    
    
  # Add the last user story (due to file not ending at the correct location)
  currStory = preProcessStory(currStory)
  stories.append(currStory)
    
  return stories
  
  
  
# Remove trailing whitespace and change everything to lowercase
def preProcessStory(story):
  story = story.strip().lower()
  return story
  
# Remove newlines, returns (windows why), and remove colons
def preProcessLine(line):
  line = line.strip('\n').strip('\r').replace(":", '')
  return line
