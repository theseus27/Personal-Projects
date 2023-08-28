## Selenium access by CSS Example
<!-- ######
# data = driver.find_elements(By.CSS_SELECTOR, "a")

# for d in data:
#     if "player" in d.get_attribute("href"):
#         link = d.get_attribute("href")
#         print(link)
######
# driver.get(URL)
# data = driver.find_elements(By.CLASS_NAME, 'roster__table')
# links = []
# for d in data:
#     links.append(d.find_elements(By.CLASS_NAME, 'info'))
    #links.append(d.find_elements(By.CSS_SELECTOR, "href"))

# data_list = []
# for x in range(len(data)):
#     data_list.append(data[x].text)

# print(data_list)

#print(links) -->


## Beautiful Soup Example

from bs4 import BeautifulSoup
import requests

URL = "https://www.mlb.com/player/adam-wainwright-425794?stats=gamelogs-r-pitching-mlb&year=2023"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)

## Selenium and lxml Example

import sys
from contextlib import closing

import lxml.html as html
from lxml.html.clean        import Cleaner
from selenium.webdriver     import Firefox
from cachelib.file import FileSystemCache

cache = FileSystemCache('.cachedir', threshold=100000)

url = "https://www.mlb.com/player/adam-wainwright-425794?stats=gamelogs-r-pitching-mlb&year=2023"

page_source = cache.get(url)
if page_source is None:
    # use firefox to get page with javascript generated content
    with closing(Firefox()) as browser:
        browser.get(url)
        page_source = browser.page_source
    cache.set(url, page_source, timeout=60*60*24*7) # week in seconds

root = html.document_fromstring(page_source)
Cleaner(kill_tags=['noscript'], style=True)(root) # lxml >= 2.3.1
print(root.text_content())
