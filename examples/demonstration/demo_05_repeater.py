"""
Demo 5: Text Repeater
---------------------
TODO:
1. Ask the user for a word.
2. Ask the user for a number (how many times to repeat).
3. Print the word that many times (you can use a loop or string multiplication).

Example:
    Input Word: Echo
    Input Count: 3
    Output: EchoEchoEcho
"""

def main():
    # Write your code here
    word = input("Enter a word: ")
    count = int(input("Enter a number: "))
    print(word * count)
    pass

if __name__ == '__main__':
    main()
