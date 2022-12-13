# split method
# convert string to list
name,age = 'harshit,24'.split(',')
print(name)
print(age)


name,age = input("enter you name and age ").split(',')
print(name)
print(age)


# join method 
# convert list to string

user_info=['Hasrhit','24']
print(",".join(user_info))