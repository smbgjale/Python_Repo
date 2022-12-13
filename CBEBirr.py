from datetime import date
import sys

print("\n\nWelcome to mobile Banking.Press * to navigate back any time , select one of the following options bello: \n")
print("1: Login")
print("2 : Exit")
user = int(input())  #it take from input
if user== 2:
    sys.exit("If wann to enter run again")
def passwo():
    i = user #i is 1
    while i < 20: #PIN is 4692
        restart = (input("please enter your PIN to Login: "))
        if restart != "4692":
            print("Incorect PIN ", i)
            i += 1
        if restart == "4692":
            break
if user == 1:
    passwo()
    print("\nWelcome to  Mobile banking \n1: My Accounts \n2: Transfer to another Account \n3: Airtime\n")
user2 = int(input()) #it take input from keybord
if user2 == 1:
    user3 = int(input("\n\nMy Accounts \n1: Educati - ETB-7453 \n"))
    if user3 == 1:
         print("\n\nSAMUEL MENGISTU BAYESSA.\nAvailable balance is ETB 13,489.62\n Transactions \n1:- 08/12 200.00 \n2:- 05/12 530.00 \n3:- More options")
    else:
        print("if you wann Run agine please")
if user2 == 2:
    user4 = int(input("\nTransfer to CBE Account\n1: Educati - ETB-7453 \n\n"))
    if user4 == 1:
        acc_no = int(input("Refile\nPlease enter Account No\n\n"))
        amount = int(input("\nEducati - ETB-7453\nRequest Tranfer from - ETB-7453\n\nPlease enter Amount \n "))
        conf = int(input("\nConfirm request foor - ETB-7453\nRequest Transfer from - ETB-7453\nTransfer To :%d\nAmount: %d \nplease Confirm\n1: Yes\n2: No\n \n" % (acc_no, amount)))
        if conf == 1:
            today = date.today()
            print("\nComplete\n\nETB %d debited from SAMUEL MENGISTU BEYESSA-ETB-7453 for Topup %d  " % (amount, acc_no))
            print("on : " , today)
        else:
            print("if you wann Run agine please")
if user2 == 3:
    user5 =int(input("\nBuy Airtime\n1:Educati-ETB-7453\n"))
    if user5 == 1:
        mob_no = int(input("Educati-ETB-7453\nRequest Transfer from Educati-ETB-7453\nPlease enter Recharged Mob No\n\n"))
        mob_amo = int(input("Educati-ETB-7453\nRequest Transfer from Educati-ETB-7453 \n\nPlease enter Amount\n\n"))
        conf1 = int(input("\nConfirm request foor - ETB-7453\nRequest Transfer from - ETB-7453\nRecharged Mob No: %d\nAmount: %d \nplease Confirm\n\n1: Yes\n2: No\n " % (mob_no, mob_amo)))
        if conf1 == 1:
            today = date.today()
            print("\nComplete\n\nETB %d debited from SAMUEL MENGISTU BEYESSA-ETB-7453 for Topup %d  " % (mob_amo, mob_no))
            print("on: " , today)
        else:
            print("if you wann Run agine please")

elif user2 == '*':
    print("if you wann Run agine please")
else:
   # exit(user)
    print("if you wann Run agine please")
    

    
    