import socket
import os
import sys
import random
import errno
import math
from multiprocessing import Process

def process_start(s_sock):

    s_sock.send(str.encode('\n\t\t*#*#*CONNECTED*#*#*\t\t\t'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        #process/calculation
        try:
            bundle, num , value = data.split(":")
            opt = str(bundle)
            qty = int(num)
            prc = float(value)

            if opt[0]  == 'A':
                opt = 'Kemeja'
                prc = 40
                ans = qty * (prc)

            elif opt[0] == 'B':
                opt = 'Tshirt'
                prc = 30
                ans = qty * (prc)

            elif opt[0] == 'C':
                opt = 'Jacket'
                prc = 90
                ans = qty * (prc)

            elif opt[0] == 'D':
                opt = 'Hoodie'
                prc = 70
                ans = qty * (prc)

            elif opt[0] == 'E':
                opt = 'Seluar Jeans'
                prc = 45
                ans = qty * (prc)

            elif opt[0] == 'F':
                opt = 'Seluar Slack'
                prc = 45
                ans = qty * (prc)

            elif opt[0] == 'G':
                opt = 'Seluar Track'
                prc = 25
                ans = qty * (prc)

            else:
                ans = ('ERROR')

            calculate = (str(opt)+ '.... RM'+ str(prc)+ ' ['+ str(qty) + ']: RM' + str(ans))
            sendClient = ans
            keClient = str(opt)
            print(calculate)
            print ('ORDER RECEIVED!! \n')
            #break

        except:
            print ('Connection Terminated \n')
            sendToClient = ('Connection Terminated')
            break

        if not data:
            break

        s_sock.send(str.encode(str(sendClient)))
        s_sock.send(str.encode(str(keClient)))
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

