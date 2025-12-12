"""
Demo 2: Simple Calculator (Adder)
---------------------------------
TODO:
1. Ask the user for the first number (integer).
2. Ask the user for the second number (integer).
3. Add them together.
4. Print the result.

Example:
    Input 1: 5
    Input 2: 10
    Output: 15
"""

def main():
    # Write your code here
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))

    sum = number1 + number2

    print(f"Input 1: {number1}")
    print(f"Input 2: {number2}")
    print(f"Output: {sum}")
    pass

if __name__ == '__main__':
    main()
