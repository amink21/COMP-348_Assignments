#
# COMP-348: Assignment 2
# Amin Kadawala - 40200998
# 2022-11-18
#

import socket

data = ""
database = {}

#Main server function, where connection is started and creates tuples for each line in the txt file
def server_program():
    #get the hostname
    host = socket.gethostname()
    port = 9999  #initiate port no above 1024

    server_socket = socket.socket()  #get instance
    #look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  #bind host address and port together

    #configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  #accept new connection
    print("Connection from: " + str(address))
    while True:
        #receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            #if data is not received break
            break
        else:
            dataTuple = data.split(",")

        #Creates tuples for each
        i = 0
        for item in dataTuple:
            if i == 0:
                methodID = int(item)
                i+=1
            elif i == 1:
                uName = item
                i+=1
            elif i == 2:
                uAge = item
                i+=1 
            elif i == 3:
                uAddress = item
                i+=1
            elif i == 4:
                uPhone = item
                i+=1

        #User inputs each of the numbers, message for the client is sent
        if methodID == 1:
            msgForClient = findCustomer(uName)

        elif methodID == 2:
            msgForClient = addCustomer(uName,uAge,uAddress,uPhone)

        elif methodID == 3:
            msgForClient = deleteCustomer(uName)

        elif methodID == 4:
            msgForClient = updateCustomerAge(uName,uAge)

        elif methodID == 5:
            msgForClient = updateCustomerAddress(uName,uAddress)

        elif methodID == 6:
            msgForClient = updateCustomerPhone(uName,uPhone)

        elif methodID == 7:
            msgForClient = printReport()

        elif methodID == 8:
            msgForClient = closeServer()

        data = msgForClient #input(' -> ')
        conn.send(data.encode())  #send data to the client

    conn.close()  #close the connection


#Function to load the data.txt file, splitting the information into values 
def loadData():
    file = open("C:\\Users\\Amin\\OneDrive\\Documents\\COMP-348_PY\\data.txt","r")
    lines = file.readlines()
    file.close()
    for line in lines:
        temp = line.split("|")
        i = 0
        value = []#(age,address,phone) a list
        for item in temp:
            if i == 0:
                key = item
                i+=1
            elif i == 1:
                value.append(item) #adding age
                i+=1
            elif i == 2:
                value.append(item) #address
                i+=1
            elif i == 3:
                item = item.replace("\n","") #removing \n
                value.append(item) #phone
                i+=1

        database[key]=value

#Find customer function where takes in a name and outputs the info for the customer 
def findCustomer(findName):
    if findName not in database:
        return findName + " not found in database."
    else:
        temp = database.get(findName)
        report = str(findName)
        for item in temp:
            if item != "":
                report = report + "|" + item
            else:
                report = report + "|  " + item
    return report

#Adds a customer to the database, takes in name, age, address, and phone number 
def addCustomer(name,age,address,phone):
    if name not in database:
        value = []
        value.append(age)
        value.append(address)
        value.append(phone)
        database[name] = value
        return name + "|" + age + "|" + address + "|" + phone + " has been added successfully."
    else:
        return "Customer already exists."

#Deletes a existing customer
def deleteCustomer(name):
    if name not in database:
        return "Customer does not exist"
    else:
        del database[name]
        return name + " has been deleted successfully."

#Updates a customers age, taking in the name and an updated age 
def updateCustomerAge(name,update):
    if name not in database:
        return "Customer not found."
    else:
        userDetails = database.get(name)
        i = 0
        value = []
        for item in userDetails:
            if i == 0:
                value.append(update) #updating age
                i+=1
            elif i == 1:
                value.append(item) #address remain same
                i+=1
            elif i == 2:
                value.append(item) #phone remain same
                i+=1
        database[name]=value
        return "Customer " + name + " has been updated with age: " + update + " successfully."

#Updates a customers address, taking in the name and an updated address 
def updateCustomerAddress(name,update):
    if name not in database:
        return "Customer does not exist"
    else:
        userDetails=database.get(name)
        i = 0
        value=[]
        for item in userDetails:
            if i == 0:
                value.append(item) # age remain same
                i+=1
            elif i == 1:
                value.append(update) #updating address
                i+=1
            elif i == 2:
                value.append(item) #phone remain same
                i+=1
        database[name]=value
        return "Customer " + name + " has been updated with address: " + update + " successfully."

#Updates a customers phone number, taking in the name and an updated phone number 
def updateCustomerPhone(name,update):
    if name not in database:
        return "Customer does not exist"
    else:
        userDetails=database.get(name)
        i = 0
        value = []
        for item in userDetails:
            if i == 0:
                value.append(item) #age remain same
                i+=1
            elif i == 1:
                value.append(item) #address remain same
                i+=1
            elif i == 2:
                value.append(update) #updating phone
                i+=1
        database[name]=value
        return "Customer " + name + " has been updated with phone number: " + update + " successfully."

#Prints a report of all the customers in the database
def printReport():
    report = ""
    subReport = ""
    for i in sorted(database.keys()):
        temp = database.get(i)
        subReport = str(i)
        for item in temp:
            if item != "":
                subReport = subReport + "|" + item
            else:
                subReport = subReport + "|  " + item
        subReport = subReport + "\n"
        report = report + subReport
    return "\n** Python DB contents **\n" + report

#Closes the server with a goodbye message
def closeServer():
    return "Good bye, server closed."

loadData()

if __name__ == '__main__':
    server_program()