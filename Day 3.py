# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
  
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
  
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")
  
  
#   LOve Calculator thingy
# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1 = name1.lower()
name2=name2.lower()

# true-> count love-> count
str1 = "true"
str2 = "love"
str1count=0
str2count=0
for i in name1 or name2:
    if i in str1:
        # print(f"I am found at {i}")
        str1count = str1count+1
print (str1count)

for i in name1 and name2:
    if i in str2:
        str2count =str2count+1
    
print(str2count)


score=str1count+str2count
cheetos = str(str1count)+str(str2count)
if score>90 or score<10:
    print(f"Your score is {cheetos}, you go together like coke and mentos.")
elif score <50 and score>40:
    print(f"Your score is {cheetos}, you are alright together.")
else:
    print(f"Score: {cheetos}")
    