import sys
import file_parse as fp
import story_importance as si


def main():
  fName = ""
  try:
    fName = sys.argv[1]
  except:
    print("Error: No Filename given/found")
    return
    
  userStories = fp.parseFile(fName)
  
  
  
  
  
  
if __name__ == "__main__": 
  main()
