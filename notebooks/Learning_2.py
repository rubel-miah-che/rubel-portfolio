#Example
def unitchange(func):
    def f():
        t=func()
        return ((t-32)/9)*5
    return f
@unitchange
def s():
    return 50
print(s())

#Example
