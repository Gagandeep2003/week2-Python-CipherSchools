# default parameters

def user_info(first_name, last_name, age):
    print(f"Your first name is {first_name}")
    print(f"Your first name is {last_name}")
    print(f"Your first name is {age}")

user_info("Harshit","Vashisth",23)



def user_info(first_name, last_name, age = None):
    print(f"Your first name is {first_name}")
    print(f"Your first name is {last_name}")
    print(f"Your first name is {age}")

user_info("Harshit","Vashisth")


def user_info(first_name, last_name = "Unknown", age = None):
    print(f"Your first name is {first_name}")
    print(f"Your first name is {last_name}")
    print(f"Your first name is {age}")

user_info("Harshit","Vashisth",23)


# def user_info(first_name, last_name = "Unknown", age):        <----- This code will make error because last_name has default parameter but age does not have
#     print(f"Your first name is {first_name}")
#     print(f"Your first name is {last_name}")
#     print(f"Your first name is {age}")

# user_info("Harshit","Vashisth",23)                