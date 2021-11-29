import re

def getPremisa(data):
    pattern = re.compile(r'<\/script> <div><\/div>(.*)<div class="spoil">')
    pattern2 = re.compile(r'<\/script> <div><\/div>(.*)<br\/><br\/><div class=')
    pattern3 = re.compile(r'<\/script> <div><\/div>(.*)<br><br\/><div class=')
    pattern4 = re.compile(r'<\/script> <div><\/div>(.*)<br><br><div class=')
    data = str(data)
    data = "".join(line.strip() for line in data.split("\n"))
    #print(data)
    
    if(re.findall(pattern, data)):
        for m in re.findall(pattern2, data):
            return cleanData(m)
    
    if(re.findall(pattern2, data)):
         for m in re.findall(pattern, data):
             return cleanData(m)
        
    if(re.findall(pattern3, data)):
         for m in re.findall(pattern, data):
             return cleanData(m)
         
    if(re.findall(pattern4, data)):
         for m in re.findall(pattern, data):
             return cleanData(m)
         
    
def cleanData(m):
    
    CLEANR = re.compile(r'<br/><br/><div class="spoil">') 
    m = re.sub(CLEANR, '', m)
    CLEANR = re.compile(r'<.*?>') 
    cleantext = re.sub(CLEANR, '', m)
    return cleantext