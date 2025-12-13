"""
Challenge 1: Number Sign + Parity
---------------------------------
TODO:
1. Ask the user to enter an integer.
2. Determine if the number is 'positive', 'negative', or 'zero'.
3. Determine if the number is 'even' or 'odd' (0 counts as even).
4. Print the two descriptions separated by a space.

Example:
    Input: -3
    Output: negative odd
"""

def main():
    value  = int(input("Input:"))

    if value % 2 == 0:
        if value >= 0:
            print("Output: even postive")
        else:
            print("Output: even and negative")

    else:
        if value < 0:
            print("Output: odd and negative")
        else:
            print("Output: odd and positive")

    
    pass

if __name__ == '__main__':
    main()