import urllib.request as ur
from bs4 import *

url = input('URL - ')
html = ur.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count_spans = 0
sum = 0

spans = soup('span')
for span in spans:
   sum += int(span.contents[0])
   count_spans += 1

print('Count ', count_spans)
print('Sum ', sum)
