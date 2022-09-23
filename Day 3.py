print("Welcome to the Roller Coster")
height =  int(input("Whats your Height in Cms? :  \n"))
if height>=120:
    print ("You can ride")
    age = int (input ("Enter your age : \n"))
    if age<=12:
        print("You have to pay 70 INR")
    elif age in range(12,18):
        print("You have to pay 120 INR")
    elif age>18:
        print("You have to pay 150 INR")
    
    
else:
    print("Sorry mate eat some Horlicks")