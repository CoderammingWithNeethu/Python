from bs4 import BeautifulSoup
import requests
url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
print('-'*10)
#extract all the URLs within a webpage
for link in soup.find_all('a'):
    print(link.get('href'))

'''
from bs4 import BeautifulSoup
with open("example.html") as fp:
   soup = BeautifulSoup(fp)
soup = BeautifulSoup("<html>data</html>")
'''

#https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/