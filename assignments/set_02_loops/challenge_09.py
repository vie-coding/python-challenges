"""
Challenge 9: Prime Checker
-------------------------
TODO:
1. Ask the user to enter an integer N greater than 1.
2. Determine if N is a prime number.
3. Print "True" if N is prime, "False" if it is not.
4. If N is less than 2, print "invalid".
5. Remember: A prime number is only divisible by 1 and itself.

Example:
    Input: 7
    Output: True

    Input: 10
    Output: False

    Input: 2
    Output: True
"""

def main():
    x = int(input())
    counter = 0
    if x < 2:
        print("invalid")
    else :
        for i in range(2, x):
            if x % i == 0:
                counter += 1
        if counter != 0:
            print("Not a prime")
        else:
            print("Prime")
              

if __name__ == '__main__':
    main()
