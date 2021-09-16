#valtyr
# from encrypt import runecode
import util
import os
import sys

def runes()->list:
    return ["ᚠ","ᚢ","ᚦ","ᚩ","ᚱ","ᚳ","ᚷ","ᚹ","ᚻ","ᚾ","ᛁ","ᛂ","ᛇ","ᛈ","ᛉ","ᛋ","ᛏ","ᛒ","ᛖ","ᛗ","ᛚ","ᛝ","ᛟ","ᛞ","ᚪ","ᚫ","ᚣ","ᛡ","ᛠ","ᚠᚢ","ᚠᚣ","ᚠᚦ",'ᚠᚩ','ᚠᚪ','ᚠᚫ','ᚠᚱ','ᚠᚳ','ᚠᚷ','ᚠᚹ','ᚠᚻ','ᚠᚾ','ᚠᛁ','ᚠᛂ','ᚠᛇ','ᚠᛈ','ᚠᛉ','ᚠᛋ','ᚠᛏ','ᚠᛒ','ᚠᛖ','ᚠᛗ','ᚠᛚ','ᚠᛝ','ᚠᛞ','ᚠᛟ','ᚠᛠ','ᚠᛡ','ᚢᚠ','ᚢᚣ','ᚢᚦ','ᚢᚩ','ᚢᚪ','ᚢᚫ','ᚢᚱ','ᚢᚳ','ᚢᚷ','ᚢᚹ','ᚢᚻ','ᚢᚾ','ᚢᛁ','ᚢᛂ','ᚢᛇ','ᚢᛈ','ᚢᛉ','ᚢᛋ','ᚢᛏ','ᚢᛒ','ᚢᛖ','ᚢᛗ','ᚢᛚ','ᚢᛝ','ᚢᛞ','ᚢᛟ','ᚢᛠ','ᚢᛡ','ᚣᚠ','ᚣᚢ','ᚣᚦ','ᚣᚩ','ᚣᚪ','ᚣᚫ','ᚣᚱ','ᚣᚳ']

def freq(data:bytes) -> dict:
    histogram=None
    return histogram

def runecode(data:bytes,freq:dict) -> bytes:
    key={}
    return data,key

class layer:
    def json(self) -> dict:
        return {"op":self.operation,"key":self.key,"tag":self.tab,"nonce":self.nonce,"iv":self.iv}

    def add(self,operation:str,key:bytes,tag:bytes,nonce:bytes,iv:bytes) -> None:
        self.add_op(operation)
        self.add_key(key)
        self.add_tag(tag)
        self.add_nonce(nonce)
        self.add_iv(iv)

    def add_op(self, operation:str) -> None:
        self.operation=operation
    
    def add_key(self,key:bytes) -> None:
        self.key=str(key)

    def add_tag(self,tab:bytes) -> None:
        self.tab=tab
    
    def add_nonce(self,nonce:bytes) -> None:
        self.nonce=nonce
    
    def add_iv(self,iv:bytes) -> None:
        self.iv=str(iv)

    key=None
    operation=None
    tab=None
    nonce=None
    iv=None

def glyph(data:bytes) -> None:
    #has to be readbytes
    #apply runes as first layer?
    ...    
    #use last entry in hacking bookmarks