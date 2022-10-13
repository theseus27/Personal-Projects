from bs4 import BeautifulSoup
import requests
import json

# URL = "https://www.sneezefetishforum.com/topic/80409-it-all-starts-with-a-sneeze/page/5"
# page = requests.get(URL, allow_redirects=False)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

URL = "https://www.sneezefetishforum.com/topic/80409-it-all-starts-with-a-sneeze/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
author = "Trynasneeze"
posts = soup.find_all("article")
for post in posts:
    content = post.find_all(class_="cPost_contentWrap")
    for text in content:
        paragraphs = text.find_all("p")
        for p in paragraphs:
            print(p)
    print("---------------------------------------")

print(posts)

#Original Content
