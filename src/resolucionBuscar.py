def resolucionBuscar(i):

    resolucion=i.find('span',{'class':'resolucion'})
    resolucion = str(resolucion).replace('</span>','')
    resolucion = str(resolucion).replace('<span class="resolucion">','')

    if len(resolucion) > 9:
        while len(resolucion) != 9:#borra la basura extra que pueda haber en esta
            resolucion = resolucion[:-1]
        
    resolucion = resolucion.replace(" ","")
    return resolucion