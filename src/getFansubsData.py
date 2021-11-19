import json
import urllib.request
from bs4 import BeautifulSoup
def getFansubsData(fansubs_):

    fansubs_url= 'https://foro.unionfansub.com/fansubs.php'
    fansubs=urllib.request.urlopen(fansubs_url)
    soup = BeautifulSoup(fansubs,'html.parser')
    soup = soup.find('div',{'class':'listado fansubs'})
    id = 1
    
    for i in soup.find_all('div'):
        
        fansub_name = i.get_text()    
        fansubs_[fansub_name] = id
        id += 1
        
    with open("src/data/fansubs.json",'w',encoding='utf8') as outfile:
        json.dump(fansubs_,outfile,indent=4,ensure_ascii=False)
