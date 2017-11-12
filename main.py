import sys
import file_parse as fp
import story_importance as si


def main():
  fName = ""
  
  # Attempt to read argument
  try:
    fName = sys.argv[1]
  except:
    print("Error: No filename given")
    return
    
  userStories = fp.parseFile(fName)
  
  
  
  
  
  
if __name__ == "__main__": 
  main()
