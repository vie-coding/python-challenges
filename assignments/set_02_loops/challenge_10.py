"""
Challenge 10: Pyramid Pattern
-----------------------------
TODO:
1. Ask the user to enter a positive integer N (height of pyramid).
2. Print a pyramid pattern of stars (*) with N rows.
3. Each row should be centered with spaces.
4. Row i should have (2*i - 1) stars.
5. If N is less than 1, print "invalid".

Example:
    Input: 4
    Output:
       *
      ***
     *****
    *******

    Input: 3
    Output:
      *
     ***
    *****

Hint: For row i (1 to N):
- Print (N - i) spaces
- Print (2 * i - 1) stars
"""

def main():
    x = int(input())
    if x < 1:
        print("invalid")
    else:
        for i in range(1, x + 1):
            print(" " * (x - i) + "*" * (2 * i - 1))
    pass

if __name__ == '__main__':
    main()
