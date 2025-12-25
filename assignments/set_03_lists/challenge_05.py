"""
Challenge 5: Remove All Occurrences
-----------------------------------
Difficulty: ⭐⭐⭐

TODO:
1. You are given a list of integers and a target value.
2. Remove ALL occurrences of the target from the list.
3. You must modify the list IN-PLACE (don't create a new list).
4. Return/print the new length and the modified list.
5. You CANNOT use remove(), pop(), or list comprehension.

Example:
    Input: nums = [3, 2, 2, 3, 4, 3, 5], target = 3
    Output: length = 4, nums = [2, 2, 4, 5, ...]
    (First 4 elements are the answer, rest doesn't matter)

    Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], target = 2
    Output: length = 5, nums = [0, 1, 3, 0, 4, ...]

    Input: nums = [1, 1, 1], target = 1
    Output: length = 0, nums = [...]

Hint: Use two pointers technique.
      - One pointer (i) iterates through the list
      - Another pointer (k) tracks where to place non-target elements
      When you find a non-target element, place it at position k and increment k.
"""

def main():
    # Test data
    nums = [3, 2, 2, 3, 4, 3, 5]
    target = 3

    # Write your code here
    pass

if __name__ == '__main__':
    main()
