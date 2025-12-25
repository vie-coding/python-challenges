"""
Challenge 10: Maximum Subarray Sum (Kadane's Algorithm)
-------------------------------------------------------
Difficulty: ⭐⭐⭐⭐⭐

TODO:
1. You are given a list of integers (can include negatives).
2. Find the CONTIGUOUS subarray with the LARGEST sum.
3. Return the maximum sum.
4. The subarray must contain at least one element.
5. Solve in O(n) time - single pass through the list.

Example:
    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    (The subarray [4, -1, 2, 1] has the largest sum = 6)

    Input: [1]
    Output: 1

    Input: [5, 4, -1, 7, 8]
    Output: 23
    (The entire array is the subarray with max sum)

    Input: [-1]
    Output: -1
    (Must include at least one element)

    Input: [-2, -1, -3]
    Output: -1
    (Best we can do with all negatives)

Hint: Kadane's Algorithm:
      1. Track current_sum and max_sum
      2. For each element:
         - current_sum = max(element, current_sum + element)
           (Either start fresh with this element, or extend the previous subarray)
         - max_sum = max(max_sum, current_sum)
      3. Return max_sum

      The key insight: If adding a number makes current_sum negative,
      it's better to start fresh from the next number.

BONUS CHALLENGE:
Also print the start and end indices of the maximum subarray!
    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: sum = 6, indices = [3, 6] (subarray from index 3 to 6)
"""

def main():
    # Test data
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # Write your code here
    pass

if __name__ == '__main__':
    main()
