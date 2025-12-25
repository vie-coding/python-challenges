"""
Challenge 6: List Intersection
------------------------------
Difficulty: ⭐⭐⭐

TODO:
1. You are given TWO lists of integers.
2. Find all elements that appear in BOTH lists (intersection).
3. Each element in the result should appear as many times as it
   shows in both lists (handle duplicates properly).
4. You CANNOT use set() or any set operations.
5. Print the intersection list.

Example:
    Input: list1 = [1, 2, 2, 1], list2 = [2, 2]
    Output: [2, 2]
    (2 appears twice in both, so include it twice)

    Input: list1 = [4, 9, 5], list2 = [9, 4, 9, 8, 4]
    Output: [4, 9] or [9, 4]
    (Order doesn't matter)

    Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
    Output: []

    Input: list1 = [1, 1, 1, 2], list2 = [1, 1]
    Output: [1, 1]
    (Only 2 ones are common)

Hint: Use a frequency counter (dictionary) for one list.
      Then iterate through the second list and check if elements
      exist in the counter. Decrease the count when found.
"""

def main():
    # Test data
    list1 = [1, 2, 2, 1]
    list2 = [2, 2]

    # Write your code here
    pass

if __name__ == '__main__':
    main()
