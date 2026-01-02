"""
Challenge 8: Two Sum
--------------------
Difficulty: ⭐⭐⭐⭐

TODO:
1. You are given a list of integers and a target sum.
2. Find TWO numbers in the list that add up to the target.
3. Return the INDICES of those two numbers.
4. Each input has exactly ONE solution.
5. You cannot use the same element twice.
6. Try to solve in O(n) time, not O(n^2).

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    (Because nums[0] + nums[1] = 2 + 7 = 9)

    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]
    (Because nums[1] + nums[2] = 2 + 4 = 6)

    Input: nums = [3, 3], target = 6
    Output: [0, 1]

    Input: nums = [1, 5, 3, 8, 2], target = 10
    Output: [1, 4] or [4, 1]
    (Because 5 + 2 = 10... wait, that's 7. Let me recalc: 5 + 8 = 13, 3 + 8 = 11, 8 + 2 = 10)
    Output: [3, 4]

Hint: Use a dictionary to store numbers you've seen.
      For each number, check if (target - number) exists in the dictionary.
      Key = number, Value = index
"""

def main():
    # Test data
    nums = [2, 7, 11, 15]
    target = 9

    # Write your code here

    for i in nums:
        diff = target - i
        if diff in nums:
            print("Output: [", i ,',', diff, "]")
            break 
    pass

if __name__ == '__main__':
    main()
