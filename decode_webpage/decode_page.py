import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.nytimes.com/")
soup = BeautifulSoup(request.content, 'html.parser')
list_of_span = soup.find_all('span')
print(list_of_span)
for text in list_of_span:
    print(text.text)
