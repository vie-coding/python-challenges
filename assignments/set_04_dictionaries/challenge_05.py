"""
Challenge 5: Invert a Dictionary
---------------------------------
Difficulty: ⭐⭐

TODO:
1. You are given a dictionary with unique values.
2. Create a new dictionary where keys become values and values become keys.
3. Print the inverted dictionary.
4. You CANNOT use dictionary comprehension.

Example:
    Input: {"a": 1, "b": 2, "c": 3}
    Output: {1: "a", 2: "b", 3: "c"}

    Input: {"name": "Alice", "age": "25", "city": "NYC"}
    Output: {"Alice": "name", "25": "age", "NYC": "city"}

Hint: Create an empty dictionary and loop through the original dictionary's items.
"""

def main():
    # Test dictionary
    original = {"a": 1, "b": 2, "c": 3}

    reverted = {
    }

    for i in original:
        reverted[original[i]] = i

    print(reverted)

    # Write your code here
    pass

if __name__ == '__main__':
    main()
