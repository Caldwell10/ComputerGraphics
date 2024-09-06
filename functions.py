"""
here we will define all the functions and handle each process
"""

import  re
import logging





def generate_email(name):
    try:
        # Split the name (format: "Last Name, First Name Middle Names")
        last_name, first_name = name.split(",")

        # Extract the first name and strip any extra spaces
        first_name = first_name.split()[0].strip()
        last_name = last_name.strip()

        #remove any special characters from the last name
        last_name_clean=re.sub(r"[^a-zA-Z]","", last_name.lower())


        # Generate the email using the first letter of the first name and the last name
        email = f"{first_name[0].lower()}{last_name_clean}@gmail.com"

        return email

    except Exception as e:
        # Return None if the name is not formatted correctly

      logging.error(f"Error processing name {name}")
    return None

def log_student_count(male_count, female_count):
   #logs the count of both male and female students
    logging.info(f"Number of male students: {male_count}")
    logging.info(f"Number of female students: {female_count}")
