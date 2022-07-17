import re

doc = input()
word = input()

match = re.findall(word, doc)
print(len(match))
