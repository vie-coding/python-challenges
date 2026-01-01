"""
Challenge 9: Majority Element
-----------------------------
Difficulty: ⭐⭐⭐⭐

TODO:
1. You are given a list of integers.
2. Find the element that appears MORE than N/2 times (majority element).
3. You may assume the majority element always exists.
4. Try to solve in O(n) time and O(1) space (without extra storage).
5. You CANNOT use Counter, sorting, or extra dictionaries for the optimal solution.

Example:
    Input: [3, 2, 3]
    Output: 3
    (3 appears 2 times, which is > 3/2 = 1.5)

    Input: [2, 2, 1, 1, 1, 2, 2]
    Output: 2
    (2 appears 4 times, which is > 7/2 = 3.5)

    Input: [1]
    Output: 1

    Input: [6, 6, 6, 7, 7]
    Output: 6
    (6 appears 3 times, which is > 5/2 = 2.5)

Hint: Use Boyer-Moore Voting Algorithm:
      1. Start with first element as candidate, count = 1
      2. For each next element:
         - If count is 0, set current element as new candidate
         - If element == candidate, increment count
         - If element != candidate, decrement count
      3. The candidate at the end is the majority element

      Why does this work? The majority element can "survive" all the cancellations.
"""

def main():
    # Test data
    nums = [2, 2, 1, 1, 1, 2, 2]

    count = 0
    element = -1
    
    for i in range(len(nums)):
        if count == 0:
            element = nums[i]
        else:
            if nums[i] == element:
                vote += 1
            else:
                vote -= 1
                
    counter = 0 
    for i in range(len(nums)):
        if nums[i] == element:
            counter += 1
    if counter > len(nums)//2:
        print("Output:", element)
    pass

if __name__ == '__main__':
    main()
