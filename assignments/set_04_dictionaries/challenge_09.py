"""
Challenge 9: Two Sum Problem with Dictionary
---------------------------------------------
Difficulty: ⭐⭐⭐⭐

TODO:
1. You are given a list of integers and a target sum.
2. Find TWO numbers in the list that add up to the target.
3. Return the INDICES of these two numbers.
4. Use a dictionary to solve this in a single pass (O(n) time).
5. You cannot use the same element twice.
6. If no solution exists, return None or [-1, -1].

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]
    Explanation: nums[1] + nums[2] = 2 + 4 = 6

    Input: nums = [3, 3], target = 6
    Output: [0, 1]

    Input: nums = [1, 2, 3], target = 10
    Output: [-1, -1] (or None)

Hint: As you iterate through the list, store each number and its index in a dictionary.
      For each number, check if (target - number) exists in the dictionary.
"""

def main():
    # Test data
    nums = [2, 7, 11, 15]
    target = 9

    # Write your code here
    pass

if __name__ == '__main__':
    main()
