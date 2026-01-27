"""
Challenge 1: Create a Student Grade Dictionary
-----------------------------------------------
Difficulty: ⭐

TODO:
1. Create a dictionary to store student names as keys and their grades as values.
2. Add at least 5 students with their grades (0-100).
3. Print the entire dictionary.
4. Print a specific student's grade.
5. Update one student's grade.
6. Print the updated dictionary.

Example:
    students = {"Alice": 85, "Bob": 92, "Charlie": 78}

    Output:
    All students: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    Bob's grade: 92
    After update: {'Alice': 90, 'Bob': 92, 'Charlie': 78}

Hint: Use dictionary[key] to access values and dictionary[key] = value to update.
"""

def main():
    # Write your code here
    grades = {
        "Alice" : 85,
        "Bob" : 92,
    "Charlie" : 90,
    "Stacy" : 99,
    "Sarah" : 100
        
    }
    print("Output:")
    print("All students:",grades)
    grades["Charlie"] = 75
    print("Charlie's grade: 75")
    print(" After update:", grades)

    print(grades)

if __name
