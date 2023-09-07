import requests
from bs4 import BeautifulSoup
#爬蟲

url='https://www.ptt.cc/bbs/Gossiping/index.html'
#設定cookies值
cookies={'over18':'1'}
r=requests.get(url,cookies=cookies)
print(r.text)
