import string
import random

useable = string.ascii_letters + string.digits + string.punctuation


def generator(min_len = 8):
    password = ''.join(random.choices(useable,k=min_len))
    return password

def check_password(password):
    count = [0,0,0,0]
    for char in password:
        if char not in useable:
            return False
        elif char in string.ascii_lowercase:
            count[0] += 1
        elif char in string.ascii_uppercase:
            count[1] += 1
        elif char in string.digits:
            count[2] += 1
        elif char in string.punctuation:
            count[3] += 1

    if 0 in count:
        return False

    return True
        
def get_length():
    change = input("Would you like to choose the length of your password? \nEnter y for yes: ")
    if change != 'y':
        return 8
    length = int(input("The minimum length is 8. Please enter a greater number: "))
    if length < 8:
        return 8
    return length
                  


def main():
    ans=input("Hello! Would you like to generate a new password?\n Please enter y/n: ")
    if ans == "y":
        password = generator(get_length())
        print ("your generated password is: {}".format(password))
        if check_password(password):
            print("Your new password is strong!")
            print("Thank you for using password generator!")
        else:
            print("Your new password is weak. It is recomended to change it.")
            main()

    elif ans == "n":
        print("OK. Thank you and goodbye")
    else:
        print ("Your answer should be y/n")
        main()
    
    
main()
