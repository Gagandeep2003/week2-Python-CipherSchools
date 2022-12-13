# if statement
name = "Mohit"
if name == "harshit" or name == "Harshit":
    print("you are harshit")
elif name == "mohit" or name == "Mohit":
    print("you are mohit")
else:
    print("you are not harshit or mohit")

# while
i = 0
while i < 10:
    print(i)
    i += 1

# for loop
for i in range(1,11,2):
    print(i)

# break keyword
for i in range (1,11):
    if i == 5:
        break
    print(i)

# continue keyboard
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# new way
for i in "harshit":
    print(i)