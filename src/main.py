import re
import sys
import json
import time
import requests
import urllib.request
from tqdm import tqdm
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

animes = {
    }
entradas = {    
    }
fansubs_={
    }
        

        
if __name__ == "__main__":

    getFansubsData(fansubs_)
    
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
        for i in tqdm(range(0, 2500)):
            num = str(i)
            time.sleep(0.01)
            url = 'http://foro.unionfansub.com/showthread.php?tid=' + num
            request = login.get(url)
            soup = BeautifulSoup(request.content,'html.parser')
            
            if soup.find_all('a', href=re.compile("fid=2")) or soup.find_all('a', href=re.compile("fid=15")):
                for i in soup.find_all('div',{'class':'ficha'}):

                    titulo =  tituloBuscar(i)
                    fansub = fansubBuscar(i)
                    entradas[num] = {
                        "Anime_title": titulo,       
                        "Anime_id":getAnimeId(titulo),
                        "Fansub": fansub,
                        "Fansub_id": fansubBuscarId(fansubs_,fansub),
                        "Resolution": resolucionBuscar(i),
                        "Codec": codecBuscar(i),
                        "Fuente": fuenteBuscar(i),
                        "Audios": audiosBuscar(i),
                        "Subs": subtitulosBuscar(i),
                        "Year": yearBuscar(i),
                        "SFW": isSafeForWork(soup)
                    }
                    print(entradas[num]);                    
                
    with open('src/data/data.json','w',encoding='utf8') as outfile:
        json.dump(entradas,outfile,indent=4,ensure_ascii=False)