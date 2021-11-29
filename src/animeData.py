import json

def getAnimeData(titulo, year, chapters,premisa,animes,animesIds):

    if titulo in animesIds:
        return animesIds[titulo]
        
    id = len(animes)+1  
    animes[id] = {
        "Title": titulo,
        "Year": year,
        "Chapters": chapters,
        "Synopsis":premisa
        }    

    animesIds[titulo] = id
    


    with open("src/data/animesData.json",'w',encoding='utf8') as outfile:
            json.dump(animes,outfile,indent=4,ensure_ascii=False)
            
    with open("src/data/animesIds.json",'w',encoding='utf8') as outfile:
            json.dump(animesIds,outfile,indent=4,ensure_ascii=False)
    
    return id
