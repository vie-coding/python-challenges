"""
Challenge 7: Digit Counter
-------------------------
TODO:
1. Ask the user to enter an integer N (can be negative).
2. Count how many digits are in N.
3. Print the count.
4. Note: Negative sign doesn't count as a digit.

Example:
    Input: 12345
    Output: 5

    Input: -456
    Output: 3

    Input: 0
    Output: 1
"""

def main():
    x = int(input())
    count = 0
    for i in str(x):
        count += 1
    print(count)

if __name__ == '__main__':
    main()
