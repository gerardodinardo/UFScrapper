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