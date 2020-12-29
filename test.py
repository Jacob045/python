import requests   
from lxml import etree   
url = "https://mofanpy.com/tutorials/data-manipulation/scraping/download/"  
response = requests.get(url).content   
html = etree.HTML(response)
b = html.xpath('/html/body/main/div[2]/div[4]/div[1]/p[4]/a/img')  
print(b) 