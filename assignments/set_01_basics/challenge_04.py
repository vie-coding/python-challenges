"""
Challenge 4: Triangle Validator
-------------------------------
TODO:
1. Ask the user to enter three numbers (can be floats) representing the sides of a triangle (a, b, c).
2. Check if the sides form a valid triangle. To be valid, the sum of any two sides must be strictly greater than the third side:
   - (a + b > c) AND (a + c > b) AND (b + c > a)
3. If valid, check the type:
   - Equilateral: All three sides are equal.
   - Isosceles: Exactly two sides are equal.
   - Scalene: No sides are equal.
4. If not valid (or any side is <= 0), print "invalid".
5. Otherwise, print the type ("equilateral", "isosceles", or "scalene").

Example:
    Input: 3, 3, 5
    Output: isosceles
"""

def main():
    # Write your code here
    a = float(input())
    b = float(input())
    c = float(input())
    if a <= 0 or b <= 0 or c <= 0:
        print("invalid")
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("valid triangle")
        if a == b and a == c and b == c:
            print("equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        else:
            print ("scalene")
    else:
        print("invalid")
    pass

if __name__ == '__main__':
    main()