# We normally execute our code and sometimes we get an error But what if you could leave warning marks for yourself before error line

# Python debugger module helps you in that

# Let's see an example without debugger first

x = [1, 2, 3]
y = 2
z = 3

result_1 = y + z
print(result_1)

# result_2 = x + y
# print(result_2)

# It returns a type error cannot concatenate list with integers

# Now let's import debugger

import pdb

x = [1, 2, 3]
y = 2
z = 3

result_1 = y + z
print(result_1)

# Now we know where the error line is so we place the python debugger trace the error before it. Because it lets you check variables and operations amidst the execution of the script

pdb.set_trace()

result_2 = x + y

print(result_2)

# When executed it will give us a small interactive window in the cosole where wecan check the value of the integers and perform operations on it also

# In order to quit it we can enter q and it will quit
