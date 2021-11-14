def ShowName(n, s, a):
    print("Name : ", n)
    print("Surname : ", s)
    print("Amount to deposit: ", a)

def Saving(amount):#ออมทรัพย์
    print("Savings Deposit Account")
    print("Interest Rate : 0.25%")
    rate = float(amount * 0.0025)
    print("Amount of deposit :", amount)
    print("Net :", amount + rate)

name = input("Enter Name : ")
surname = input("Enter Surname : ")
amount = float(input("Amount to deposit : "))
long = int(input("Time require to deposit : "))
while long < 1:
    print("Invalid time require")
    long = int(input("Time require to deposit : "))

if long == 1:#คำนวนออมทรัพย์ทุกอันและประจำของscb+krungsri
    print("SCB Bank")
    Saving(amount) #ประจำ
    print("Fixed Deposit Account")
    print("Interest Rate : 0.25%")
    rate = float(amount * 0.0025)
    print("Amount of deposit :", amount)
    print("Net :", amount + rate)


    print("K Bank")
    Saving(amount)
    print("Fixed Deposit Account")
    print("No interest rate for 1 month with Fixed Deposit Account")


    print("Krungsri Bank")
    Saving(amount)#ประจำ
    print("Fixed Deposit Account")
    print("Interest Rate : 0.1%")
    rate = float(amount * 0.001)
    print("Amount of deposit :", amount)
    print("Net :", amount + rate)


    print("BKK Bank")
    Saving(amount)
    print("Fixed Deposit Account")
    print("No interest rate for 1 month with Fixed Deposit Account")
