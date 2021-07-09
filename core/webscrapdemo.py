import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

from urllib.error import URLError

page = requests.get("https://www.thehindu.com/")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())