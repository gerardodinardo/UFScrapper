import re

def fansubBuscar(i):

    fansubs = []

    fansub = i.find_all('a', href=re.compile('^fansubs.php?'))
    for i2 in fansub:
        fansub = i2.get_text()
        fansubs.append(fansub)

    return fansubs