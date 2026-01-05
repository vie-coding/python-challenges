"""
Challenge 1: Count Up
---------------------
TODO:
1. Ask the user to enter a positive integer N.
2. Print all numbers from 1 to N (inclusive), each on a new line.
3. If N is less than 1, print "invalid".

Example:
    Input: 5
    Output:
    1
    2
    3
    4
    5
"""

def main():
    x = int(input("Input:"))
    print("Output:")
    if x < 1:
        print("invalid")
    else:
        for i in range(1, x + 1):
            print(i)




    pass

if __name__ == '__main__':
    main()
