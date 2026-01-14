"""
Challenge 7: Group Anagrams
----------------------------
Difficulty: ⭐⭐⭐

TODO:
1. You are given a list of words.
2. Group all anagrams together using a dictionary.
3. Anagrams are words that contain the same letters in different order.
4. Return a dictionary where keys are sorted letters and values are lists of anagrams.
5. Print each group of anagrams.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output:
    {
        "aet": ["eat", "tea", "ate"],
        "ant": ["tan", "nat"],
        "abt": ["bat"]
    }

    Input: ["listen", "silent", "hello", "world"]
    Output:
    {
        "eilnst": ["listen", "silent"],
        "ehllo": ["hello"],
        "dlorw": ["world"]
    }

Hint: For each word, sort its letters to create a key. Use this key to group anagrams.
      You can use sorted() on a string to get sorted letters.
"""

def main():
    # Test list
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    # Write your code here
    pass

if __name__ == '__main__':
    main()
