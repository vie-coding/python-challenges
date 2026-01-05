"""
Challenge 2: Countdown
---------------------
TODO:
1. Ask the user to enter a positive integer N.
2. Print all numbers from N down to 1 (inclusive), each on a new line.
3. If N is less than 1, print "invalid".

Example:
    Input: 5
    Output:
    5
    4
    3
    2
    1
"""

def main():
     x = int(input("Input:"))
    print("Output:")

    if x < 1:
        print("invalid")
    else:
        for i in range(x, 0, -1):
            print(i)



if __name__ == '__main__':
    main()
