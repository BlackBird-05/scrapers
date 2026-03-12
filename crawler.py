import requests
from requests import get
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

#crawler
base = ""
baseLength = len(base) - 1
visited = set()
to_visit = [base]
all_links = []


def crawler(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = bs(response.content, "html.parser")
        links = []
        for link in soup.find_all("a", href=True):
            nexturl = urljoin(url, link["href"])
            if site_checker(nexturl):
                links.append(nexturl)

        return links
    
    except requests.exceptions.RequestException as e:
        print(f"Error crawling {url}: {e}")
        return []
        
def site_checker(url):
    return base[0:baseLength] == url[0:baseLength]

def begincrawl(base):
    while to_visit:
        current = to_visit.pop(0)
        if current in visited:
            continue
        print(f"Crawling: {current}")
        all_links.append(current)
        new = crawler(current)
        visited.add(current)
        to_visit.extend(new)

    print("crawling finished")
    print(all_links)

begincrawl(base)



