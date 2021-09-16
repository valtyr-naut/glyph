#valtyr
from encrypt import encrypt
from random import choice
import subprocess
import getpass
import curses
import crypt
import util
import os

def clear() -> None:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass
    return

def bar(runes:list,size:int) -> None:
    i=0
    while i<size:
        print(choice(runes),end='')
        i=i+1
    print(choice(runes),end='\n')
    return

def title() -> None:
    runes=crypt.runes()
    bar(runes,80)
    for line in util.readlines('data/title.txt'):
        print(line.strip('\n'),end='')
        bar(runes,10)
    bar(runes,80)
    return

def tip() -> None:
    print(choice([
        'It is highly recomended that you physically seperate the rune.crypt and glyph.crypt data to maintain maximum security.',

    ]))

def menu_main() -> None:
    print('\n[0] Encrypt\t[2] Whatami\t[*] Autoinstall')
    print('[1] Decrypt\t[3] Config\t[-] Exit')
    while True:
        choice=input('< ')
        if choice=='0':
            menu_encrypt()
        elif choice=='1':
            ...
        elif choice=='2':
            menu_whatami()
        elif choice=='3':
            menu_configure()
        elif choice=='*':
            subprocess.run(['python3','autoinstall.py'])
            break
        elif choice=='-':
            break
        else:
            print('Invalid Input.')
    return

def menu_encrypt() -> None:
    config=util.readjson('data/config.json')
    targets=os.scandir(config['paths']['input'])
    runic=config['extras']['runic']
    print('Targets:'+str(config['paths']['input']))
    for target in targets:
        print('\t'+str(target.name))
    print('Output:')
    print('\trune:\t'+config['paths']['rune'])
    print('\tglyph:\t'+config['paths']['glyph'])
    print('Runic?:\t'+str(runic))
    cont=input('\nContinue?\n< ').lower()
    if cont=='y':
        #TEMP HARDCODED FILE
        encrypt(util.readbytes('input/test.txt'))
    else:
        return

def menu_decrypt() -> None:
    ...

def menu_whatami() -> None:
    print('I am GlyphCrypt; a hardcore encryption application.\nI use various encryption ciphers, size-reduction encoding, and obfuscation methods to keep your data secure.\nOpen the config.json to customize this tool.')
    return

def menu_configure() -> None:
    print('To make changes, open the config.json file.')
    config=util.readjson('data/config.json')
    print('intake: '+config['paths']['input'])
    print('\t-The path to a folder which contains the raw data to be encrypted. Defaults to input.')
    print('rune.crypt: '+config['paths']['rune'])
    print('\t-The path where the encrypted data will be saved. Defaults to output.')
    print('glyph.crypt: '+config['paths']['glyph'])
    print('\t-The path where the encrypted metadata will be saved. Defaults to output.')
    print('auto-delete: '+str(config['decryption']['scrub/delete']))
    print('\t-This signals GlyphCrypt to auto scrub and delete the rune.crypt and glyph.crypt files after decryption. Defaults to True.')
    print('layers: '+str(config['encryption']['layers']))
    print('\t-This indicates the number of encryption layers that will be stacked on top of each other.')

def progress(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix}|{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()