# While loops will continueto execute a block of code while somecondition remains true

# syntax of while loop

# while some_boolean_condition:
# do something

# we can also combine while and else

# while some_boolean_condition:
# dosomething
# else:
# do something different

# new

x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1

# this will print
# The current value of x is 0
# The current value of x is 1
# The current value of x is 2
# The current value of x is 3
# The current value of x is 4

print("\n================================================================================================\n")

# new

# we can also use while .....  else

x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1

else:
    print(f"The current value of x is {x} which is more than or equal to 5")
