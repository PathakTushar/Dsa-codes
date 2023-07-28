# print("day1-string concatenation")
# print("String concatenation is done with '+' sign")
# print('e.g. print("hello" + "world")')


# print(len(input("what is your name? ")))

# a=input("a: ")
# b=input("b: ")
# c=a
# a=b
# b=c
# print("a = "+a)
# print("b = "+b)


# two_digit=input("enter the two digit number : ")
# first=two_digit[0]
# second=two_digit[1]
# result=int(first)+int(second)
# print(result)


# height = input("enter the height : ")
# weight = input("enter the weight : ")
# bmi=round(float(weight)/float(height) ** 2)
# print(int(bmi))
# message=f"your bmi is {bmi}, you are "
# if bmi<18.5:
#     print(message+"underweight")
# elif bmi<25:
#     print(message+"normal weight")
# elif bmi<30:
#     print(message+"overweight")
# elif bmi<35:
#     print(message+"slightly obese")
# else:
#     print(message+"clinically obese")




# age=int(input("what is your age? "))
# yearsLeft=90-age
# monnthsLeft=12*yearsLeft
# daysLeft=365*yearsLeft
# message=f"you have {daysLeft} days, {monnthsLeft} months and {yearsLeft} years left"
# print(message)


# num=int(input("enter the number : "))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")



# year=int(input("enter the year : "))
# rem4=year%4
# rem100=year%100
# rem400=year%400
# if rem4==0:
#     if rem100==0:
#         if rem400==0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")  
# else:
#     print("not leap year")


# print("welcome to python pizza deliveries")
# size=input("what size pizza do you want? S, M, L : ")
# add_pepperoni=input("do you want pepperoni? Y or N : ")
# extra_cheese=input("do you want extra cheese? Y or N : ")
# price=0
# if size=='S':
#     price+=15
# elif size=='M':
#     price+=20
# elif size=='L':
#     price+=25
# else:
#     print("enter the correct size")

# if add_pepperoni=='Y':
#     if size=='S':
#         price+=2
#     else:
#         price+=3;
# if extra_cheese=='Y':
#     price+=1;

# print(f"your final bill is ${price}")


# name1=input("enter your name : ")
# name2=input("enter their name : ")

# finalName=name1.lower()+name2.lower()

# t=finalName.count("t")
# r=finalName.count("r")
# u=finalName.count("u")
# e=finalName.count("e")

# true=t+r+u+e

# l=finalName.count("l")
# o=finalName.count("o")
# v=finalName.count("v")
# e=finalName.count("e")

# love=l+o+v+e

# score=str(true)+str(love)
# print(f"your love score is {score}") 



# import random
# random_side=random.randint(0,1)
# if random_side==1:
#     print("heads")
# else:
#     print("tails")


# import random
# names=input("enter the set of names separated by a comma : ")
# names_list=names.split(",")
# random_choice=random.randint(0,len(names_list)-1)
# print(f"{names_list[random_choice]} is going to buy the meal today")
# print(f"{random.choice(names_list)} is going to buy the meal today")


# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# row_pos=int(position[1])
# column_pos=int(position[0])
# map[row_pos-1][column_pos-1]="X"
# print(f"{row1}\n{row2}\n{row3}")
# print(map)



# import random
# list=["rock","paper","scissors"]
# print("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.")
# users_choice=int(input())
# users_select=list[users_choice]
# computer_choice=random.randint(0,2)
# computer_select=list[computer_choice]

# if (users_choice==0 and computer_choice==2)or(users_choice==1 and computer_choice==0)or(users_choice==2 and computer_choice==1):
#     res="win"
# else:
#     res="lose"

# print(f"you chose {users_select} and computer chose {computer_select}, so you {res}")




# student_height=input("input a list of student heights: ").split()
# print(student_height)
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n])
# sum1=sum(student_height)
# len1=len(student_height)
# avg1=sum1/len1
# print(student_height)
# print(f"average of the heights = {avg1}")
# sum2=0
# num=0
# for i in student_height:
#     sum2+=i
#     num+=1

# avg2=round(sum2/num)
# print(f"average of the heights = {avg2}")



# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# passwordList=[]
# for i in range (0,nr_letters):
#     passwordList+=random.choice(letters)
# for i in range (0,nr_numbers):
#     passwordList+=random.choice(numbers)
# for i in range (0,nr_symbols):
#     passwordList+=random.choice(symbols)

# random.shuffle(passwordList)
# password=""
# for char in passwordList:
#     password+=char
# print(password)


# def prime_checker(number):
#     count = 0
#     for i in range(1,number+1):
#         if number%i==0:
#             count+=1
#     if count==2:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")


# n=int(input("check this number: "))
# prime_checker(number=n)



# def encryption(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         pos=alphabet.index(letter)
#         new_pos=(pos+shift_amount)%len(alphabet)
#         cipher_text+=alphabet[new_pos]
#     print(f"The encoded text is {cipher_text}")

# def decryption(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         pos=alphabet.index(letter)
#         new_pos=(len(alphabet)+pos-shift_amount)%len(alphabet)
#         cipher_text+=alphabet[new_pos]
#     print(f"The decoded text is {cipher_text}")

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# while(True):
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     if(direction=="encode"):
#         encryption(plain_text=text,shift_amount=shift)
#     elif(direction=="decode"):
#         decryption(plain_text=text,shift_amount=shift)
#     else:
#         print("invalid choice")
#     print("Type 'yes' if you want to go again. Otherwise type 'no'.")
#     choice=input().lower()
#     if(choice=="no"):
#         break;



# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades={}
# print(student_scores)
# for student in student_scores:
#     print(student)
#     print(student_scores[student])
#     if(student_scores[student]>90):
#         student_grades[student]="outstanding"
#     elif(student_scores[student]>80):
#         student_grades[student]="very good"
#     elif(student_scores[student]>70):
#         student_grades[student]="good"
#     else:
#         student_grades[student]="average"
    
# print(student_grades)



# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country,visitNum,cities):
#     new_country={}
#     new_country["country"]=country
#     new_country["visits"]=visitNum
#     new_country["cities"]=cities
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# import os
# def cls():
#     os.system('cls' if os.name=='nt' else 'clear')
# print("welcome to secret bidding")
# bidders={}
# while(True):
#     name=input("what is your name? ")
#     bidAmount=int(input("enter the bid amount. "))
#     bidders[name]=bidAmount
#     ch=input("Are there anymore bidders? Type yes or no : ").lower()
#     if(ch=="no"):
#         break
#     cls()
# cls()

# max=0;
# for bid in bidders:
#     if bidders[bid]>max:
#         max=bidders[bid]
#         person=bid

# print(f"The highest bid was from {person} that is a total amount of rs {max}")



# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         print("Leap year.")
#         return True
#       else:
#         print("Not leap year.")
#         return False
#     else:
#       print("Leap year.")
#       return True
#   else:
#     print("Not leap year.")
#     return False

# def days_in_month(year,month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month==2:
#         if is_leap(year):
#             month_days[month-1]=29
#     return month_days[month-1]
  
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# from functools import reduce


# a="1 2 3 4"
# list_ele=list(a.split())
# print(list_ele)
# x= map(int, a.split())
# temp=list(x)
# print(temp)


# z=filter(lambda x:x>2, temp)
# print(list(z))

# b=reduce(lambda num1,num2:num1+num2, temp)
# print(b)


# import math
# x=float(input("value of x: "))
# eq=x-(math.cos(x)-x*x-x)/(-math.sin(x)-2*x-1)
# print(eq)

# k=0.2
# res1=k*(0.6363+0.7032)/2
# res2=k*k*0.0669/2
# res3=k*(k*k-1)*(0.0063+0.0070)/12
# res4=k*k*(k*k-1)*0.0007/24
# res5=k*(k*k-1)*(k*k-4)*0.0001/240
# ans=6.6859+res1+res2+res3+res4+res5
# print(res1)
# print(res2)
# print(res3)
# print(res4)
# print(res5)
# print(ans)