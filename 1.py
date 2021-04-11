import requests
from bs4 import BeautifulSoup as bs
username=input('Input username:  ')
url='http://github.com/'+username
req=requests.get(url)
soup=bs(req.content,'html.parser')
image=soup.find('img',{'alt':'Avatar'})['src']
print(image)