import re

def check_password_strength(password):
    if len(password) < 8 :                                        # Function to check password strength
        return "Use minimum 8 characters in the password : Weak Password !"
    
    if not any(char.isdigit() for char in password):              # checks if digits are there in password
        return "Must have atleast one digit in the password : Weak Password !"
    
    if not any(char.isupper() for char in password):              # checks for uppercase letters
        return "Must have atleast one uppercase letter in the password : Weak Password !"
    
    if not any(char.islower() for char in password):              # checks for lowercase letters
        return "Must have atleast one lowercase letter in the password : Weak Password !"
    
    if not re.search(r'[!@#$%^&*(){}<>.,?]', password):           # checks if password has special characters
        return "Must have atleast one special character : Medium Password !"
    
    return "Password is all set! : Strong Password"

def password_checker():

    print("-" * 70)
    print(" ||||||||||  WELCOME TO PASSWORD STRENGTH CHECKER TOOL  ||||||||||")       # Theme of Password Checker Tool
    print("-" * 70)

    while True:

        password = input("\nEnter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':

            print("\n Thank you for using the Password Checker Tool!")
            break

        result = check_password_strength(password)

        print(result)

# Run the program
if __name__ == "__main__":
    password_checker()