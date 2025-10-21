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
[print(x) for x in li] #short hand
a1="rubel"
i=0
while i<len(a):
    print(a[i])
    i=i+1
a1="rubel"
i=0
while i<5:
    print(a[i])
    i=i+1
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new=[x for x in fruits if "a" in x]
print(new)
#Sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #alphabetical order
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort() #small to greater
print(thislist)
thislist = [100, 50, 65, 82, 23]
def f(n):
    return n<80 #here the value satisfy the equation will sit last, which doesn't satisfy sit prior
thislist.sort(key=f)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.casefold) #Sort the list in a way that each word is first converted to lowercase, then arranged alphabetically.
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for p in list2:
    list1.append(p)
print(list1)
#tuples
tup=("apple","egg","ilish","o","u")
print(type(tup))
print(tup)
print(len(tup))
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple="apple"
print(type(thistuple))
tup=("apple","egg","ilish","o","u")
print(tup[1])
print(tup[1:])
if "u" in tup:
    print("yes")
else:
    print("no")
#replace of tuple item
tup=("apple","egg","ilish","o","u")
y=list(tup)
y[1]="banana"
print(y)
tup=tuple(y)
print(tup)
#addition of tuple item
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
y=list(fruits)
y.insert(2,"love")
fruits=tuple(y)
print(fruits)
fruits = ("apple", "banana", "cherry")
(x,y,z)=fruits
print(x)
print(y)
print(z)
fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)
for i in range(len(fruits)):
    print(fruits[i])
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
fruits = ("a", "b", "c")
[print(x) for x in fruits]
#join tuples
t1=("a", "b", "c")
t2=(1, 2, 3)
t=t1+t2
print(t)
t3=3*t2
print(t3)
x=t3.count(1)
print(x)
fruits = ("a", "b", "c")
y=fruits.index("b")
print(y)
#sets
thisset = {"apple", "banana", "cherry"} #To add one item to a set use the add() method.
thisset.add("orange")
print(thisset)
thisset.remove("apple")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
[print(x) for x in thisset]
thisset = {"apple", "banana", "cherry"}
thislist=list(thisset)
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
r=x.copy()
print(r)
print(type(r))
a={1,2,3,4,5}
b={1,2,3,8,9}
print(a-b)
c=a.difference(b)
print(c)
print(a&b)
print(b.issubset(a))
print(a<=b)
print(a|b)
print(a^b) #common elements will be eliminated

a={1,2,3,4,8,9,11}
b={3,4,5}
print(a-b) #here new set is created
print(a)
a-=b # here old set is retained, but some elements are eliminated
print(a)