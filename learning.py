#Intro
print("Hello world!")
a = 2
b = 3
print(a * b)
c = "TRUE"
if a < b:
    print(c)
print(type(a))
my_name = "Rubel"
print(my_name)
u, me = "sefa", "Rubel"
print(u)
print(me)
#unpack a collection
flowers = ["Rose", "jui", "lily"]
x, y, z = flowers
print(x)
print(y)
print(z)
p = "Sefa"
q = "is"
r = "love"
print(p + q + r)
#Global Variables
w = "Sefa"


def f():
    print(r, q, w)


f()
a1 = "Cute"


def g():
    a_1 = "Beautiful"
    print("You are", a_1)


g()
print("You are", a1)
x = 7
print(x)
x = 9


def func():
    global x
    x = "Sefa"
    print(x)


func()
print("She is", x)
print("you are", x)
#dict variables
y = {"name": "Sefa", "age": 23}
print(type(y))
print(y)
y = dict(name="Rubel", age=25)
print(y)
#numbers
p = 1
q = 3.99
r = 3 + 4j
print(type(r))
a = float(p)
print(a)
a = int(q)
print(a)
import random

print(random.randrange(1, 10))
a = str(7)
b = str(2)
print(a + b)
a = "Sefa,Rubel"
print(a[0:4])
a = "There is a cow"
print(len(a))
for x in a:
    print(x)
a = "Python is free"
print("x" in a)
a = "She is good"
if "z" not in a:
    print("no, good is not present")
a = "She is good"
print(a[-6:-3])
a = "She is good"
print(a.upper())
print(a.lower())
#Remove Whitespace
a = "Here is a boy!  "
print(a.strip())
print(a.replace("boy", "girl"))
print(a.split())
a = "Rubel"
b = "Sefa"
print(a, b)
age = 36
print(f"My name is John, I am {age}")
a = 9
b = 8
c = a + b
print(f"The sum is {c:.10f}")
print(f"This is {11 + 3}")
print("I om \"Ripon video\"")
a = "The cow is Big"
print(a.capitalize())
print(a.casefold())
print(a.count("i", 2, 7))
print(a.center(25, "*"))
print(a.endswith("c", 1, 5))
print(a.find("B", 0, 15))
a = "H\te\tl\tl\to"
print(a)
print(a.expandtabs(1))
txt = f"We have {41:>10} chickens."
print(txt)
#how to use dict in f style
y = {"name": "Rubel", "age": 25}
print(f"My name is {y["name"]} and I am {y["age"]}")
#Python Booleans
print(10 < 3)
a = 30
b = 33
if a > b:
    print("a>b")
else:
    print("b>a")
a = "c"
print(bool(a))
#Operator
a = 2
b = 4
print(a ** b)
a = 19
b = 4
print(a // b)
print(p := 3)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is not y)
print(x == y)
print("apples" in x)
#list
li = ["ruti", "rice", "egg", "muri"]
print(li)
print(len(li))
li = list(("ruti", "rice", "egg", "muri"))
print(li)
print(type(li))
#list item replace
li = ["ruti", "rice", "egg", "muri"]
li[1] = "water"  #replace one
print(li)
print(type(li))
print(li[0:3])
li[1:2] = ["pitha", "gur"]  #one replace and one add next to it
print(li)
li.append("patisapta")  #add at the end
print(li)
li.insert(2, "ilish")  #add any index
print(li)
li = ["a", "e", "i", "o", "u"]
li_1 = ["w", "y"]
li.extend(li_1)
print(li)
li.extend(["love"])
print(li)
li = ["a", "e", "i", "o", "u"]
li.pop(1)
print(li)
li.remove("a")
print(li)
li = ["a", "e", "i", "o", "u"]
del li
li = ["a", "b", "c"]
li.clear()  #to clear the list
print(li)
a = "rubel"
li = ["apple", "egg", "ilish", "o", "u"]
for x in li:
    print(x)
[print(x) for x in li]  #short hand
a1 = "rubel"
i = 0
while i < len(a):
    print(a[i])
    i = i + 1
a1 = "rubel"
i = 0
while i < 5:
    print(a[i])
    i = i + 1
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = [x for x in fruits if "a" in x]
print(new)
#Sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()  #alphabetical order
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()  #small to greater
print(thislist)
thislist = [100, 50, 65, 82, 23]


def f(n):
    return n < 80  #here the value satisfy the equation will sit last, which doesn't satisfy sit prior


thislist.sort(key=f)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(
    key=str.casefold)  #Sort the list in a way that each word is first converted to lowercase, then arranged alphabetically.
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for p in list2:
    list1.append(p)
print(list1)
#tuples
tup = ("apple", "egg", "ilish", "o", "u")
print(type(tup))
print(tup)
print(len(tup))
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = "apple"
print(type(thistuple))
tup = ("apple", "egg", "ilish", "o", "u")
print(tup[1])
print(tup[1:])
if "u" in tup:
    print("yes")
else:
    print("no")
#replace of tuple item
tup = ("apple", "egg", "ilish", "o", "u")
y = list(tup)
y[1] = "banana"
print(y)
tup = tuple(y)
print(tup)
#addition of tuple item
fruits = ("apple", "banana", "cherry", "kiwi", "mango")
y = list(fruits)
y.insert(2, "love")
fruits = tuple(y)
print(fruits)
fruits = ("apple", "banana", "cherry")
(x, y, z) = fruits
print(x)
print(y)
print(z)
fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)
for i in range(len(fruits)):
    print(fruits[i])
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1
fruits = ("a", "b", "c")
[print(x) for x in fruits]
#join tuples
t1 = ("a", "b", "c")
t2 = (1, 2, 3)
t = t1 + t2
print(t)
t3 = 3 * t2
print(t3)
x = t3.count(1)
print(x)
fruits = ("a", "b", "c")
y = fruits.index("b")
print(y)
#sets
thisset = {"apple", "banana", "cherry"}  #To add one item to a set use the add() method.
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
thislist = list(thisset)
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
r = x.copy()
print(r)
print(type(r))
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 8, 9}
print(a - b)
c = a.difference(b)
print(c)
print(a & b)
print(b.issubset(a))
print(a <= b)
print(a | b)
print(a ^ b)  #common elements will be eliminated

a = {1, 2, 3, 4, 8, 9, 11}
b = {3, 4, 5}
print(a - b)  #here new set is created
print(a)
a -= b  # here old set is retained, but some elements are eliminated
print(a)
#Python Dictionaries
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(dict1)
print(dict1["brand"])
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print(type(thisdict))
thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)
d=dict(name="Sefa", age=21)
print(d)
x=d.get("age")
print(x)
x=d.keys()
print(x)
d["Husband"]="Rubel"
print(d.keys())
print(d.values())
d["age"]=22
print(d)
print(d.items())
if "age" in d:
    print("yes")
else:
    print("No")
di=dict(name="Sefa", age=21)
di.update({"age": 23})
print(di)
di=dict(name="Sefa", age=21)
di.update({"age":23})
print(di)
di.update({"F":"A"})
print(di)
di["H"]="R"
print(di)
for x in di:
    print(x)
for x in di.values():
    print(x)
for x in di.items():
    print(x)
us={"me":{"name":"Rubel", "Birth":2000},"bou":{"name":"Sefa", "birth":2003}}
print(us)
print(us["me"]["name"])
thisdict1 = dict(name = "John", age = 36, country = "Norway")
[print(x+":",thisdict1[x]) for x in thisdict1]
for x in thisdict1:
    print(x+":",thisdict1[x])
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "red") #if value is present, then it returns that value. If not present, add that and returns
print(x)
print(car)
#if else statement
a=10
b=15
if a>b:
    print("a is greater")
else:
    print("b is greater")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:#if the previous conditions were not true, then try this condition
  print("a and b are equal")
#Nested if
#Example 1
age=19
has_license=False
if age>=18:
    if has_license:
        print("You can drive")
    else:
        print("you need license")
else:
    print("you are under age")
#Example 2
Mark=65
attendance=82
Submitted=True
if Mark>=60:
    if attendance>=80:
        if Submitted:
            print("pass")
        else:
            print("pass but not submitted")
    else:
        print("pass but low attendance")
else:
    print("Fail")
#for loops
name="Rubel"
[print(x) for x in name]
#Fuctions
#Example 1
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
#Example 2
def f(name):
    return(name+" ""Miah")
print(f("Rubel"))
print(f("Alamin"))
#example 3
def f(fruits):
    for x in fruits:
        print(x)
a="apple", "banana","pear"
f(a)
#Example 4
def f(x):
    return x**x
print(f(3))
#Ex 4
def my_function(name):
  print("Hello", name)
#ex 5
my_function(name = "Emil")
def my_function(*, name):
  print("Hello", name)

my_function(name="Emil")
#ex 6
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
#ex 7
def f(*args):
    print("Me:", args[0])
    print("You:", args[1])
f("Rubel","Sefa")
#Ex 8
def f(*args):
    for x in args:
        print(x)
f("Rubel","Sefa")
#ex 9
def f(*numbers):
    total=0
    for n in numbers:
        total+=n
    return total
print(f(1,2,3))
#ex 10
def f(*numbers):
    if len(numbers)==0:
        return None
    max=numbers[0]
    for n in numbers:
        if n>max:
            max=n
    return max
print(f(1,2,6,9))
#ex 11
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
#ex12
x = 10     # এটা বাইরের (global) ভ্যারিয়েবল

def myfunc():
    global x   # এখানে বলছি: বাইরের x ব্যবহার করব, নতুন বানাবো না
    x = 20     # তাই এই লাইন আসলে বাইরের x-এই পরিবর্তন করছে

myfunc()
print(x)
#ex13
def myfunc1():
    x = "Jane"
    def myfunc2():
        x = "hello"   # ❌ নতুন লোকাল x তৈরি হলো, বাইরেরটা বদলাল না
    myfunc2()
    return x

print(myfunc1())
#ex 14
def myfunc1():
    x = "Jane"            # ← outer function-এর লোকাল ভ্যারিয়েবল
    def myfunc2():
        nonlocal x        # ← বলছে: বাইরের (myfunc1 এর) x ব্যবহার করব
        x = "hello"       # ← তাই এটা বাইরের x-এর মান পরিবর্তন করছে
    myfunc2()
    return x

print(myfunc1())
#ex 15
x = "global"

def outer():
    y = "outer local"

    def inner():
        global x      # গ্লোবালটা বদলাবে
        nonlocal y    # outer ফাংশনেরটা বদলাবে
        x = "changed globally"
        y = "changed nonlocally"

    inner()
    print("y inside outer:", y)

outer()
print("x outside:", x)
#Example
def leap(y):
    if (y%4==0 and y%100!=0) or (y%400==0):
        return "Leap year"
    else:
        return "Not leap year"
print(leap(2000))
#ex
def f(t):
    return (t/5)*9+32
print(f(-40))
#example
def changecase(f1):
    def f2():
        return f1().upper()
    return f2
@changecase
def f():
    return "Hello bou"
print(f())
@changecase
def g():
    return "my name is rubel"
print(g())
