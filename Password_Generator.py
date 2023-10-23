import random
import string

def generate_password(length):
    # Defining the character set
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combination of character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # To Randomly generate Password
    password = ''.join(random.choice(all_characters) for char in range(length))
    return password

def main():
    try:
        # Geting password length from the user
        length = int(input("Enter the desired password length: "))

        if length <= 0:
            print("Password length must be greater than 0 length.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a number for length of the password.")

if __name__ == "__main__":
    main()
