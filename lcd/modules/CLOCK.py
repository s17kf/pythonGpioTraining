import time

def getTime():
    return time.asctime(time.localtime(time.time()))[11:19]
def getDate():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime[:4] + localtime[8:11] + localtime[4:8] + localtime[20:]


