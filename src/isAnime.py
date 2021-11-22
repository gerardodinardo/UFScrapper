import re

from bs4 import BeautifulSoup


def isAnime(soup):

    pattern = re.compile(r'id=2\">Anime')
    pattern2 = re.compile(r'id=15\">')
    head = soup.find('h4',{'class':'navigation'})
    data = str(head)
    data = "".join(line.strip() for line in data.split("\n"))

    if re.findall(pattern, data) or re.findall(pattern2, data):
        return True