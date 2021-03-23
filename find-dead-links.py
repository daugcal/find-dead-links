#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def urlCrawl(url, depth):
    raw = requests.get(url)
    soup = BeautifulSoup(raw.content, features='html.parser')
    
    goodLinks=[]
    for rawRef in soup.find_all('a', href=True):
        link= rawRef.get("href")
        try:
            if link.startswith("/"):
                link = url+link
            if requests.get(link).status_code not in [200, 302]:
                print("BAD LINK: %s" % link)
            else:
                goodLinks.append(link)        
        except:
            print("BAD LINK: %s" % link)
    if depth != 0:
        for goodLink in goodLinks:
            urlCrawl(goodLink, depth-1)


if __name__ == '__main__':
    from sys import argv
    progName = argv[0]
    depth = 0
    url = ""
    if len(argv) <= 2:
        print("Error: Usage: %s <url> OR %s -<depth> <url>" % (progName,progName))
        exit(1)
    if argv[1].startswith('-'):
        depth = int(argv[1][1:])
        url = argv[2]
    else:
        url = argv[1]
    
    urlCrawl(url, depth)
