import re

from bs4 import BeautifulSoup


def isAnime(soup):

    pattern = re.compile(r'id=2\">Anime')
    pattern2 = re.compile(r'id=15\">')
    pattern3 = re.compile(r'id=2&')
    pattern4 = re.compile(r'id=15&')
    head = soup.find('h4',{'class':'navigation'})
    data = str(head)
    data = "".join(line.strip() for line in data.split("\n"))
    #print(soup)
    if re.findall(pattern, data) or re.findall(pattern2, data) or re.findall(pattern3, data) or re.findall(pattern4, data):
        return True