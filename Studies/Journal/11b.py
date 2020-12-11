import re

mobile = input("Enter your mobile number : ")
search = re.match("(0)*[0-9]{10}$", mobile)

if len(mobile) == 10:
    if search:
        print(f"Your mobile number : {mobile} is valid")
    else:
        print(f"Your mobile number : {mobile} is not valid")
else:
    print("Please enter a 10 digit mobile number")
