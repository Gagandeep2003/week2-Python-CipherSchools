# functions practice 
def last_char(name):
    return name[-1]

print(last_char("harshit vashisth"))
# last_char[9] #error



# another way
def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
num = 9
print(odd_even(num))



# another way
def odd_even(num):
    if num%2 == 0:
        return "even"
    return "odd"
print(odd_even(9))




# another  way
def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
print(is_even(9))
       
       


        # Another way
def is_even(num):
    return num%2 == 0 #true

print(is_even(9))





# new
def song():
    return "happy birthday song"
print(song())