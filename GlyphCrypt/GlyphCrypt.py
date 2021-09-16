#!/usr/bin/env python3
from random import choice
from time import sleep
import argparse
import util
import gui




if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='GlyphCrypt : Hardcore Encryption')
    # parser.add_argument('-g',dest='glyph',action='store',default=None,help='Optional:Specify a json file to generate a crypto.glyph. Used to streamline RuneCrypt and ignore all cli args.')
    # parser.add_argument('-f',dest='data',action='store',default=None,help='Used to flag a file for encryption/decryption. ex. -f example.txt or rune.glyph.')
    # parser.add_argument('-d',dest='de',action='store',default=None,help='Optional:Flag used to signal the decryption operation : specify the path to crypto.glyph.')
    # parser.add_argument('-e',dest='en',action='store',default=None,help='Optional:Specify encryption layers seperated by dashes. ex. random-random-random-random. Default uses 20 random layers. available layers:fernet, aes_eax, aes_cbc, arc2_eax, arc2_cbc, arc4')
    # parser.add_argument('-decoy',dest='decoy',action='store',nargs='?',default=False,const=True,help='Optional:Advanced:Signal that you want decoys made. This produces identical encrypted files of the same size, but with garbage data. The cryptoglyph for the decoy is not saved and the cryptoglyph for the real data cannot decrypt the decoy. ex. -decoy True or t.')
    # parser.add_argument('-huff',action='store',nargs='?',default=False,const=True,help='Under Construction:Optional:Advanced:Specify \'True\' to enable huffman encoding on the encrypted data to reduce final size. ex. -huff True or t.')
 
    # args=parser.parse_args()

    gui.clear()
    gui.title()
    gui.menu_main()
    exit(0)