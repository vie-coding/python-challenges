"""
Challenge 3: Merge Two Sorted Lists
-----------------------------------
Difficulty: ⭐⭐⭐

TODO:
1. You are given TWO lists that are already sorted in ascending order.
2. Merge them into ONE sorted list (also ascending).
3. You CANNOT use sort(), sorted(), or any built-in sorting.
4. The result must be sorted without using sort after merging.
5. Print the merged sorted list.

Example:
    Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]

    Input: list1 = [1, 2, 8, 10], list2 = [3, 5, 7]
    Output: [1, 2, 3, 5, 7, 8, 10]

    Input: list1 = [], list2 = [1, 2, 3]
    Output: [1, 2, 3]

    Input: list1 = [5], list2 = [1]
    Output: [1, 5]

Hint: Use two pointers, one for each list.
      Compare elements at both pointers.
      Add the smaller one to the result and move that pointer forward.
      Continue until both lists are exhausted.
"""

def main():
    # Test data
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]

    # Write your code here
    
    list3 = []
    for i in list1:
        list3.append(i)

    for x in list2:
        list3.append(x)
    
    for i in range(1,len(list3)):
        j =  i - 1
        while(j >= 0 and list3[j + 1] < list3[j]):
            list3[j] , list3[j + 1] = list3[j + 1] , list3[j]
            j -= 1
    print("Output:" , list3)
    pass


if __name__ == '__main__':
    main()
