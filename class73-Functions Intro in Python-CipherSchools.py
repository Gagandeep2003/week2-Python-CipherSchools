# functions
name = "harshit"
print(len(name))

def add_two(a,b): # also we can write anything instead of a and b
    return a+b

total = add_two(5,4)
print(total)
# another way
print(add_two(5,4))


def add_two(num1,num2): 
    return num1 + num2

a=int(input("enter first number : "))
b=int(input("enter second number : "))
total = add_two(a,b)
print(total)

first_name = input("type first name ")
last_name = input("type last name ")
print(add_two(first_name,last_name))