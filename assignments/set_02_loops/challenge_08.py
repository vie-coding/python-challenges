"""
Challenge 8: FizzBuzz
--------------------
TODO:
1. Ask the user to enter a positive integer N.
2. For each number from 1 to N (inclusive), print:
   - "Fizz" if the number is divisible by 3
   - "Buzz" if the number is divisible by 5
   - "FizzBuzz" if the number is divisible by both 3 and 5
   - The number itself if none of the above conditions are met
3. Each output should be on a new line.
4. If N is less than 1, print "invalid".

Example:
    Input: 15
    Output:
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
"""

def main():
    x = int(input())
    if x < 1:
        print("invalid")
    else:
        for i in range(1, x + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

if __name__ == '__main__':
    main()
