# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this caseWrite a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def countBits(n):
    binary_str = "{0:b}".format(n)
    i = 0
    for each in binary_str:
        if each == '1':
            i += 1
    return i

print(countBits(37))
    