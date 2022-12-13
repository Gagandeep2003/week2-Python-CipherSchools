# define a function which will take list containing numbers as input 
# and return list containing square of every elements

# example
# numbers = [1,2,3,4]
# square_list(numbers) ---> return -----> [1,4,9,16]

# solution

def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
# list,str

numbers=list(range(1,11))
print(square_list(numbers))