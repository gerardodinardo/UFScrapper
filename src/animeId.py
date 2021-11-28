import json

def getAnimeId(titulo, animes):

    if titulo in animes:
        return animes[titulo]
        
    id = len(animes)+1  
    animes[titulo] = id
    anime_id = animes[titulo] 

    with open("src/data/animesIds.json",'w',encoding='utf8') as outfile:
            json.dump(animes,outfile,indent=4,ensure_ascii=False)
    
    return anime_id
