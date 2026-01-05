"""
Challenge 3: Sum to N
--------------------
TODO:
1. Ask the user to enter a positive integer N.
2. Calculate the sum of all numbers from 1 to N (inclusive).
3. Print the result.
4. If N is less than 1, print "invalid".

Example:
    Input: 5
    Output: 15
    (Because 1 + 2 + 3 + 4 + 5 = 15)
"""

def main():
     x = int(input("Input:"))
    
    sum = 0 

    if x < 0 :
        print("invalid")

    else:
        for i in range(1, x + 1):
            sum += i
        print("Output:",sum)



if __name__ == '__main__':
    main()
