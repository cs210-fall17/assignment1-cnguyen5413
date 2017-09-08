"""
Christopher Nguyen
CSC 210, Section 1A
cat.py
This program replicated the cat command on cygwin
"""

import sys

def main():
  files = sys.argv
  
  line_num = 0

  if(len(files) == 1):      #The only argument is the program name
    for input in sys.stdin:
      sys.stdout.write(input) 
    
  elif(len(files) == 2):    #Runs if arguments has no file or only the file
    if("-n" == files[1] or files[1] == "-b"):
      for line in sys.stdin:
        line_num += 1
        if(files[1] == "-b" and len(line) == 0):
          line_num -= 1
          continue

	#number_space accounts for the spaces before the number for greater accuracy
        number_space = max((6-int(len(str(line_num)))),0) * " "
        sys.stdout.write(number_space + str(line_num) + "  " + line)
      return

    else:
      start_index = 1

#The first if of this elif checks whether there were options or not
  elif(len(files) >= 3):
    if(files[1] == "-n" or files[1] == "-b"):
      start_index = 2
    else:
      start_index = 1
 

#This for loops runs throught the entire remaining files, also checking the options
#along the way

  for file in files[start_index:]:
    current_file = open(file)
    for line in current_file.readlines():
      line_num += 1
      if("-n" == files[1] or files[1] == "-b"):
        if(files[1] == "-b" and len(line) == 0):
          line_num -= 1
          continue
        number_space = max((6-int(len(str(line_num)))),0) * " "
        sys.stdout.write(number_space + str(line_num) + "  " + line)
      else:
        sys.stdout.write(line)


main()
