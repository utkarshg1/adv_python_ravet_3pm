# This is a program to calculate simple intrest


def simple_intrest(p, n, r):
    """This function calulates simple intrest and amount"""
    i = (p * n * r) / 100
    a = p + i
    return i, a


# Take p, n, r as input from user
p = float(input("Please enter Principal in INR : "))
n = int(input("Please enter number of years : "))
r = float(input("Please enter rate of Intrest in %p.a. : "))

# Call simple intrest function
i, a = simple_intrest(p, n, r)

# Show the final results
print(f"Simple Intrest : {i:.2f} INR")
print(f"Amount : {a:.2f} INR")
