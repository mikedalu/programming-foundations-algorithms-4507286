# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    # while b != 0:
    #     if a % b == 0:
    #         return b
    #     else:
    #         r = a % b
    #         a = b
    #         b = r
    if a % b == 0:
        return b
    r = a % b;
    a = b
    b = r
    return gcd(a, b)


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
