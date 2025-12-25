"""
Challenge 4: Find the Missing Number
------------------------------------
Difficulty: ⭐⭐⭐

TODO:
1. You are given a list containing N distinct numbers from 0 to N.
2. One number in the range is MISSING.
3. Find and print the missing number.
4. You CANNOT sort the list.
5. Try to solve it in O(n) time - single pass through the list.

Example:
    Input: [3, 0, 1]
    Range is 0-3, so numbers should be: 0, 1, 2, 3
    Output: 2 (missing!)

    Input: [0, 1]
    Range is 0-2
    Output: 2

    Input: [9, 6, 4, 2, 3, 5, 7, 0, 1]
    Range is 0-9
    Output: 8

    Input: [1]
    Range is 0-1
    Output: 0

Hint: Mathematical approach - what's the sum of 0 to N?
      Formula: N * (N + 1) / 2
      Compare expected sum with actual sum.
      The difference is the missing number!
"""

def main():
    # Test data
    numbers = [3, 0, 1]  # Missing: 2

    # Write your code here
    pass

if __name__ == '__main__':
    main()
