def sum(x,y):
   return x+y
    

y=sum(5,6)
print(y)

def myname(name , age):
   return print(f"hello {name} your age is {age}")

myname("ahmed",15)


def mul(x=5,y=2):
   return x*y
    

g = mul(6)
print(g)


#anonymous function
o = lambda x,y=0: x * y

print(o(5))
