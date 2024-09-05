"""
here we will define all the functions and handle each process
"""

import  re


def generate_email(name):
    try:
        # Split the name (format: "Last Name, First Name Middle Names")
        last_name, first_name = name.split(",")

        # Extract the first name and strip any extra spaces
        first_name = first_name.split()[0].strip()
        last_name = last_name.strip()

        # Generate the email using the first letter of the first name and the last name
        email = f"{first_name[0].lower()}{last_name.lower()}@gmail.com"

        return email

    except Exception as e:
        # Return None if the name is not formatted correctly
        return None


if __name__ == "__main__":
    name = input("Enter your name in 'Last Name ,First Name ,Middle Name(s) 'format:")
    email=generate_email(name)
    print(f"Your email is {email}")


