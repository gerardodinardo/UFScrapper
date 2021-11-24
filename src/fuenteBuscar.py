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
    elif i.find('span',{'class':'source Web'}):
        return "Web-Rip"
    else:
        return "desconocido"
    