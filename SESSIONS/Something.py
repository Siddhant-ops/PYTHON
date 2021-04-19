def crate(n, initial):
    print(
        f"There are {n-initial} mongoes more"
        if n > initial
        else f"There are {initial-n} mongoes less"
        if (initial > n)
        else f"Number of mangoes is equal to Number of mangoes from User"
    )


crate(10, 30)
crate(40, 30)
crate(30, 30)

