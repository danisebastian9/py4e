import urllib.request as ur
from bs4 import *

url = input("URL - ")
html = ur.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
for tag in tags:
    print("TAG:", tag)
    print("URL:", tag.get("href", None))
    print("Contents:", tag.contents[0])
    print("Attrs:", tag.attrs)

    
