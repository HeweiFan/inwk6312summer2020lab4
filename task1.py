import string

f = open("doc_1.txt")
 
# lines = f.readlines()
# for i in range(0,lines.__len__(),1):
list = []
     
for line in f:
  # list = []
  stripped_line = line.lower().strip(str.maketrans("",""),string.punctuation).split()
  list.append(stripped_line)
  print(list)
