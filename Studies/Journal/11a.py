import re


def validate_email(email):
    search = re.match("[0-9]*[a-z]+[0-9]*[./_]?[a-z]*[0-9]*@[ymail/gmail/yahoo]+[.com/.co.in]+", email)

    print(f"Your Email id : {email} is valid") if search else print("Invalid Email id.")


inp_Email = input("Enter your email id : ")

validate_email(inp_Email)

inp_Email = input("Enter your email id : ")

validate_email(inp_Email)
