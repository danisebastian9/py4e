data = "From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008"
atpos = data.find("@")
print(atpos)
sppos = data.find(" ",atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

words = data.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])


import re
y = re.findall("@([^ ]*)", data)
print(y)

z = re.findall("^From .*@([^ ]*)",data)
print(z)

x = "We just received $10.00 for cookies."
w = re.findall("\$[0-9.]+",x)
print(w)

a = 'From: Using the : character'
b = re.findall('^F.+:', a)
print(b)
