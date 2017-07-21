import requests
from bs4 import BeautifulSoup

def spider(url):
   list = []
   source_code = requests.get(url)
   plain_text = source_code.text
   soup = BeautifulSoup(plain_text, 'html.parser')

   for link in soup.select('.list_news li dt a'):
      title = link.string
      href = link.get('href');
      dic = {'title' : title, 'href' : href}
      list.append(dic)

   return list

def htmlGenerator(list):
   f = open("test.html",'w')
   f_str = '';
   template_top = '<!doctype><html><head></head><body>'
   template_bottom = '</body></html>'

   f_str += template_top

   for item in list:
      div = '<div><a href='+ item['href'] + '>' + item['title'] + '</a></div>'
      f_str += div

   f_str += template_bottom
   f.write(f_str)

   f.close()

htmlGenerator(spider('url'))