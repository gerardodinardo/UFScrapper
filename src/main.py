import sys
import json
import time
import requests
import urllib.request
from tqdm import tqdm
from bs4 import BeautifulSoup
from yearBuscar import yearBuscar
from codecBuscar import codecBuscar
from fuenteBuscar import fuenteBuscar
from fansubBuscar import fansubBuscar
from audiosBuscar import audiosBuscar
from tituloBuscar import tituloBuscar
from fansubBuscarId import fansubBuscarId
from getFansubsData import getFansubsData
from resolucionBuscar import resolucionBuscar
from subtitulosBuscar import subtitulosBuscar

animes = {
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
        for i in tqdm(range(0, 20)):
            num = str(i)
            time.sleep(0.01)
            url = 'http://foro.unionfansub.com/showthread.php?tid=' + num
            request = login.get(url)
            soup = BeautifulSoup(request.content,'html.parser')

            for i in soup.find_all('div',{'class':'ficha'}):
                animes[num] = {
                    "Title": tituloBuscar(i),       
                    "Fansub": fansubBuscar(i),
                    "Fansub_id": fansubBuscarId(fansubs_,fansubBuscar(i)),
                    "Resolution": resolucionBuscar(i),
                    "Codec": codecBuscar(i),
                    "Fuente": fuenteBuscar(i),
                    "Audios": audiosBuscar(i),
                    "Subs": subtitulosBuscar(i),
                    "Year": yearBuscar(i)
                }
                print(animes[num]);            

with open('src/data/animes.json','w',encoding='utf8') as outfile:
    json.dump(animes,outfile,indent=4,ensure_ascii=False)
