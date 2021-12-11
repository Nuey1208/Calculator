def ShowName(n, s, a):
    print("Name : ", n)
    print("Surname : ", s)
    print("Amount to deposit: ", a)

def Saving_Account(amount):#print ออมทรัพย์ account
    print("Savings Deposit Account")
    print("Interest Rate : 0.25%")
    rate = float(amount * 0.0025)
    print("Amount of deposit :", amount, 'Baht')
    print("Net :", amount + rate , 'Baht')

def Fixed_Account(r):#print ประจำ account
    print("Fixed Deposit Account For", long, "month")
    print("Interest Rate :", str(r)+'%')
    rate = float(amount * (r/100))
    print("Amount of deposit :", amount , 'Baht')
    print("Net :", amount + rate , 'Baht')


name = input("Enter Name : ")
surname = input("Enter Surname : ")
amount = float(input("Amount to deposit : "))
long = int(input("Time require to deposit : "))
while long < 1:
    print("Invalid time require")
    long = int(input("Time require to deposit : "))


'''print both type of account'''

if long == 1:#fixed((2)scb bank, krungsri bank)
    print("SCB Bank")#SCBมีแบบ1เดือน
    Saving_Account(amount)
    Fixed_Account(0.25)#ประจำ


    print("K Bank")
    Saving_Account(amount)#K Bank มีแต่ออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")


    print("Krungsri Bank")#KrungSri มีประจำแบบ1เดือน
    Saving_Account(amount)
    Fixed_Account(0.1)


    print("BKK Bank")
    Saving_Account(amount)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")

if long == 3:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.32)#มีประจำ


    print("K Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.32)#มีประจำ
    

    print("Krungsri Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.32)#มีประจำ


    print("BKK Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.375)#มีประจำ

if long == 6:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ


    print("K Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ
    

    print("Krungsri Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ


    print("BKK Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.5)#มีประจำ

if long == 9:# fixed((3) scb, k bank, bkk bank)
    print("SCB Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ


    print("K Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ
    

    print("Krungsri Bank")
    Saving_Account(amount)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")


    print("BKK Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.45)#มีประจำ

if long == 12:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ


    print("K Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ
    

    print("Krungsri Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ


    print("BKK Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.50)#มีประจำ

if long == 24:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.45)#มีประจำ


    print("K Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.45)#มีประจำ
    

    print("Krungsri Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.45)#มีประจำ


    print("BKK Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.50)#มีประจำ

if long == 36:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.65)#มีประจำ


    print("K Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.65)#มีประจำ
    

    print("Krungsri Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.65)#มีประจำ


    print("BKK Bank")
    Saving_Account(amount)#มีออมทรัพย์
    Fixed_Account(0.75)#มีประจำ

else:
    print("SCB Bank")
    Saving_Account(amount)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")


    print("K Bank")
    Saving_Account(amount)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")
    

    print("Krungsri Bank")
    Saving_Account(amount)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")


    print("BKK Bank")
    Saving_Account(amount)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")
