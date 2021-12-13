from bs4 import BeautifulSoup, Comment

import requests

url = 'https://www.scmp.com/hk'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

# Headline
headline = doc.find(class_='article-title__article-link article-hover-link')
headline_text = " ".join(headline.find_all(
    text=lambda t: not isinstance(t, Comment)))

print(headline_text)
