from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start=%s&filter='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
ret = Request(url, headers=headers)
html = urlopen(ret).read().decode('utf-8')
# print(html)

soup = BeautifulSoup(html,features='lxml')
urls = soup.find_all("span",{"class":"title"})
  
i = 0
for url in urls:
    if(url.get_text()[1] != '/'):
        print(i)
        i = i + 1
        print(url.get_text())    