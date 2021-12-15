def ShowName(n, s, a):
    print("Name : ", n)
    print("Surname : ", s)
    print("Amount to deposit : ", a)

def Saving_Account(amount, long):#print ออมทรัพย์ account
    print("Savings Deposit Account")
    print("Interest Rate : 0.25% per year")
    print("Amount of deposit :", amount, 'Baht per month')
    if long/12 <= 1:
        rate = float((amount*long) * 0.0025 * (long*30)/360)
        print("Net :",(amount*long)+rate, "Bahts")
    elif 1 < long/12 <= 2:
        x = float(amount*12) + float((amount*12) * 0.0025)
        rate = float((x +(amount*(long-12))) * 0.0025 * ((long-12)*30)/360)
        print("Net :", x + amount*(long-12) + rate, "Bahts")
    elif 2 < long/12 <=3:
        x = float(amount*12) + float((amount*12) * 0.0025)
        y = x+(amount*12) + (float(x+(amount*12)) * 0.0025)
        rate = (y + amount(long-24))*(0.0025)*(long-24)/360
        print("Net :", y + amount*(long-24) + rate , 'Baht')

def Fixed_Account(r):#print ประจำ account
    print("Fixed Deposit Account For", long, "month")
    print("Interest Rate :", str(r)+'%',"per year")
    rate = float((amount*long) * (r/100))
    print("Amount of deposit :", amount , 'Baht per month')
    print("Net :", (amount*long) + rate , 'Baht')
    


name = input("Enter Name : ")
surname = input("Enter Surname : ")
amount = float(input("Amount of money to deposit per month : ")) #จะเก็บเดือนละเท่าไหร่
while amount < 1:
    print("Invalid Amount to deposit require")
    amount = float(input("Amount of money to deposit per month : "))

long = int(input("Months require to deposit(1-36) : "))
while long < 1:
    print("Invalid time require")
    long = int(input("Months require to deposit : "))


'''print both type of account'''
if long == 1:#fixed((2)scb bank, krungsri bank)
    print("SCB Bank")#SCBมีแบบ1เดือน
    Saving_Account(amount, long)
    Fixed_Account(0.25)#ประจำ

    print("K Bank")
    Saving_Account(amount, long)#K Bank มีแต่ออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")

    print("Krungsri Bank")#KrungSri มีประจำแบบ1เดือน
    Saving_Account(amount, long)
    Fixed_Account(0.1)

    print("BKK Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")

elif long == 3:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.32)#มีประจำ

    print("K Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.32)#มีประจำ    

    print("Krungsri Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.32)#มีประจำ

    print("BKK Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.375)#มีประจำ

elif long == 6:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ

    print("K Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ
    
    print("Krungsri Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ

    print("BKK Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.5)#มีประจำ

elif long == 9:# fixed((3) scb, k bank, bkk bank)
    print("SCB Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ

    print("K Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ

    print("Krungsri Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")

    print("BKK Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.45)#มีประจำ

elif long == 12:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ

    print("K Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ
    
    print("Krungsri Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.40)#มีประจำ

    print("BKK Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.50)#มีประจำ

elif long == 24:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.45)#มีประจำ

    print("K Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.45)#มีประจำ

    print("Krungsri Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.45)#มีประจำ

    print("BKK Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.50)#มีประจำ

elif long == 36:# fixed(all)
    print("SCB Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.65)#มีประจำ

    print("K Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.65)#มีประจำ

    print("Krungsri Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.65)#มีประจำ

    print("BKK Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    Fixed_Account(0.75)#มีประจำ

else:
    print("SCB Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")

    print("K Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")
    
    print("Krungsri Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")

    print("BKK Bank")
    Saving_Account(amount, long)#มีออมทรัพย์
    print("Fixed Deposit Account")#ไม่มีประจำ
    print("No interest rate for",long, "month with Fixed Deposit Account")
