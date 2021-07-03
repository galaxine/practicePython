# TODO: this is as intended: BS is searching for static content, there are articles that don't seem to find dynamic ones. Later I can modify for selenium

import requests
from bs4 import BeautifulSoup


request = requests.get("http://www.nytimes.com/")
soup = BeautifulSoup(request.content, 'html.parser')
body = soup.body
print(body.prettify())
list_of_span = soup.find_all(class_=["css-xxaj7r e1lsht870", "css-3gcxf0 e1lsht870", "css-wso0n8 e1lsht870", "css-v6dkq5 e1lsht870", "css-1ylc550 e1lsht870"])
real_list = []
for text in list_of_span:
    if text.text != "":
        real_list.append(text.text)
print(real_list)

# search in body output:
# f = open('practicePython/decode_webpage/debug.html', 'w')
# f.writelines(str(body))
# commented it out because I got from it what I wanted and didn't want to format the content every time I run this