import re
text = open("regex_sum_42.txt")
numlist = list()
sum = 0
for line in text:
    line = line.rstrip()
    stuff = re.findall("[0-9]+", line)
    if len(stuff) > 0:

        #nonlist = [int(i) for i in stuff]
        #print(sum(nonlist))
