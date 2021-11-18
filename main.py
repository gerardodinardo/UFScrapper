import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import json
from tqdm import tqdm
import time


animes = {
    }
fansubs_={
    }
def tituloBuscar(i):

    titulo=i.find('h2')
    if type(titulo) != int:
        if i.find("strong",text="Título original: "):
            titulo = i.find("strong",text="Título original: ").next_sibling.string
        else:                
            titulo.span.decompose()
            titulo=str(titulo).replace('<h2>','')
            titulo=str(titulo).replace('</h2>','')
            titulo=titulo[1:]#limpia el espacio que tiene el título delante.

    return titulo    
            
def resolucionBuscar(i):

    resolucion=i.find('span',{'class':'resolucion'})
    resolucion = str(resolucion).replace('</span>','')
    resolucion = str(resolucion).replace('<span class="resolucion">','')

    if len(resolucion) > 9:
        while len(resolucion) != 9:#borra la basura extra que pueda haber en esta
            resolucion = resolucion[:-1]
        
    resolucion = resolucion.replace(" ","")
    return resolucion

def codecBuscar(i):
    codec = i.find('span',{'class':'codec'})
    codec = str(codec).replace('<span class="codec">','')
    codec = str(codec).replace('</span>','')
    return codec

def fuenteBuscar(i):
    if i.find('span',{'class':'source DVD'}):
        return 'DVD'
    elif i.find('span',{'class':'source Blu-ray'}):
        return 'Blu-ray'   
    elif i.find('span',{'class':'source TV'}):
        return "TV"
    elif i.find('span',{'class':'source HDTV'}):
        return "HDTV"
    elif i.find('span',{'class':'source VHS'}):
        return "VHS" 
    elif i.find('span',{'class':'source Laserdisc'}):
        return "Laserdisc"
    else:
        return "desconocido"

def fansubBuscar(i):

    fansubs = []

    fansub = i.find_all('a', href=re.compile('^fansubs.php?'))
    for i2 in fansub:
        fansub = i2.get_text()
        fansubs.append(fansub)

    return fansubs

def audiosBuscar(i):

    audios = []

    for i in i.find_all("span",{'class':'flag'}):
        audio = i.get('title')
        if ' ' in audio:
            audios.append(audio)

    return audios

def subtitulosBuscar(i):

    subtitulos = [] 
    
    for i in i.find_all("span",{'class':'subtitulos'}):
            for i in i.find_all("span",{'class':'flag'}):
                sub = i.get('title')
                subtitulos.append(sub)
        
    return subtitulos

def yearBuscar(i):
    if i.find('span',{'class':'produccion'}):
        year = i.find('span',{'class':'produccion'})
        year = year.getText()
        year = str(year)
        if len(year) != 4:
            while len(year) > 4:
                year = year[:-1]

        return year
    else:
        return "¿?"


def fansubBuscarId(fansubName):
    fansubs_id = []


    for i2 in fansubName:
        fansub = fansubs_[i2]
        fansubs_id.append(fansub)
    
    return fansubs_id

def fansubsData():

    fansubs_url= 'https://foro.unionfansub.com/fansubs.php'
    fansubs=urllib.request.urlopen(fansubs_url)
    soup = BeautifulSoup(fansubs,'html.parser')
    soup = soup.find('div',{'class':'listado fansubs'})
    id = 1
    
    for i in soup.find_all('div'):
        
        fansub_name = i.get_text()    
        fansubs_[fansub_name] = id
        id += 1
        
    with open('fansubs.json','w',encoding='utf8') as outfile:
        json.dump(fansubs_,outfile,indent=4,ensure_ascii=False)



if __name__ == "__main__":


    fansubsData()

    params = {
        'action': 'do_login',
        'username': '',#introduce tu usuario entre las comillas
        'password': '',#introdude la contraseña entre las comillas
        'loginsubmit': 'Inicia+sesi%C3%B3n'
        }
    login_url = ('https://foro.unionfansub.com/portal.php?')

    with requests.session() as login:
        login.post(login_url, data=params)
        for i in tqdm(range(0, 25000)):
            num = str(i)
            time.sleep(0.1)
            url = 'http://foro.unionfansub.com/showthread.php?tid=' + num
            request = login.get(url)
            soup = BeautifulSoup(request.content,'html.parser')

            for i in soup.find_all('div',{'class':'ficha'}):
                animes[num] = {
                    "Title": tituloBuscar(i),       
                    "Fansub": fansubBuscar(i),
                    "Fansub_id": fansubBuscarId(fansubBuscar(i)),
                    "Resolution": resolucionBuscar(i),
                    "Codec": codecBuscar(i),
                    "Fuente": fuenteBuscar(i),
                    "Audios": audiosBuscar(i),
                    "Subs": subtitulosBuscar(i),
                    "Year": yearBuscar(i)
                }
                print(animes[num]);            

with open('animes.json','w',encoding='utf8') as outfile:
    json.dump(animes,outfile,indent=4,ensure_ascii=False)
