"""
here we will define all the functions and handle each process
"""

import  re


def generate_email (name):
    # Split the name (format: "Last Name, First Name Middle Names")
    last_name,first_name = name.split(",")
    #first name for word from the first name and strip any extra spaces
    first_name=first_name.split()[0].strip
    last_name=last_name.strip()
    email=f"{first_name[0].lower()}{last_name.lower()}.@gmail.com"

    return email

if __name__ == "__main__":
    name = input("Enter your name in 'Last Name ,First Name ,Middle Name(s) 'format:")
    email=generate_email(name)
    print(f"Your email is {email}")


