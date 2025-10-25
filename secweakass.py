#1
number=int(input("enter your number"))
if number % 2== 0:
    print(" the number is even ")
else:
    print("the number is odd")
#2
if number<0:
    print(" the number is negative")
elif number == 0:
    print("the number is zero")
else:
    print("the number is positive")    
3
password="Strangers things"
guesspassword= input("enter the password")
if password == guesspassword:
    print("Access Granted")
else:
    print("Access Denied")
#4
firstnumber=int(input(" enter your first number "))
secnumber=int(input("enter your secound number"))
oper=input("input your operator")
if oper== "+":
  print(firstnumber + secnumber)
elif oper== "-":
  print(firstnumber - secnumber)
elif oper== "%":
  print(firstnumber % secnumber) 
elif oper== "*":
  print(firstnumber * secnumber) 
elif oper== "/":
  print(firstnumber / secnumber)
#5
age = int(input("enter your age"))
if age<13:
    print("child")
elif age<=19:
    print("teenager")
elif age<=59:
    print("adult")
else:
    print("senior")    
#8
username = input(" ENTER YOUR CARD. \n ")
pin = input(" PLEASE ENTER YOUR PIN. \n")
acctyp = input(" \n  SELECT YOUR ACCOUNT  : \n 1. CURRENT ACCOUNT : \n 2. SAVINGS ACCOUNT \n : ")
amount = str(input("  PLEASE ENTER YOUR AMOUNT \n : "))
recipt = input("\n  DO  YOU WANT RECIPT : \n 1: YES : \n 2: NO: \n ")
print(amount)
print(" HEAR IS YOUR AMOUNT. ")
print(" THANK YOU FOR YOUR VISIT ." ) 
#7
count = 1
username= "ayan@123"
passs=12345
while count <= 3 :
    usname=input("enter your username")
    passs = input("enter your passs ")
    if passs and usname == username :
        print(" welcome ")
        break
    count+=1
else:
    print(" accountlockes ")    
#9
no=int(input("enter a number"))
count=1
while count<=10:
    print(no*count)
    count+=1

