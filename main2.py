# muitiple lines print
Name="Gauri"
Friend="aarti"
print("hello," +Name)
convo='''hey,miss
what is your name
my name is gauri'''
print(convo)
print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])
print(Name[4])
# print(Name[5]) throws an error
print("Lets use a for loop\n")
for character in convo:
    print(character)

sister="seema"
seemalen=len(sister)
print(seemalen) # here 0=s,1=e, 2=e, 3=m, 4=a
print(sister[0:4])#including 0 but not 4
print(sister[0:5])
print(sister[0:3]) #[0 to 5 is length(letters) of word]
print(sister[1:3])
print(sister[-1:3])
print(sister[-4:-3]) #-4 means length of letter(5)-4=1
# strips are immutable

a="arti"
print(a)
print(a.upper())
b="gauri !!!!!! gauri"
print(b.lower())
print(b.rstrip("!"))
print(b.replace("gauri", "jitin"))
print(b.split(" "))

blogheading="introduction of python"
print(blogheading.capitalize())

nextstr="I Am Runing Python!!"
print(len(nextstr))
print(nextstr.center(40))
print(len(nextstr.center(40)))
print(b.count("gauri"))
print(nextstr.endswith("!!"))
print(nextstr.endswith("ing", 3,10))

print(nextstr.find("!"))
nextstr1="WelcomeToPython"
print(nextstr1.isalnum())#this is true for A-Z, a-z,0-9
nextstr1="Welcome00"
print(nextstr1.isalpha())#this is true for A-Z,a-z

print(nextstr.find("@!"))#for getting this is not exist
# print(nextstr.index("!@"))#for getting error

nextstr1="hello world\n"
print(nextstr1.islower())
print(nextstr1.isprintable())
str1="        "      #using spaceabr
print(str1.isspace())
str2="          "        #using tab
print(str2.isspace())
str1="World Health Organisation"
print(str1.istitle())
str2="To kill a mocking bird "
print(str2.istitle()) 
str1="python is my fav language"  
print(str1.startswith("is"))
str1="Python Is My Fav Language"  
print(str1.swapcase()) #to intercgange lower=upper
str1="My name is gauri. i am very honest"
print(str1.title())

#TIMESTAMP
import time
timestamp=time.strftime('%H: %M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
timestamp=int(time.strftime('%M'))
print(timestamp)
timestamp=int(time.strftime('%S'))
print(timestamp)

# x=int(input("Enter the value of x: "))
# #x is the variable to match
# match x:
#     #if x is zero
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")
#     case _ if x!=90:
#         print(x, "is not 90")
#     case _:
#         print(x)


name='gauri'
for i in name:
    print(i)
    if(i =="b"):
        print("This is something special!")

colors= ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k+1)

#for k in range(1, 200):
    #print(k)

#for i in range(3):
   # print(i)

i=0
while(i<3):
    print(i)
    i=i+1

# i= int(input("Enter the number: "))
# while(i<=38):
#        i=int(input("Enter the number: "))
#        print(i)
# print("done with the loop")

count=5
while (count>0):
    print(count)
    count=count-1
else:
    print("i am inside else")

for i in range(12):
    if(i==10):
        break
    print("5 x", i+1, "=", 5*(i+1))

print("skip the loop")

for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 x", i+1, "=", 5*(i+1))

i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

def calculateGmean(a, b):
    mean= (a*b)/(a+b)
    print(mean)

a=8
b=9
def isGreater(a,b):
    pass
# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")


# gmean1=(a*b)/(a+b)
# print(gmean1)
calculateGmean(a,b)

def average(a=9, b=1,c=1):
    print("the average is", (a+b+c)/2)
average()

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        #print("the average is",   sum/len(numbers))
        return 5
        return sum/len(numbers)       # if there are 2 returns then first one will be prior
c= average(5,6,7,8)
print(c)

#list

# marks=[93, 95, 89, "Gauri"]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[-3])

# if 93 in marks:
#     print("yes")
# else:
#     print("no")

# #same things applies for strings as well
# if "Ga" in "Gauri":
#     print("yes")
# print(marks[:])
# print(marks[1:4])
# print(marks[0:4:3])
# print(marks[1:4:2]) #jump index

# list=[i for i in range(5)]
# list=[i*i for i in range(5)]
# list=[i*i for i in range(5) if i%2==0]
# print(list)

l=[11,23,1,45,1,5,3]
#l.append(11)
#l.reverse()
#l.sort(reverse=True)
#print(l.index(5))
#print(l.count(1))
# m=l.copy()
# m[0]=0
# l.insert(1,900)
#m=[900,1000,1100]
# k=l+m
# print(k)
#.extend(m)

print(l)

#tup=(1,)  #for tuple there is at least one value with comma
#tup = (1,2,76,342,32, "green", True)
#tup= [1,3,5]  #we cant change touple so we convert into list to chnge items by changes brackets from()to[]
#tup[0]=20
# print(type(tup), tup)
# print(len(tup))
# print(tup[0])
# print(tup[-1])


# if 32 in tup:
#     print("yes 23 is present in the tuple")
# tup2=tup[1:4]
# print(tup2)

countries = ("Spain", "India", "Italy", "England", "Germany")
temp =list( countries)
temp.append("Russia")  #add item
temp.pop(3)            #remove item
temp[2] = "Finland"   #change item
countries= tuple(temp)

print(countries)

countries2 = ("Chaina", "Usa", "Switserland")
world = countries+countries2
print(world)

tuple1 = (9,1,2,3,1,2,3,1,0)
#res = tuple1.count(1)
#res = tuple1.index(1)
#res = tuple1.index(1,2,8)
res=len(tuple1)
print("count of 1 in tuple1 is:", res)


#Letter format
letter = "Hey my name is {1} and i am from {0}"
country="India"
name="gauri"

#print(letter.format(name,country))
print(letter.format(country,name))   #if words are not in series than we can use numbers
print(f"We use fstrings lik this: Hey my name is {name} and i am from {country}")
print(f"We use fstrings lik this: Hey my name is {{name}} and i am from {{country}}")

price=29.34446
txt = f"For only {price: .2f} dollars!"
print(txt)
#print(txt.format(price=29.34446))
#print(txt.format())
print(f"{2*30}")
print(type(f"{2*30}"))

# READING A FILE
# f = open('myfile.text' , 'r')
# text = f.read()
# print(text)
# f.close()

#WRITING A FILE
# f = open('myfile2.txt' ,'a')  #'w' to write in file  ,'a' to append
# f.write('Hello, world!')
# f.close() 

def square(n):
    '''Takes in a number n, returns the square of n'''   #this is doc
    print(n**2)
square(5)
print(square.__doc__)  # to print the doc

#factorial(7) = 7*6*5*4*3*2*1
#factorial(6) = 6*5*4*3*2*1
#factorial(5) = 5*4*3*2*1
#factorial(4) = 4*3*2*1
#factorial(0) = 1

#factorial(n)= n* factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(3))
#print(factorial(4))
print(factorial(5))
#5 * factorial(4)
#5 * 4* factorial(3)
#5 * 4*3* factorial(2)
#5 * 4 * 3 * 2 * 1

#quick quiz:Write a program to print the Fibonacci sequence
#f(0) = 1
#f(1) = 1
#f(2) = f(1) + f(0)
#f(3) = f(n-1) + f(n-2)

#set theory
s = {2,5,2,6}
print(s)

info = {name , color , bool, "Gauri", name}
print(info)

Gauri = set()
print(type(Gauri))

for value in info:
    print(value)

s1 = {1,4,7,2}
s2 = {9, 8, 5}
print(s1.union(s2))
s1.update(s2)
print(s1 , s2)

# cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
# cities.intersection_update(cities2)
# print(cities)

# cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
# print(cities.isdisjoint(cities2))

# cities = {"Tokyo2" , "Madrid2" , "Berlin" , "Delhi"}
# cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
# print(cities.isdisjoint(cities2))

# cities = {"Tokyo2" , "Madrid2" , "Berlin" , "Delhi"}
# cities2 = {"Seoul" , "Kabul" }
# print(cities.issuperset(cities2))
# cities3 = {"seoul" , "madrid" , "kabul"}
# print(cities.issuperset(cities3))

# cities = {"tokyo" , "madrid" , "berlin" , "delhi"}
# cities.add("Helsinki")
# print(cities)

cities = {"tokyo" , "madrid" , "berlin" , "Delhi"}
cities.remove("Delhi")
print(cities)

#DICTIONARY
# dic = {
#     "Harry" : "Human being",
#     "Spoon" : "Object"
# }

# print(dic["Harry"])

dic = {
    344 : "Gauri",
    47 : "Arti"
}
print(dic[47])

info = {'name':'karan' , 'age':19, 'eligible':True}
print(info)
# print(info['name'])
# print(info.get('name'))
# #print(info['name2'])
# print(info.get('name2'))   #TO GET NONE\ 
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")












 

















































































































































































































































































































































































































































    
    



 






    











