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