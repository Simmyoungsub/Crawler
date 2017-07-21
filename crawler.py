import requests

from bs4 import BeautifulSoup



def spider(max_pages):

   page = 1

   while page < max_pages:

      url = 'url' + str(page)

      source_code = requests.get(url)

      plain_text = source_code.text

      soup = BeautifulSoup(plain_text, 'html.parser')

      for link in soup.select('header h2'):
         title = link.string
         print(title)

      page += 1