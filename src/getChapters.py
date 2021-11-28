def getChapters(i):
    if i.find('span',{'class':'episodios'}):
        chapters = i.find('span',{'class':'episodios'})
        chapters = chapters.getText()
        return chapters
    
    return "0"
        
        
        