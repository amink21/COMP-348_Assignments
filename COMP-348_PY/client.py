#
# COMP-348: Assignment 2
# Amin Kadawala - 40200998
# 2022-11-18
#

import socket

#Main client function where the client connects to the server being ran
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 9999  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    flag = 1
    while(flag == 1): #keeps running till user presses 8

        #Outputs the menu
        print("\nPython DB Menu\n\n1. Find customer\n2. Add customer\n3. Delete customer\n4. Update customer age\n5. Update customer address\n6. Update customer phone\n7. Print report\n8. Exit\n")
        userInput = int(input("Select: "))

        #if user selects 1 - findCustomer
        if userInput == 1:
            findName = input("Enter customer name: ")
            message = str(1)
            message += "," + findName

        #if user selects 2 - addCustomer
        elif userInput == 2:
            name = input("Enter customer name: ")
            while (name ==""):
                name = input("Name can not be empty! Enter customer name: ")

            age = input("Enter the age of the customer: ")
            if(age != ""):
                age = input("Age has to be a number. Enter the age of the customer: ")
            address = input("Enter the address of the customer: ")
            phone = input("Enter the phone number of the customer: ")
            message = str(2) + "," + name + "," + age + "," + address + "," + phone

        #if user selects 3 - deletesCustomer
        elif userInput == 3:
            name = input("Enter customer name: ")
            message = str(3) + "," + name

        #if user selects 4 - updates customers age
        elif userInput == 4:
            name = input("Enter customer name: ")
            update = input("Enter the age of the customer: ")
            if(update != ""):
                while (not update.isdigit()):
                    update = input("Age has to be a number. Enter the age of the customer: ")
            message = str(4) + "," + name + "," + update

        #if user selects 5 - updates customers address
        elif userInput == 5:
            name = input("Enter customer name: ")
            update=input("Enter the address of the customer: ")
            message = str(5) + "," + name + "," + " " + "," + update + "," + " "

        #if user selects 6 - updates customers phone number
        elif userInput == 6:
            name = input("Enter customer name: ")
            update = input("Enter the phone number of the customer: ")
            message = str(6) + "," + name + "," + " " + "," + " " + "," + update

        #if user selects 7 - prints out a report of all customers in database
        elif userInput == 7:
            message=str(7)

        #if user selects 1 - terminates the program with message
        elif userInput == 8:
            message=str(8)
            flag = 0

        #message = input(" -> ")  # again take input
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Server response: ' + data)  # show in terminal
    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()