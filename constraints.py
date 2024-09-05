
import re
from functions import name
"""
here we will handle all the constraints
"""

def handle_special_characters():
    """Checks if the name has special characters
        Returns true if special characters are found, false otherwise"""

    if re.search(r"[^-zA-Z\s,']",name):
        return True
    else:
        return False