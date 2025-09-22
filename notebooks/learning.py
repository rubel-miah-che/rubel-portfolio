#Intro
print("Hello world!")
a=2
b=3
print(a*b)
c="TRUE"
if a<b:
    print(c)
print(type(a))
my_name="Rubel"
print(my_name)
u,me="sefa","Rubel"
print(u)
print(me)
#unpack a collection
flowers=["Rose", "jui", "lily"]
x,y,z=flowers
print(x)
print(y)
print(z)
p="Sefa"
q="is"
r="love"
print(p+q+r)
#Global Variables
w="Sefa"
def f():
    print(r,q, w)
f()
a1="Cute"
def g():
    a_1= "Beautiful"
    print("You are", a_1)
g()
print("You are", a1)
x=7
print(x)
x=9
def func():
    global x
    x="Sefa"
    print(x)
func()
print("She is", x)
print("you are", x)
#dict variables
y={"name":"Sefa","age":23}
print(type(y))
print(y)
y=dict(name="Rubel", age=25)
print(y)
#numbers
p=1
q=3.99
r=3+4j
print(type(r))
a=float(p)
print(a)
a=int(q)
print(a)
import random
print(random.randrange(1,10))
a=str(7)
b=str(2)
print(a+b)
a="Sefa,Rubel"
print(a[0:4])
a="There is a cow"
print(len(a))
for x in a:
    print(x)
a="Python is free"
print("x" in a)
a="She is good"
if "z" not in a:
    print("no, good is not present")
a="She is good"
print(a[-6:-3])
a="She is good"
print(a.upper())
print(a.lower())
#Remove Whitespace
a="Here is a boy!  "
print(a.strip())
print(a.replace("boy", "girl"))
print(a.split())
a="Rubel"
b="Sefa"
print(a,b)
age = 36
print(f"My name is John, I am {age}")
a=9
b=8
c=a+b
print(f"The sum is {c:.10f}")
print(f"This is {11+3}")
print("I om \"Ripon video\"")
a="The cow is Big"
print(a.capitalize())
print(a.casefold())
print(a.count("i",2,7))
print(a.center(25,"*"))
print(a.endswith("c",1,5))
print(a.find("B",0,15))
a="H\te\tl\tl\to"
print(a)
print(a.expandtabs(1))
txt = f"We have {41:>10} chickens."
print(txt)
#how to use dict in f style
y={"name":"Rubel","age":25}
print(f"My name is {y["name"]} and I am {y["age"]}")
#Python Booleans
print(10<3)
a=30
b=33
if a>b:
    print("a>b")
else:
    print("b>a")
a="c"
print(bool(a))
#Operator
a=2
b=4
print(a**b)
a=19
b=4
print(a//b)
print(p:=3)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is not y)
print(x==y)
print("apples" in x)
#list
li=["ruti","rice","egg","muri"]
print(li)
print(len(li))
li=list(("ruti","rice","egg","muri"))
print(li)
print(type(li))
#list item replace
li=["ruti","rice","egg","muri"]
li[1]="water" #replace one
print(li)
print(type(li))
print(li[0:3])
li[1:2]=["pitha", "gur"] #one replace and one add next to it
print(li)
li.append("patisapta") #add at the end
print(li)
li.insert(2,"ilish") #add any index
print(li)
li=["a","e","i","o","u"]
li_1=["w", "y"]
li.extend(li_1)
print(li)
li.extend(["love"])
print(li)
li=["a","e","i","o","u"]
li.pop(1)
print(li)
li.remove("a")
print(li)
li=["a","e","i","o","u"]
del li
li=["a","b","c"]
li.clear() #to clear the list
print(li)
a="rubel"
li=["apple","egg","ilish","o","u"]
for x in li:
    print(x)
a1="rubel"
i=0
while i<len(a):
    print(a[i])
    i=i+1
print("hello world")