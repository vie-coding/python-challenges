"""
Challenge 2: Count Character Frequency
---------------------------------------
Difficulty: ⭐⭐

TODO:
1. You are given a string.
2. Create a dictionary that counts the frequency of each character.
3. You CANNOT use Counter from collections.
4. Print the dictionary showing each character and its count.
5. Ignore spaces in the count.

Example:
    Input: "hello world"
    Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

    Input: "programming"
    Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

Hint: Loop through each character. If it's already in the dictionary, increment its count.
      Otherwise, add it with a count of 1.
"""

def main():
    # Test string
    text = "hello world"

    thisdict = {
    }

    for i in text:
        if i == ' ':
            continue
        if i in thisdict:
            thisdict[i] += 1
        else:
            thisdict[i] = 1
            
        print("Output:" , thisdict)
            
        

    # Write your code here
    pass

if __name__ == '__main__':
    main()
