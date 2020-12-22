sum=0
n=int(input("Enetr : "))
while(n ==0):
    sum = sum + int(n %10)
    n = n//10
print(sum)