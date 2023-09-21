import sys

text_file = sys.argv[1]

f = open(text_file,'r')
file_content = f.readlines()

print(file_content)
