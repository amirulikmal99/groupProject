import socket
import signal
import sys

socket = socket.socket()
host = '192.168.56.104'
port = 8888

print('Waiting for connection...')

try:
        socket.connect((host, port))

except socket.error as e:
        print(str(e))

try:
        file = open(r'bundle.txt', 'r')

except :
        file = open(r'bundle.txt', 'w')
        file.write('Sales Record \n')
        file.close()
        file = open(r'bundle.txt', 'r')

file = open(r'bundle.txt', 'a')


Response = socket.recv(2048)
print(Response.decode("utf-8"))



print ( "\n============================================================================\n"
               "      * *** *** ***WELCOME TO AIM'S BUNDLE ONLINE SHOP *** **** *** *\t\t\t\n"
                        "============================================================================\n");

print("   --------------------------------------------------------------------------")
print("    | [A]  Kemeja - RM 40" , end =" ")
print("                     [B]  Tshirt - RM 30          |")
print("    | [C]  Jacket - RM 90", end =" ")
print("                     [D]  Hoodie - RM 70          |")
print("    | [E]  Seluar Jeans - RM 45", end =" ")
print("               [F]  Seluar Slack - RM 45    |")
print("    | [G]  Seluar Track - RM 25", end =" ")
print("                                       ")
print("   --------------------------------------------------------------------------")
print("============================================================================")



while True:
    opt = input('\nSelect Your Option [Code Bundle] Press "X" if you are done..\n> ')
    if opt == "A" or opt == "a" or opt == "B" or opt == "b" or opt == "C" or opt == "c" or opt == "D" or opt == "d" or opt == "E" or opt == "e" or opt == "F" or opt == "f" or opt == "G" or opt == "g":
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
           name = input('\nEnter your name: ')
           address = input('\nEnter your home address: ')
           print("Total to Pay: RM " + str(tot))

        elif delivery == "B":
           hantar = "Postage [RM5.00]\n"
           tot += 5.00
           name = input('\nEnter your name: ')
           address = input('\nEnter your home address: ')
           print("Total to Pay: RM " + str(tot))
           print("\nOur Account Number: AIM Bundle - 1234567891011 (Bank Islam) \nPlease send the transaction receipt to us after transfer the money \nThank You ^^")

        else:
           hantar = "Postage [RM5.00]\n"
           tot += 5.00
           name = input('\nEnter your name: ')
           address = input('\nEnter your home address: ')
           print("Total to Pay: RM " + str(tot))
           print("\nOur Account Number: AIM Bundle - 1234567891011 (Bank Islam) \nPlease send the transaction receipt to us after transfer the money \nThank You ^^")


        print("\nThis is your receipt. Please save it\n")
        print("\n\t\t\t*********RECEIPT*********\n")
        print("\t\t\t AIMS'S ONLINE BUNDLE")
        print("\t\t\tNAME: " + name)
        print("\t\t\tHOME ADDRESS: " + address)
        print("\n\t\t\tITEM: " + prod)
        print("\t\t\tSIZE: " + saiz)
        print("\t\t\tADD-ON: " + add)
        print("\t\t\tMEMBERSHIP: " + ahli)
        print("\t\t\tDELIVERY: " + hantar)
        print("\t\t\tTotal to Pay: RM " + str(tot) + "\n")
        print("\t\t\tOur Account Number: AIM Bundle - 1234567891011 (Bank Islam) \n\t\t\tPlease send the transaction receipt to us after transfer the money")
        print("\n\t\t\t*********THANK YOU*********\n")

    elif opt == 'X':
        print('YOUR ORDER HAS BEEN SUCCESFULLY RECORDED..\nTHANK YOU FOR YOUR ORDER :)')
        break

    else:
        print("WRONG INPUT, TRY AGAIN!!")
        break

write = '\n' + name + '| ' + str(prod) + '| ' + str(saiz) + '| ' + str(add) + '|' +  str(ahli) + '| ' + str(hantar) + '| ' + str(address) + '| ' + str(total) + '\n'
file.write(write)
file.close

socket.close()
