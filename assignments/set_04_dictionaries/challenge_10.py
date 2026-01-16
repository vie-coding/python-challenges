"""
Challenge 10: Dictionary from Two Lists (Zip Without Zip)
----------------------------------------------------------
Difficulty: ⭐⭐⭐

TODO:
1. You are given two lists of equal length.
2. Create a dictionary where elements from the first list are keys.
3. Elements from the second list are values.
4. You CANNOT use the zip() function or dictionary comprehension.
5. If lists have different lengths, use the length of the shorter list.
6. Print the resulting dictionary.

Example:
    Input:
    keys = ["name", "age", "city", "country"]
    values = ["Alice", 25, "NYC", "USA"]

    Output:
    {"name": "Alice", "age": 25, "city": "NYC", "country": "USA"}

    Input:
    keys = ["a", "b", "c", "d"]
    values = [1, 2, 3]

    Output:
    {"a": 1, "b": 2, "c": 3}

    Input:
    keys = [1, 2, 3]
    values = [10, 20, 30, 40]

    Output:
    {1: 10, 2: 20, 3: 30}

Hint: Use a loop with range() and the minimum length of both lists.
"""

def main():
    # Test lists
    keys = ["name", "age", "city", "country"]
    values = ["Alice", 25, "NYC", "USA"]

    # Write your code here
    pass

if __name__ == '__main__':
    main()
