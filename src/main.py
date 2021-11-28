import re
import sys
import json
import time
import requests
import urllib.request
from tqdm import tqdm
from isAnime import isAnime
from bs4 import BeautifulSoup
from animeId import getAnimeId
from yearBuscar import yearBuscar
from codecBuscar import codecBuscar
from fuenteBuscar import fuenteBuscar
from fansubBuscar import fansubBuscar
from audiosBuscar import audiosBuscar
from tituloBuscar import tituloBuscar
from isSafeForWork import isSafeForWork
from fansubBuscarId import fansubBuscarId
from getFansubsData import getFansubsData
from resolucionBuscar import resolucionBuscar
from subtitulosBuscar import subtitulosBuscar
from getChapters import getChapters
from getPremisa import getPremisa

animesId = {}
entradas = {}
fansubs={}
data = {}
animesData={}

        
if __name__ == "__main__":

    getFansubsData(fansubs)
    
    #parámetros para el login
    params = {
        'action': 'do_login',
        'username': sys.argv[1],
        'password': sys.argv[2],
        'loginsubmit': 'Inicia+sesi%C3%B3n'
        }
    login_url = ('https://foro.unionfansub.com/portal.php?')

    with requests.session() as login:
        login.post(login_url, data=params)
        
        for i in tqdm(range(0, 100)):
            num = str(i)
            time.sleep(0.01)
            url = 'http://foro.unionfansub.com/showthread.php?tid=' + num
            request = login.get(url)
            soup = BeautifulSoup(request.content,'html.parser')
            
            if isAnime(soup):
                for i in soup.find_all('div',{'class':'ficha'}):
                    helper = len(entradas) + 1
                    titulo =  tituloBuscar(i)
                    anime_id = getAnimeId(titulo,animesId)
                    fansub = fansubBuscar(i)
                    entradas[helper] = {
                        "Anime_title": titulo,       
                        "Anime_id": anime_id,
                        "Fansub": fansub,
                        "Fansub_id": fansubBuscarId(fansubs,fansub),
                        "Resolution": resolucionBuscar(i),
                        "Video Codec": codecBuscar(i),
                        "Chapters": getChapters(i),
                        "Fuente": fuenteBuscar(i),
                        "Audios": audiosBuscar(i),
                        "Subs": subtitulosBuscar(i),
                        "Year": yearBuscar(i),
                        "SFW": isSafeForWork(soup),
                        "premisa" : getPremisa(soup)
                        
                    }
                    print(entradas[helper]);                    
                
    with open('src/data/data.json','w',encoding='utf8') as outfile:
        json.dump(entradas,outfile,indent=4,ensure_ascii=False)
