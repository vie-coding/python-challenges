"""
Challenge 4: Find Key with Maximum Value
-----------------------------------------
Difficulty: ⭐⭐

TODO:
1. You are given a dictionary with string keys and integer values.
2. Find and print the key that has the maximum value.
3. You CANNOT use the max() function.
4. If multiple keys have the same maximum value, return any one of them.

Example:
    Input: {"apple": 5, "banana": 8, "cherry": 3, "date": 8}
    Output: "banana" (or "date")

    Input: {"x": 100, "y": 50, "z": 75}
    Output: "x"

    Input: {"a": -5, "b": -10, "c": -2}
    Output: "c"

Hint: Keep track of the maximum value and its corresponding key as you iterate.
"""

def main():
    # Test dictionary
    scores = {"apple": 5, "banana": 8, "cherry": 3, "date": 8}
    x = scores["apple"]

    for i in scores.values():
        if i > x:
            x = i
    for i in scores:
        if scores[i] == x:
            print("Output:",i)
            break
    # Write your code her
    pass

if __name__ == '__main__':
    main()
