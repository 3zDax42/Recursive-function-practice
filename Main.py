def factorial (n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)
def starpattern(stars):
    if stars > 0:
        for i in range(stars,0,-1):
            print("*", end = " ")
        print()
        return starpattern(stars-1)

print(factorial (5))
starpattern(5)
# you told micheal to help me understand question 2 and I did not get help
