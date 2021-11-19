def audiosBuscar(i):

    audios = []

    for i in i.find_all("span",{'class':'flag'}):
        audio = i.get('title')
        if ' ' in audio:
            audios.append(audio)

    return audios