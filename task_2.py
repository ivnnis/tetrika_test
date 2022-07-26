import requests as rq
from bs4 import BeautifulSoup

letters ='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
result = {}
page = rq.get('https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту')


def get_next_page(next_url: str):
  global result
  page = rq.get('https://ru.wikipedia.org/w/index.php?'+next_url)
  soup = BeautifulSoup(page.content, "html.parser")
  table = soup.find('div', {'class': 'mw-category mw-category-columns'})
  print(table.contents[0].contents[2].text.split('\n'))
  for div in table.contents:
    letter = table.contents[0].contents[0].contents[0]
    if letter not in letters:
      return
    else:
      if letter not in result:
        result[letter] = len(table.contents[0].contents[2].text.split('\n'))
      else:
        result[letter] += len(table.contents[0].contents[2].text.split('\n'))
  tag = soup.find_all('a', text = 'Следующая страница')
  get_next_page(tag[1]['href'].split('?')[1])
  

get_next_page('title=Категория%3AЖивотные_по_алфавиту&from=А')

for key, value in result.items():
  print(key, ': ', value)