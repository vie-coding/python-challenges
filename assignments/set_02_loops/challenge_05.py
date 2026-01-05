"""
Challenge 5: Even Numbers
------------------------
TODO:
1. Ask the user to enter a positive integer N.
2. Print all even numbers from 1 to N (inclusive), each on a new line.
3. If N is less than 1, print "invalid".
4. If there are no even numbers in the range, print nothing (besides potentially "invalid").

Example:
    Input: 10
    Output:
    2
    4
    6
    8
    10
"""

def main():
    x = int(input("Input:"))
    print("Output:)
    if x < 1:
        print("invalid")
        return
    for i in range(1, x + 1):
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    main()
