from bs4 import BeautifulSoup as bs
import requests

base_url = "https://www.reddit.com/"
response= requests.get(base_url)

html = response.content
soup = bs(html, "html.parser")
print(soup.prettify())

topic = soup.select('summary left-nav-topic-tracker')
print(topic[1]["topic"])