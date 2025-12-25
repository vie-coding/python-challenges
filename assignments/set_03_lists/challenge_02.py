"""
Challenge 2: Rotate List
------------------------
Difficulty: ⭐⭐⭐

TODO:
1. You are given a list of integers and a number K.
2. Rotate the list to the RIGHT by K positions.
3. The last K elements move to the front.
4. If K is negative, rotate LEFT instead.
5. If K is larger than the list length, wrap around (use modulo).
6. Print the rotated list.

Example:
    Input: [1, 2, 3, 4, 5], K = 2
    Output: [4, 5, 1, 2, 3]
    (Last 2 elements [4, 5] moved to front)

    Input: [1, 2, 3, 4, 5], K = -1
    Output: [2, 3, 4, 5, 1]
    (Rotated left by 1)

    Input: [1, 2, 3], K = 5
    Output: [2, 3, 1]
    (K=5 is same as K=2 for length 3, since 5 % 3 = 2)

    Input: [], K = 3
    Output: []

Hint: Think about slicing. If you rotate right by K:
      - Take the last K elements
      - Take the first (length - K) elements
      - Combine them
"""

def main():
    # Test data
    numbers = [1, 2, 3, 4, 5]
    k = 2

    # Write your code here
    pass

if __name__ == '__main__':
    main()
