"""
Challenge 5: Shipping Cost
--------------------------
TODO:
1. Ask the user to enter the weight of a package in kg (float).
2. If the weight is 0 or less, print "invalid".
3. Calculate the shipping cost based on these brackets:
   - Weight > 0 up to 1 kg:    $50
   - Weight > 1 up to 5 kg:    $80
   - Weight > 5 up to 20 kg:   $150
   - Weight > 20 kg:           $250
4. Print the final cost.

Example:
    Input: 2.5
    Output: 80
"""

def main():
    # Write your code here
    kg = float(input())

    if kg < 0:
        print("invalid")

    elif 0 < kg <= 1:
        print("$50")
    elif 1 < kg <= 5:
        print("$80")
    elif 5 < kg <= 20:
        print("$150")
    else:
        print("$250")

    pass

if __name__ == '__main__':
    main()