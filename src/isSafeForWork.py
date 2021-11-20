def isSafeForWork(data):
    if data.find_all('a', href=re.compile("fid=2")):
        return True