#valtyr
import curses
import json
import decrypt as d

def read(name:str) -> str:
    try:
        return open(name,'r').read()
    except:
        print('ERROR: read('+str(name)+') failed!')
        exit(0)

def readlines(name:str) -> list:
    try:
        return open(name,'r').readlines()
    except:
        print('ERROR: readlines('+str(name)+') failed!')
        exit(0)

def readbytes(name:str) -> bytes:
    try:
        return open(name,'rb').read()
    except:
        print('ERROR: readbytes('+str(name)+') failed!')
        exit(0)

def readjson(name:str) -> dict:
    try:
        return json.loads(read(name))
    except:
        print('ERROR: read_json('+str(name)+') failed!')
        exit(0)

def write(name:str,data:str) -> None:
    try:
        open(name,'w+').write(data)
    except:
        print('ERROR: write('+str(name)+') failed!')
        exit(0)

def writelines(name:str,data:list) -> None:
    try:
        open(name,'w+').write(list)
    except:
        print('ERROR: writelines('+str(name)+') failed!')
        exit(0)

def writebytes(name:str,data:bytes) -> None:
    try:
        open(name,'wb').write(data)
    except:
        print('ERROR: writebin('+str(name)+') failed!')
        exit(0)

def writejson(name:str,data:list) -> None:
    try:
        write(name,json.dumps(data))
    except:
        print('ERROR: write_json('+str(name)+') failed!')
        exit(0)

#user config
def color(color:any) -> None:
    ...

def block(block:list) -> None:
    ...

def save(data:any) -> None:
    writejson()

def load() -> dict:
    return readjson(d.decrypt(readbytes('config.crypt')))

def show() -> None:
    for line in load('settings.json'):
        ...

def path() -> None:
    ...

