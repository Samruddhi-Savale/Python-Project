# Task 3:
# Random Password Generator
""" Create a program that generates a random password of user-defined length"""

import random
def gen_pwd(len):
    "This function accept a paratmeter 'len' and returns a randomly generated password"
    char_ls = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_-+={,}[]:;'<>,.?/|"
    selected_char = random.sample(char_ls,len)
    pwd_str = "".join(selected_char)
    return pwd_str
if __name__=="__main__":
    len = int(input("Enter the length of the password: "))
    pwd_str = gen_pwd(len)
    print("A randomly generated password is: ",pwd_str)