"""
Challenge 6: Word Frequency Counter
------------------------------------
Difficulty: ⭐⭐⭐

TODO:
1. You are given a sentence (string).
2. Create a dictionary that counts how many times each word appears.
3. Words are case-insensitive (e.g., "The" and "the" are the same word).
4. Remove punctuation from words.
5. Print the dictionary sorted by frequency (highest first).
6. You CANNOT use Counter from collections.

Example:
    Input: "The quick brown fox jumps over the lazy dog"
    Output: {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}

    Input: "Hello hello HELLO world world"
    Output: {"hello": 3, "world": 2}

Hint: Use .lower() to make words lowercase. Use .split() to break the sentence into words.
      For sorting by value, you'll need to convert to a list of tuples, sort, then convert back.
"""

def main():
    # Test sentence
    sentence = "The quick brown fox jumps over the lazy dog"

    # Write your code here
    pass

if __name__ == '__main__':
    main()
