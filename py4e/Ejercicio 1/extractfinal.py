import re
text = open("regex_sum_150277.txt")
num = []
total = 0
for line in text:
    extract = re.findall("[0-9]+", line)
    numbers = num + extract
    for a in numbers:
        total = total + int(a)
print("Result is =", total)
