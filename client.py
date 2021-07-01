import socket
import signal
import sys

socket = socket.socket()
host = '192.168.56.103'
port = 8888

print('Waiting for connection...')

try:
        socket.connect((host, port))

except socket.error as e:
        print(str(e))


Response = socket.recv(2048)
print(Response.decode("utf-8"))

print ( "\n============================================================================\n"
                 "\t* *** *** ***WELCOME TO AIM'S BUNDLE ONLINE SHOP *** **** *** *\t\t\t\n"
                        "============================================================================\n");

print("   --------------------------------------------------------------------------")
print("         | [A]  Kemeja" , end =" ")
print("                         [B]  Tshirt            |")
print("         | [C]  Jacket", end =" ")
print("                         [D]  Hoodie            |")
print("         | [E]  Seluar Jeans", end =" ")
print("                   [F]  Seluar Slack      |")
print("         | [G]  Seluar Slack", end =" ")
print("                                          |")
print("   --------------------------------------------------------------------------")
print("============================================================================")



while True:
    opt = input('\nSelect Your Option [Code Bundle] Press "X" if you are done..\n> ')
    if opt == "A" or opt == "B" or opt == "C" or opt == "D" or opt == "E" or opt == "F" or opt == "G":
        qty = input("\nQuantity per Order: ")
        prc = '0.00'
        total = 0.00
        keServer = opt + ":" + qty + ":" + prc
        socket.send(str.encode(keServer))
        price = socket.recv(1024)
        price = float(price)
        prod = socket.recv(1024)
        prod = str(prod)

        size = input ('We have S/M/L/XL/2XL/3XL size. If size XL-->3XL, add RM10.00 \nChoose your size: ')
        if size == "S":
           saiz = "S\n"
           total = price

        elif size == "M":
           saiz = "M\n"
           total = price

        elif size == "L":
           saiz = "L\n"
           total = price

        elif size == "XL":
           saiz = "XL [+RM10.00]\n"
           total = price + 10.00

        elif size == "2XL":
           saiz = "2XL [+RM10.00]\n"
           total = price + 10.00

        elif size == "3XL":
           saiz = "3XL [+10.00]\n"
           total = price + 10.00


        else:
           print("WRONG INPUT SIZE!!!\n")
           break

        add = input('\nAdd Onn [+RM 10.00] (Y/N): ')
        if add == "Y":
         addon = input('We have [A]Face Mask | [B]Lanyard | [C]Mafla\nChoose your Add on (A/B/C): ')
         if addon == "A":
          add = "Face Mask [+RM10.00]\n"
          total +=  10.00

         elif addon == "B":
          add = "Lanyard [+10.00]\n"
          total += 10.00

         elif addon == "C":
          add = "Mafla [+10.00]\n"
          total += 10.00

         else:
          print( "WRONG ADD ONN!!!")
          break

        else:
         add = "No Add On\n"


        member = input('\nMembership (Y/N)?: ')
        if member == "Y":
            ahli = "Member [-30%]\n"
            tot = total - (total*0.3)


        elif member == "N":
            ahli = "Non-Member\n"
            tot = total

        else:
            ahli = "Non-Member\n"
            tot = total


        delivery = input('\nDeliver Option - [A]COD  [B]POSTAGE[+RM 5.00]: ')
        if delivery == "A":
           hantar = "COD\n"
           print("Total to Pay: RM " + str(tot))

        elif delivery == "B":
           hantar = "Postage [RM5.00]\n"
           tot += 5.00
           print("Total to Pay: RM " + str(tot))

        else:
           hantar = "Postage [RM5.00]\n"
           tot += 5.00
           print("Total to Pay: RM " + str(tot))

        
        print("\n\t\t\t*****RECEIPT*****\n")
        print("\t\t\tITEM: " + prod)
        print("\t\t\tSIZE: " + saiz)
        print("\t\t\tADD-ON: " + add)
        print("\t\t\tMEMBERSHIP: " + ahli)
        print("\t\t\tDELIVERY: " + hantar)
        print("\t\t\tTotal to Pay: RM " + str(tot) + "\n")
        print("\t\t\t*****THANK YOU*****\n")

    elif opt == 'X':
        print('YOUR ORDER HAS BEEN SUCCESFULLY RECORDED..\nTHANK YOU FOR YOUR ORDER :)')
        break

    else:
        print("WRONG INPUT, TRY AGAIN!!")
        socket.send(str.encode(keServer))
        Response = socket.recv(1024)
        print(Response.decode("utf-8"))

socket.close()
