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
  print ("Take an umbrella")
elif weather == "snowing":
  print ("Wear gloves!")
elif weather == "sunny":
  print ("no need for a coat today!")
else:
  print ("wear a coat!")
  