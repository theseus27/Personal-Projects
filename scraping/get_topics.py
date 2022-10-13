import requests                 #type:ignore
from bs4 import BeautifulSoup   #type:ignore
import xml.etree.ElementTree as ET

outfile = open("stories.txt", "w")
   
def check_folders(checked: str):
    if checked[:40] == "https://www.sneezefetishforum.com/topic/":
        return True
    return False
    
def get_topics():
    original_fiction_links = []
    for pagenum in range(1,121):
        URL = f"https://www.sneezefetishforum.com/forum/83-original-fiction/page/{pagenum}.xml/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "xml")
        links = soup.find_all("link")
        for link in links:
            if check_folders(link.contents[0]):
                original_fiction_links.append(link.contents[0])
    return original_fiction_links

def get_story(link):
    num = 1
    paragraphs = []
    hasSoup = True
    URL = link + f"/page/{num}"
    
    page = requests.get(URL, allow_redirects=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.text
    title_split = title.split('-')
    title = title_split[0]
    print(title + "\n\n")
    
    while(hasSoup):
        URL = link + f"/page/{num}"
        page = requests.get(URL, allow_redirects=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        posts = soup.find_all(class_="cPost_contentWrap")
        if len(posts) == 0: hasSoup = False
        for post in posts:
            cls = post.find_all("p")
            for p in cls:
                paragraphs.append(p.contents[0])
        num += 1
    return paragraphs
            

def main():
    # topics = get_topics()
    # print(topics)
    # for topic in topics:
    #     story = get_story(topic)
    #     for paragraph in story:
    #         print(paragraph)
    
    story = get_story("https://www.sneezefetishforum.com/topic/80409-it-all-starts-with-a-sneeze")
    for paragraph in story:
        print(paragraph)

main()