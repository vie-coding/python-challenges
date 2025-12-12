"""
Demo 4: Traffic Light
---------------------
TODO:
1. Ask the user for the color of the light ("red", "yellow", "green").
2. Check the color:
   - If "red", print "Stop!"
   - If "yellow", print "Slow down."
   - If "green", print "Go!"
   - If anything else, print "Invalid color."

Example:
    Input: red
    Output: Stop!
"""

def main():
    # Write your code here
    color = input("Enter the color of the light: ")
    if color == "red":
        print("Stop!")
    elif color == "yellow":
        print("Slow down.")
    elif color == "green":
        print("Go!")
    else:
        print("Invalid color.")
    pass

if __name__ == '__main__':
    main()
