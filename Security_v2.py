import sys
import os
banner = ('''
██╗  ██╗███╗   ███╗███████╗██╗██╗  ██╗ █████╗ 
██║ ██╔╝████╗ ████║██╔════╝██║██║  ██║██╔══██╗
█████╔╝ ██╔████╔██║█████╗  ██║███████║███████║
██╔═██╗ ██║╚██╔╝██║██╔══╝  ██║██╔══██║██╔══██║
██║  ██╗██║ ╚═╝ ██║███████╗██║██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                              
''')
print(banner)
if "caesarcipher" not in sys.modules or "xorencryption" not in sys.modules  :
    print("[+]Must Install Needed Libraries...")
    needed = str(input('[+]Auto Install(N/y)?: '))
    if needed == 'y':
        os.system('pip install caesarcipher')
        os.system('pip install xorencryption')
    else:
        print('pip install caesarcipher \npip install xorencryption')
        #exit()
######################################################
from caesarcipher import CaesarCipher
from xorencryption import XOREncryption
import time
######################################################
#CaesarCipher
def dk_index_decode(string,x=0,y=26):
    for i in range(x,y):
        cipher = CaesarCipher(string,offset=i)
        print(cipher.decoded)
#print(dk_index_decode('Uryyb,jbeyq',1,15))

def dk_index_decode_v2(string,y=26):     #TO DO
    if y == 0 : return 0
    #return dk_index_decode_v2(string,x=0,y=y-1)
    cipher = CaesarCipher(string,offset=y)
    return dk_index_decode_v2(string,y=y-1)
    print(cipher.decoded)
#print(dk_index_decode_v2('Uryyb,jbeyq',15))

def string_encode(string,x=2):
    cipher = CaesarCipher(string,offset=x)
    print(cipher.encoded) 

def string_decode(string,x=2):
    cipher = CaesarCipher(string,offset=x)
    print(cipher.decoded)
######################################################
#XOR
def xor_encrypt(string,key): 
    XOREncryption().set_plaintext(plaintext=string)
    XOREncryption().set_key(key=key)
    print(XOREncryption().encrypt())

def xor_decrypt(string,key):
    XOREncryption().set_plaintext(plaintext=string)
    XOREncryption().set_key(key=key)
    print(XOREncryption().decrypt())

######################################################
def run_xor():
    again = 'y'
    while again == 'y':
        string = str(input('[+]Enter Your Text: '))
        if string == '' :
            print('[+]Please enter a text!')
            run_xor()
        opt = str(input('[+]Encrypt(en)/Decrypt(de)?: '))
        key = input('[+]Enter your Key: ')
        if opt.lower() == 'en' or opt.lower() == 'encrypt':
            xor_encrypt(string,key)
            #print('[+]Please enter a valid options!')
            #run_xor()
        #elif opt == '' or opt.lower() != 'en' or opt.lower() != 'encrypt'  or opt.lower() != 'de' or opt.lower() != 'decrypt': 
        #  print('[+]Please enter a valid options!')
        #  run_xor()
        elif opt.lower() == 'de' or opt.lower() == 'decrypt' :
            xor_decrypt(string,key)
        else:
            print('[+]Please enter a valid options!')
            run_xor()
        again = str(input('[+]Try Again?(N/y)'))
######################################################
def run_caesarcipher():
    again = 'y'
    while again == 'y':
        string = str(input('[+]Enter Your Text: '))
        if string == '' :
            print('[+]Please enter a text!')
            run_caesarcipher()
        opt = str(input('[+]Encode(en)/Decode(de)?: '))
        x = input('[+]Enter your offset: ')
        if  opt.lower() == 'en' or opt.lower() == 'encode'   :
            if x == '' :
                print('Offest is NULL... \nDefault offset is 2')
                string_encode(string)
            string_encode(string,int(x))
        elif opt.lower() == 'de' or opt.lower() == 'decode':
            if x == '':
                print('[+]Trying With random offset...')
                dk_index_decode(string)
            else : string_decode(string,int(x))
        #elif opt == '' or opt.lower() != 'en' or opt.lower() != 'encode'  :
        else:
            print('[+]Please enter a valid options!')
            run_caesarcipher()
        again = str(input('[+]Try Again?(N/y)'))
######################################################
def run():
    print(banner + '\nWelcome...')
    type = str(input('Wana Xor or Caesar Cipher(x/c): '))
    if type.lower() == 'x' or type.lower() == 'xor':
        run_xor()
    elif type.lower() == 'c' or type.lower() == 'caesar' or type.lower() == 'cipher' or type.lower() == 'caesar cipher' :
        run_caesarcipher()
    else : 
        print('Please Enter a valid option...')
        run()
######################################################
run()
print('Bye...')
time.sleep(1)
exit()
######################################################