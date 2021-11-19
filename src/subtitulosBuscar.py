def subtitulosBuscar(i):

    subtitulos = [] 
    
    for i in i.find_all("span",{'class':'subtitulos'}):
            for i in i.find_all("span",{'class':'flag'}):
                sub = i.get('title')
                subtitulos.append(sub)
        
    return subtitulos