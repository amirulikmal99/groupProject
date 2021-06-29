import socket
import signal
import sys

socket = socket.socket()
host = '192.168.56.103'
port = 8888

print('Waiting for connection')
try:
        socket.connect((host, port))
except socket.error as e:
        print(str(e))


Response = socket.recv(2048)
print(Response.decode("utf-8"))

print ( "\n=========================================================================================\n"
                        "\t\t\t* *** *** ***LIST *** **** *** *\t\t\t\n"
                        "=========================================================================================\n");

print("   ------------------------------------------------------------------------------------")
print("   | [A]  Kemeja" , end =" ")
print("                            [B]  Tshirt   |")
print("   | [C]  Jacket", end =" ")
print("       [D]  Hoodie        |")
print("   | [E]  Seluar Jeans", end =" ")
print("           [F]  Seluar Slack                    |")
print("   | [G]  Seluar Slack", end =" ")
print("            [H]  Topi     |")
print("   ------------------------------------------------------------------------------------")
print("=========================================================================================")



while True:
    opt = input('\nSelect Your Menu [Code Menu] Press "EXIT" if you are done..\n> ')
    if opt == "A" or opt == "B" or opt == "C" or opt == "D" or opt == "E" or opt == "F" or opt == "G" or opt == "H":
        qty = input("Quantity per Order: ")
        prc = '0.00'
        total = 0.00
        keServer = opt + ":" + qty + ":" + prc
        socket.send(str.encode(keServer))
        price = socket.recv(1024)
        price = float(price)

        size = input ('Choose Size: S/M/L/XL/2XL/3XL [XL-->3XL +RM10.00')
        if size == "S":
           print("Size: S\n")
           total = price
           print(str(total))
        elif size == "M":
           print("Size: M\n")
           total = price
           print(str(total))
        elif size == "L":
           print("Size: L\n")
           total = price
           print(str(total))
        elif size == "XL":
           print("Size: XL\n")
           total = price + 10.00
           print(str(total))
        elif size == "2XL":
           print("Size: 2XL\n")
           total = price + 10.00
           print(str(total))
        elif size == "3XL":
           print("Size: 3XL\n")
           total = price + 10.00
           print(str(total))
        else:
           print("WRONG INPUT SIZE!!!\n")
           break


        member = input('Membership (Y/N)?')
        if member == "Y":
            print("Member\n")
            tot = total - (total*0.3)
            print("Total Price (RM):" + str(tot))
        elif member == "N":
            print("Non-Member\n")
            tot = total
            print("Total Price (RM):" + str(tot))
        else:
            print("Non-Member\n")
            tot = total
            print("Total Price (RM):" + str(tot))

        delivery = input('Deliver Option: [A]COD [B]POSTAGE[+RM 5.00]')
        if delivery == "A":
           print("COD\n")
           sum = tot
           print("Total to Pay (RM):" + str(sum))
        elif delivery == "B":
           print("Postage\n")
           sum = tot + 5.00
           print("Total to Pay (RM):" + str(sum))
        else:
           print("Postage\n")
           sum = tot + 5.00
           print("Total to Pay (RM):" + str(sum))





    elif opt == 'EXIT':
        print('YOUR ORDER HAS BEEN SUCCESFULLY RECORDED..\nTHANK YOU FOR YOUR ORDER :)')
        break

    else:
        print("WRONG INPUT, TRY AGAIN!!")
        socket.send(str.encode(keServer))
        Response = socket.recv(1024)
        print(Response.decode("utf-8"))

socket.close()
