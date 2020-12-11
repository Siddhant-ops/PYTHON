my_string = input("Enter a String : ")


def return_even_char(my_string):
    result = ""

    for i in range(len(my_string)):
        if i % 2 != 0:
            result += my_string[i]

    print(result)


return_even_char(my_string)
