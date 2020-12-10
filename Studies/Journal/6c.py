# Write a program to implement exception handling.


def TypeException():
    try:
        my_string = "a"
        c = 5 + my_string
    except TypeError as e:
        print(f"This is TypeError ==> {e}")
    else:
        print(c)
    finally:
        print("TypeError function has been executed")


TypeException()


print("\n==================================================\n")


def NameException():
    try:
        print(b)
    except NameError as e:
        print(f"This is NameError ==> {e}")
    else:
        print("Working!!")
    finally:
        print("NameError function has been executed")


NameException()
