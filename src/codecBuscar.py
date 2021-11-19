def codecBuscar(i):
    codec = i.find('span',{'class':'codec'})
    codec = str(codec).replace('<span class="codec">','')
    codec = str(codec).replace('</span>','')
    return codec