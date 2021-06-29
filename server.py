import socket
import os
import sys
import json
import random
import errno
import math
from multiprocessing import Process

def process_start(s_sock):

    s_sock.send(str.encode('\n\t\t\t\t*#*#*LIST*#*#*\t\t\t'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        #process/calculation
        try:
            menu, num , value = data.split(":")
            opt = str(menu)
            qty = int(num)
            prc = float(value)

            if opt[0]  == 'A':
                opt = 'Kemeja'
                prc = 5.3
                ans = qty * (prc)
            elif opt[0] == 'B':
                opt = 'Tshirt'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'C':
                opt = 'Jacket'
                prc = 7
                ans = qty * (prc)
            elif opt[0] == 'D':
                opt = 'Hoodie'
                prc = 6
                ans = qty * (prc)
            elif opt[0] == 'E':
                opt = 'Seluar Jeans'
                prc = 5
                ans = qty * (prc)
             elif opt[0] == 'F':
                opt = 'Seluar slack'
                prc = 3
                ans = qty * (prc)
            elif opt[0] == 'G':
                opt = 'Seluar Track'
                prc = 3.50
                ans = qty * (prc)
            elif opt[0] == 'H':
                opt = 'Topi'
                prc = 3.80
                ans = qty * (prc)
            else:
                ans = ('ERROR')

            sendtoCli = (str(opt)+ '.... RM'+ str(prc)+ ' ['+ str(qty) + ']: RM' + str(ans))
            sendClient = ans
            print(sendtoCli)
            print ('ORDER RECEIVED!!')
            #break
        except:
            print ('Connection Terminated')
            sendtoCli = ('Connection Terminated')
            break
        if not data:
            break

        s_sock.send(str.encode(str(sendClient)))
    s_sock.close()

if __name__ == '__main__':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("",8888))
        print("listening...")
        s.listen(3)
        try:
                while True:
                        try:
                                s_sock, s_addr = s.accept()
                                print('Client from : ' + str(s_addr))
                                p = Process(target=process_start, args=(s_sock,))
                                p.start()

                        except socket.error:
                                print('got a socket error')

        except Exception as e:
                print("an exception occurred!")
                print(e)
                sys.exit(1)
        finally:
                s.close()
