"""
Challenge 6: Power Calculator
-----------------------------
TODO:
1. Ask the user to enter a base (integer).
2. Ask the user to enter an exponent (non-negative integer).
3. Calculate base^exponent WITHOUT using the ** operator or pow() function.
4. Print the result.
5. If exponent is negative, print "invalid".

Example:
    Input: 2, 3
    Output: 8
    (Because 2^3 = 2 × 2 × 2 = 8)

    Input: 5, 0
    Output: 1
    (Because any number to the power of 0 is 1)
"""

def main():
    base = int(input())
    exponent = int(input())
    result = 1
    if exponent < 0:
        print("invalid")
    else:
        for i in range(exponent):
            result *= base
        print(result)

if __name__ == '__main__':
    main()
