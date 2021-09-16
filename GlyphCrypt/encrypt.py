#valtyr
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from random import choice
import crypt
import util
import gui

def keygen() -> bytes:
    return get_random_bytes(choice([16,24,32]))

def aes_eax(data:bytes) -> tuple:
    key=keygen()
    cipher=AES.new(key, AES.MODE_EAX)
    data,tag=cipher.encrypt_and_digest(data)  
    return [data,key,tag,cipher.nonce]

def functions() -> list:
    return ['aes_eax']


def encrypt(data:bytes) -> bytes:
    layers=[]
    amount=util.readjson('data\config.json')['encryption']['layers']
    i=0
    while i < amount:
        layer=crypt.layer()
        encry=choice(functions())
        if encry=='aes_eax':
            tmp=aes_eax(data)
            data=tmp[0]
            layer.add('aes_eax',tmp[1],tmp[2],tmp[3],None) 
        elif encry=='aes_cbc':
            ...
        else:
            i=i-1
        layers.append(layer)
        i=i+1
        gui.progress(i,amount,prefix='Encrypting: ',length=50)

    # print(data)
    crypt.glyph(data)
    # util.writebytes('test.crypt',data)
