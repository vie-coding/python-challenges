"""
Challenge 1: Second Largest Element
-----------------------------------
Difficulty: ⭐⭐

TODO:
1. You are given a list of integers.
2. Find the SECOND LARGEST element in the list.
3. You CANNOT use sort(), sorted(), max(), or min() functions.
4. If the list has less than 2 unique elements, print "invalid".
5. Print the second largest number.

Rules:
- Must handle duplicates (e.g., [5, 5, 5, 3] → second largest is 3)
- Must work with negative numbers
- Cannot use built-in sorting or max/min functions

Example:
    Input: [10, 5, 8, 20, 15]
    Output: 15

    Input: [5, 5, 5, 5]
    Output: invalid

    Input: [1, 2]
    Output: 1

    Input: [-5, -2, -10, -1]
    Output: -2

Hint: Think about tracking two variables - the largest and second largest.
      Update them as you iterate through the list.
"""

def main():
    # Test list - you can modify this for testing
    numbers = [10, 5, 8, 20, 15]

    # Write your code here
        if len(numbers) == 0:
            return -1
    max_num = numbers[0]

    for i in numbers:
        if i > max_num:
            max_num = i

    for i in numbers:
        if i  == max_num:  
            numbers.remove(i)

    sec_max = numbers[0]
    for i in numbers:
        if i > sec_max:
            sec_max = i
    
    print("Output:" , sec_max)
    pass

if __name__ == '__main__':
    main()
