# define a function which will take list as argument and this function 
# will return a reversed list

# examples
# [1,2,3,4] --> [4,3,2,1]
# ['word1','word2'] --> ['word2','word1']

# NOte you simply do this with the reverse method or [::-1]
# but you have to do this with the help of append or pop method

# solution

def reverse_list(l):
    l.reverse()
    return l


numbers = [1,2,3,4]
print(reverse_list(numbers))

# another way
def reverse_list(l):
    return l[::-1]

numbers = [1,2,3,4]
print(reverse_list(numbers))


# Another Way
def reverse_list(l):
    r_list =[]
    for i in range(1,len(l)+1):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
numbers = [1,2,3,4]
print(reverse_list(numbers))