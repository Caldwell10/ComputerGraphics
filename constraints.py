import re

"""
Here we will handle all the constraints.
"""


def handle_special_characters(name):
    """Checks if the name has special characters.
       Returns True if special characters are found, False otherwise."""
    # Look for anything that is not a letter (a-z, A-Z), a comma, or a space
    if re.search(r"[^a-zA-Z\s,]", name):
        return True
    else:
        return False