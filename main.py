#Python Tasks
#27.09.2022


salary = 15 
print (salary)
salary = salary + 50
print (salary)
salary = salary + salary
print (salary)
salary = salary * salary
print (salary)

#Two variables: Price and Stock 
price = 10
stock = 5

print (price)
print (stock)
print (price + stock)
print (price)
#only use speech marks when you want to print out some text, no speech marks if you want the answer to something 

#Assigning a Variable
ProductName ="iPhone"
ProductPrice = 450

print(ProductName)
print(ProductPrice)
print (ProductName, ProductPrice)
print("Your",ProductName, "costs £",ProductPrice)

#User input: City 
name = input("What is your name?")
print("Hello" + name)

city = input("What city do you live in?")
age = int(input("What is your age?"))
print("Hello",name, "you will be", age +1, "next year")
#This code does not work - error message. Define Variable as an integar 
#correct code below: age = int(input("What is your age?"))

#User input 2: Phone 
ProductName = input ("What is your phone?")
ProductPrice = int(input ("What is your phone worth?"))
print ("Your", ProductName, "will be worth £", ProductPrice -100, "next year")

#User input 3: Weather 
weather = input ("What is the weather like? ")
if weather == "raining":
  print ("Take an umbrella!")
elif weather == "snowing":
  print ("Wear gloves!")
elif weather == "sunny":
  print ("No need for a coat today!")
else:
  print ("Wear a coat!")
#double equals sign (==) means the same as 

#Guess my number!
import random #imports the random library 
myname=input("Please enter your name?:")
number=random.randint (1,5) #generates number between 1 and 5
print ("Well ",myname, "I am thinking of a number between 1 and 5")
guess= int(input("Take a guess :")) 
if guess == number:
  print ("Well done, ",myname,"You guessed my number")
else:
  print ("Incorrect, better luck next time!")
