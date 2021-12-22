class Test:
    def __init__(self, a , b):
        self.a=a
        self.b=b

    def sum(self):
        print(a+ b)
        
a=input("enter: ")
b=input("enter: ")
p=Test(a,b)
p.sum()








'''print("You are in Aqib Program")
print("Wellcom To Aqib Program")
print("If you create a new accout so please write create other wise you have allready create a accouunt then you write sigin")
for i in range(1 , 5):
    account =input("Please enter this action (create or sign) : ")
    if account=="create":
        username = input("Please enter your name : ")
        usermail = input("Please enter your mail : ")
        dob      = input("Plaase enter your date-Of-Birth : ")
        password = input("Create your password : ")
        conformpassword = input("Please re enter your Pass for matching : ")
        if password == conformpassword:
            print("your acount hase been created")
        else:
            print("Please check your conform password")
            
        break
    elif account=="sign":
        usermail = input("Please enter your mail : ")
        password = input("Please enter your password : ")
        if usermail == "mohdaqib79656@gmail.com" and password == "MohdAqib123456":
            print("Hello Mohd Aqib")
        else:
            print("Please enter right information")
        break
    else:
        print("Please enter correct action")
'''



'''mystr = "banannaaa"


for i in mystr:
    print(i)

'''



'''class Aqib:
    def __init__(self , name , age):
        self.name = name
        self.age = age

print("detail", a2.age,a2.name)
    def update(self):
        self.age = 30
        self.upd = "update"

a1 = Aqib("aqib",20)
a2 = Aqib("Saifi",18)
print("detail", a1.age,a1.name)
print("detail", a2.age,a2.name)
a2.update()
print("detail", a2.age,a2.name,a2.upd)
        
'''













'''class Kingdom:                             
    def __init__(self, act , first , second , action):      
        self.act = act
        self.first = first
        self.second = second
        self.action = action
    
    def story(self):
        if self.act=="king":
            print("The Pot of the Wit")
            print("Once Emperor {0} became very angry at his favorite minister {1}. He asked {1} to leave the kingdom and go away. Accepting the command of the Emperor, {1} left the kingdom and started working in a {2}.".format(self.first, self.second, self.action))
        else:
            print("Crows in the Kingdom")
            print("One day Emperor {0} and {1} were taking a walk in the palace {2}. It was a nice summer morning and there were plenty of crows happily playing around the pond. While watching the crows, a question came".format(self.first, self.second, self.action))



if __name__ == '__main__':
    act = input("Enter the Story name (king or crows) : ")
    first = input("Enter the first name : ")
    second = input("Enter the second name : ")
    action = input("Enter the working place name like shope name : ")
    
    obj = Kingdom(act , first , second , action)
    obj.story()


'''


'''  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.action = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("mohd aqib", 36)
p1.myfunc()

'''



'''print("Nutshell")
print("Creater Name Mohd Aqib")
place=input("Enter the place name ")
action=input("Enter the action ")
txt = "The nutshell is {}."
tet = "this is the action of nutshell {}"
print(txt.format(place))
print(tet.format(action))

'''



'''a=input("Enter number of stars you need ")
for x in range(int(a)):
    for y in range(x):
        print("*", end="")
    for z in range(x-1):
        print("/", end="")
    for a in range(x):
        print("&", end="")
    print()'''
'''
a=input("Enter number of stars you need ")
i="*"
for row in range(1,int(a)):
    for call in range(row):
        print(i, end="")
    print()
'''

'''#Calculater----

print("Hello You are in the Aqib Calculater")
print("Please enter if you need + for 1, - for 2, * for 3 ,/ for 4")
x=input("enter the any case ")
print("Please Enter the numbers")
a=input("Enetr the first number ")
b=input("enter the second number ")
if int(x)==1:
    c=int(a)+int(b)
    print("the addition of two number is:" +str(c))
elif int(x)==2:
    c=int(a)-int(b)
    print("the addition of two number is:" +str(c))
elif int(x)==3:
    c=int(a)*int(b)
    print("the addition of two number is:" +str(c))
elif int(x)==4:
    c=int(a)/int(b)
    print("the addition of two number is:" +str(c))
else:
    print("enter the Valid number")

'''




'''#Star Partern Print----
a=input("Enter number of stars you need ")
i="*"
for row in range(1,int(a)):
    for call in range(row):
        print(i, end="")
    print()
    
'''



'''a=input("Enter ")
print(len(a))

if int(len(a))>10:
    
    print("It's a Sentance")
elif  int(len(a))>3:
    print("It's a Character")
else:
    print("Is's a integer")


'''

'''i="*"
for row in range(1,5):
    for col in range (row):
        print(i, end="")
    print()''


'''

'''
class Name:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc1(self):
    print("Hello my name is " + self.name)

p1 = Name("Mohd Aqib", 21)
p1.myfunc1()

'''

'''class Person:
  def __init__(self, name, age):




#-------
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name,p1.age)
print(p1.age)

#-----
a=input("prelas input a number ")
b=input("please enter the second number ")
if int(a)<=10 and int(a)%2:
    if int(b)<=10:
        print("the number is less then 10" )
        print (a + b)
else:
    print("number is greater then 10")'''
#------------For loop with itreater
"""
a=[ 'aqib', 'shovam' , 'rea' ,'zea']
for x in a:
    print(x)
output
aqib index no0
shovam 1 
rea 2 
zea 3
"""
#-----
"""x = range(5)
type(x)
for i in x:
    print(i)
output
0
1
2
3
4"""
#-----




















