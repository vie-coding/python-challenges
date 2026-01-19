"""
Challenge 8: Nested Dictionary - Student Records
-------------------------------------------------
Difficulty: ⭐⭐⭐

TODO:
1. Create a nested dictionary to store student records.
2. Each student has: name, age, grades (list of 3 subjects), and attendance (%).
3. Add at least 3 students.
4. Calculate and print the average grade for each student.
5. Find and print the student with the highest attendance.
6. Find and print the student with the highest average grade.

Example Structure:
    students = {
        "S001": {
            "name": "Alice",
            "age": 20,
            "grades": [85, 90, 88],
            "attendance": 95
        },
        "S002": {
            "name": "Bob",
            "age": 21,
            "grades": [78, 82, 80],
            "attendance": 88
        }
    }

Example Output:
    Alice's average: 87.67
    Bob's average: 80.00
    Highest attendance: Alice (95%)
    Highest average grade: Alice (87.67)

Hint: Use nested loops to access inner dictionary values.
"""

def main():
    # Write your code here
    students = {
        "S001": {
            "name": "Alice",
            "age": 20,
            "grades": [85, 90, 88],
            "attendance": 95
        },
        "S002": {
            "name": "Bob",
            "age": 21,
            "grades": [78, 82, 80],
            "attendance": 88
        },
         "S003":{
         "name":"Stacy",
         "age": 18,
         "grades":[91, 92, 93],
         "attendance":99

         }
    }

    sum = 0 
    u = students["S001"]["attendance"] 
    attendance =[]

    for i in students:
        for x in students[i]["grades"]:
            t = len(students[i]["grades"])
            sum += x
        ave = sum/t
        attendance.append(ave)
        print(ave)
        sum = 0
      
        if students[i]["attendance"] > u:
            u = students[i]["attendance"]
            
    attendance.sort()       
    
    print(u)       
    print(attendance[len(attendance)-1])
            
        
        
            
    pass

if __name__ == '__main__':
    main()
