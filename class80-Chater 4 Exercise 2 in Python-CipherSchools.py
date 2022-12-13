#  Define is_pallindrome function  that take one word in string as input
# And return True if it is pallindrome else return False



# pallindrome - word that reads same backwards as forwars


# example
# is_pallindrome("madam") ---> True
# is_pallindrome("naman") ---> True
# is_pallindrome("horse") ---> False

# logic (algorithm)
# step 1 -> reverse the string 
# step 2 -> compare reverse string with original string


# SOLUTION

def is_pallindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

print(is_pallindrome("naman"))
print(is_pallindrome("horse"))

# Another way

def is_pallindrome(word):
    if word == word[::-1]:
        return True
    return False

print(is_pallindrome("naman"))
print(is_pallindrome("horse"))

# Another Way

def is_pallindrome(word):
    return word == word[::-1]

print(is_pallindrome("naman"))
print(is_pallindrome("horse"))

