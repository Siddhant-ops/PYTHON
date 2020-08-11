# LESSER OF TWO EVENS:

# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

print("================================================================================================")
print("lesser of two evens")


def lesser_of_two_evens(a, b):
    # here we will \check if both the numbers are even
    if a % 2 == 0 and b % 2 == 0:
        # here min function is udsed to determine who has the minimum value
        return min(a, b)
    # if both of them are not even the else code block is trigered
    else:
        # here min function is udsed to determine who has the maximum value
        return max(a, b)


print(lesser_of_two_evens(6, 5))

# ANIMAL CRACKERS:

# Write a function takes a two-word string and
# returns True if both words begin with same letter

# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

print("================================================================================================")
print("animal crackers")


def animal_cracker(text):
    # now we split the paramter text and before spliting it we lower its alphabet
    input_list = text.lower().split()
    # we will return a boolean value if input_list[0][0] == input_list[1][0]
    return input_list[0][0] == input_list[1][0]


print(animal_cracker("Levelhead Llama"))

# MAKES TWENTY:

# Given two integers,
# return True if the sum of the integers is 20 or
# if one of the integers is 20.
# If not, return False

# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

print("================================================================================================")
print("makes twenty")


def makes_twenty(a, b):
    # here we return a boolean value if either the sum of the numbers is equal to 20 or the nums are equal to 20
    return a + b == 20 or a == 20 or b == 20


print(makes_twenty(20, 10))
print(makes_twenty(1, 18))
print(makes_twenty(2, 3))

# OLD MACDONALD:

# Write a function that capitalizes
# the first and fourth letters of a name

# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

print("================================================================================================")
print("old macdonald")


def old_macdonald(name):
    # here we split the first three letters int the keyword 'first'
    # and in the keyword 'second' we store the values from 3 onwards;
    first = name[:3]
    second = name[3:]
    # in keyword 'result' we store the concatenation of the capitalized keywords 'first' & 'second'
    result = first.capitalize() + second.capitalize()
    return result


print(old_macdonald("macdonald"))

# MASTER YODA:

# Given a sentence,
# return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here.
# The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'

# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
# >>> " ".join(['Hello','world'])
# >>> "Hello world"

print("================================================================================================")
print("master yoda")


def master_yoda(text):
    # here we split the input 'text' and store it in keyword 'input_list'
    input_list = text.split()
    # here we reverse the 'input_list' and store it in keyword 'result'
    result = input_list[::-1]
    # here we take a variable 'mystring' which is an empty string which only has a space
    # and we use the join method which joins the words present in the var 'input_list' and we use space to join those words
    # and make a single string
    mystring = " ".join(result)
    return mystring


print(master_yoda("I am home"))

# ALMOST THERE:

# Given an integer n,
# return True
# if n is within 10 of either 100 or 200

# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

# NOTE: abs(num) returns the absolute value of a number

print("================================================================================================")
print("almost there")


def almost_there(n):
    # here we chech if the given number is in between the range(90 to 110) or range(190 to 210)
    # we use abs() function which standout for absolute which works as a mod function of maths it removes the negative sign and makes it positive
    # in the abs funct we check the difference between 100 and given number or 200 and given number
    # abs function helps us int the following conditions:
    # if the given number is 109 which is more than 100 and while the checking the diff the ans would be (-9) and the abs would make it (9)
    # if the given number is 99 which is more than 100 and while the checking the diff the ans would be (1) and still the abs would make it (1)
    # and we check if the abs value of that diff is less than or equal to 10
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(90))
print(almost_there(150))
print(almost_there(209))

# FIND 33:

# Given a list of ints,
# return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

print("================================================================================================")
print("almost there")


def has_33(nums):
    # now we
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# PAPER DOLL:

# Given a string,
# return a string where for every character in the original there are three characters

# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

print("================================================================================================")
print("paper_Doll")


def paper_doll(text):
    # here we make a string 'ans' which is empty initially
    ans = ""
    # now we take every character from the text
    for char in text:
        # now we take the character and we multiply it by 3
        # eg. character is l
        #       char*3  ==> lll;
        # and now ans += char*3  ===> ans = ans + (char + char + char);
        # for every char this loop continues until it break
        ans += char * 3
    return ans


print(paper_doll("Hello"))


# BLACKJACK:

# Given three integers between 1 and 11,
# if their sum is less than or equal to 21,
# return their sum.
# If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally,
# if the sum (even after adjustment) exceeds 21,
# return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

print("================================================================================================")
print("black_jack")


def blackjack(a, b, c):
    # here we take 3 parameters or arguments
    # and sum them and store that value in var sum1
    sum1 = a + b + c
    # if sum1 == 21 or sum1 < 21
    # return sum1
    if sum1 <= 21:
        return sum1
    # if sum1 is more than 21 else bode block is activated
    else:
        # here we check if there's an 11 in one of numbers
        if a == 11 or b == 11 or c == 11:
            # if 'if' condition is true then we subtract 10 from sum1
            sum1 = sum1 - 10
            return sum1
        else:
            print("BUST")


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# SUMMER OF '69:

# Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6
# and extending to the next 9
# (every 6 will be followed by at least one 9).
# Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

print("================================================================================================")
print("summer_69")


def summer_69(arr):
    # here we take a var 'totalsum' and we assign it's value '0'
    totalsum = 0
    # here we make a condition TRUE
    # it helps in if and only if the condtion would be TRUE
    # then only code block is executed
    add = True

    # here 'arr' is a list data type
    # we select a number from 'arr' unitwise
    for num in arr:
        # here we put the conditon if it's True then only the while code block is executed
        while add:
            # if number is not equal to 6 then code block is executed
            if num != 6:
                # we take that num and add it to totalsum, which is initially 0;
                totalsum += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return totalsum


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


# SPY GAME:

# Write a function that takes in a list of integers
# and returns True if it contains 007 in order

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

print("================================================================================================")
print("spy_game")


def spy_game(myarr):

    # here we make a decoy list to cross check the numbers with the input list
    code = [0, 0, 7, "x"]

    # now we take every number from the input list
    for num in myarr:
        # we check if the unit number is as same as code[0] which is 0
        if num == code[0]:
            # if it is equal to 0 then we would use pop function on 'code' list
            # pop function removes the element from the list
            code.pop(0)
            # now when the code[0] is poped   =====   first 0 is poped
            # now when the code[0] is poped   =====   now next 0 is poped
            # now when the code[0] is poped   =====   now 7 is poped

    # len(code) == 1 is used to return a boolean value for the ans of this function
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


# COUNT PRIMES:

# Write a function that returns the number
# of prime numbers that exist up to and
# including a given number

# count_primes(100) --> 25
# By convention, 0 and 1 are not prime

print("New")
print("Count primes")


def prime_count(numb):
    # here we make a condition if the input number is 1 or less than 1
    # it would return 0
    if numb <= 1:
        return 0

    # now we make a var which is a list and the initial value set to it is 2
    prime = [2]

    # we take a var 'x' and set it's value to 3 initially
    x = 3

    # while 3 is less than equal to input numb, code block of while will be executed
    while x <= numb:

        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            prime.append(x)
            x += 2

    print(prime)
    return len(prime)


print(prime_count(100))


# Just for fun, not a real problem :)

# PRINT BIG:
# Write a function that takes in a single letter,
# and returns a 5x5 representation of that letter

# print_big('a')
#
# out:   *
#      * *
#     *****
#     *   *
#     *   *

# HINT:
# Consider making a dictionary of possible patterns,
# and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".

print("================================================================================================")
print("print_big")


def print_big(letter):

    patterns = {1: "  *  ", 2: " * * ", 3: "*   *", 4: "*****", 5: "**** ", 6: "   * ", 7: " *   ", 8: "*   * ", 9: "*    "}

    alphabet = {"A": [1, 2, 4, 3, 3], "B": [5, 3, 5, 3, 5], "C": [4, 9, 9, 9, 4], "D": [5, 3, 3, 3, 5], "E": [4, 9, 4, 9, 4]}

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print(print_big("e"))

