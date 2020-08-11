# This is Loop Controling Statements
#break: Breaks out of th current closest enclosing loop
#continue: Goes to the top of the closest enclosing loop
#pass: Does nothing at all

x = [1,2,3,4,5,6,7,8,9];
a = 2;
b = 5;
c = 8;

for i in x:
    if i == a:
        continue;
    elif i == b:
        pass;
    elif i == c:
        break;
    else:
        print(i);