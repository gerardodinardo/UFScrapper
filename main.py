from bs4 import BeautifulSoup
import urllib.request
import re
import json
from tqdm import tqdm
import time

animes = {
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
            titulo=titulo[1:] #limpia el espacio que tiene el título delante.

    return titulo    
            
def resolucionBuscar(i):

    resolucion=i.find('span',{'class':'resolucion'})
    resolucion = str(resolucion).replace('</span>','')
    resolucion = str(resolucion).replace('<span class="resolucion">','')

    if len(resolucion) > 9:
        #borra la basura extra que pueda haber en esta
        while len(resolucion) != 9:
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


if __name__ == "__main__":

    for i in tqdm(range(0, 20)):

        num = str(i)

        time.sleep(0.1)

        url = 'http://foro.unionfansub.com/showthread.php?tid=' + num
        ourUrl=urllib.request.urlopen(url)
        soup = BeautifulSoup(ourUrl,'html.parser')

        for i in soup.find_all('div',{'class':'ficha'}):

            animes[num] = {
                "Title": tituloBuscar(i),       
                "Fansub": fansubBuscar(i),
                "Resolution": resolucionBuscar(i),
                "Codec": codecBuscar(i),
                "Fuente": fuenteBuscar(i),
                "Audios": audiosBuscar(i),
                "Subs": subtitulosBuscar(i),
                "Year": yearBuscar(i)
            }

with open('data.json','w',encoding='utf8') as outfile:
    json.dump(animes,outfile,indent=4,ensure_ascii=False)