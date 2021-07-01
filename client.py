import socket
import signal
import sys

socket = socket.socket()
host = '192.168.114.6'
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
print("                   [H]  Topi              |")
print("   --------------------------------------------------------------------------")
print("============================================================================")



while True:
    opt = input('\nSelect Your Option [Code Bundle] Press "X" if you are done..\n> ')
    if opt == "A" or opt == "B" or opt == "C" or opt == "D" or opt == "E" or opt == "F" or opt == "G" or opt == "H":
        qty = input("\nQuantity per Order: ")
        prc = '0.00'
        total = 0.00
        keServer = opt + ":" + qty + ":" + prc
        socket.send(str.encode(keServer))
        price = socket.recv(1024)
        price = float(price)

        size = input ('\nWe have S/M/L/XL/2XL/3XL size. If size XL-->3XL, add RM10.00 \nChoose your size: ')
        if size == "S":
           print("Size: S\n")
           total = price

        elif size == "M":
           print("Size: M\n")
           total = price

        elif size == "L":
           print("Size: L\n")
           total = price

        elif size == "XL":
           print("Size: XL\n")
           total = price + 10.00

        elif size == "2XL":
           print("Size: 2XL\n")
           total = price + 10.00

        elif size == "3XL":
           print("Size: 3XL\n")
           total = price + 10.00


        else:
           print("WRONG INPUT SIZE!!!\n")
           break

        add = input('\nAdd Onn (Y/N): ')
        if add == "Y":
         addon = input('We have [A]Face Mask | [B]Lanyard | [C]Mafla\nChoose your Add on (A/B/C): ')
         if addon == "A":
          print("Face Mask[+RM15.00]\n")
          total +=  15.00

         elif addon == "B":
          print("Lanyard[+RM10.00]\n")
          total += 10.00

         elif addon == "C":
          print("Mafla[+RM20.00]\n")
          total += 20.00

         else:
          print("WRONG ADD ONN!!!")
          break

        else:
         print("No Add On\n")


        member = input('\nMembership (Y/N)?: ')
        if member == "Y":
            print("Member\n")
            tot = total - (total*0.3)


        elif member == "N":
            print("Non-Member\n")
            tot = total

        else:
            print("Non-Member\n")
            tot = total


        delivery = input('\nDeliver Option - [A]COD [B]POSTAGE[+RM 5.00]: ')
        if delivery == "A":
           print("COD\n")
           sum = tot
           print("Total to Pay: RM " + str(sum))

        elif delivery == "B":
           print("Postage\n")
           sum = tot + 5.00
           print("Total to Pay: RM " + str(sum))

        else:
           print("Postage\n")
           sum = tot + 5.00
           print("Total to Pay: RM " + str(sum))


    elif opt == 'X':
        print('YOUR ORDER HAS BEEN SUCCESFULLY RECORDED..\nTHANK YOU FOR YOUR ORDER :)')
        break

    else:
        print("WRONG INPUT, TRY AGAIN!!")
        socket.send(str.encode(keServer))
        Response = socket.recv(1024)
        print(Response.decode("utf-8"))

socket.close()
