
import random
import math

digits = [i for i in range(0, 20)]
random_no = ""

for i in range(10):
    index = math.floor(random.random() * 10)
    random_no += str(digits[index])
############################################
print("SlackUsername - BlackAdam")
print("Welcome")
###################

print("1. login")
print("2. close the app")
User = int(input("Enter your choice please:"))
if User == 1:
    while True:
        Staff_Username = input(str("Enter Username:"))
        Staff_Password = input("Enter Password:")
        Staff_database = open("staff.txt", "r")
        for line in Staff_database:
            details = line.split(",")
            username = str(details[0])
            password = str(details[1])
            if Staff_Username != username and Staff_Password != password:
                print("Incorrect Username or Password")
                continue
        else:
            print("Login Successfully")
            break

    print("1. Create New Bank Account")
    print("2. Check Account Details")
    print("3. Logout")
    User = int(input("Enter your choice please:"))
    if User == 1:
        Account_Name = input("Enter Account Name:")
        Opening_Balance = float(input("Enter Opening Balance:"))
        print("1. Savings")
        print("2. Current")
        Account_Type = input("Enter your choice please:")
        Account_Email = input("Enter email:")
        Account_Number = random_no
        #######################

        Customer_database = open("customer.txt", "w+")
        Customer_database.write("Account Name: %s \n" % Account_Name)
        Customer_database.write("Opening Balance: %s \n" % Opening_Balance)
        Customer_database.write("Account Type: %s \n" % Account_Type)
        Customer_database.write("Account Email: %s \n" % Account_Email)
        Customer_database.write("Account Number: %s \n" % Account_Number)
        print("Account Created Successfully")

    elif User == 2:
        while True:
            Account_Num = input("Enter account number: ")
            file = open("customer.txt")
            for line in file:
                field = line.split(",")
                accNumber = field[4]

                if Account_Num == accNumber:
                    print(line)
                    file.close()
                    break
            else:
                print("incorrect account number")
                continue
    else:
        print("logout successfully")

else:
    print("Thank You")