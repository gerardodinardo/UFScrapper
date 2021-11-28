import re

def getPremisa(data):
    pattern = re.compile(r'<\/script> <div><\/div>(.*)<div class="spoil">')
    pattern2 = re.compile(r'<\/script> <div><\/div>(.*)<br\/><br\/><div class=')
    data = str(data)
    data = "".join(line.strip() for line in data.split("\n"))
    
    if(re.findall(pattern2, data)):
         for m in re.findall(pattern, data):
             return m
    
    for m in re.findall(pattern2, data):
        return m