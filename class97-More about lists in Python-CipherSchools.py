# generate list with ranege function
# something more about pop method
# index method
# pass list to a function

numbers = list(range(1,11))
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,5,7,8,1,]
print(numbers)

popped_item = numbers.pop()
print(numbers)

print(numbers.index(1))
print(numbers1.index(1,11))
# print(numbers.index(1,11,14))


def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers1))
