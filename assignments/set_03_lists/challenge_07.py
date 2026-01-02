"""
Challenge 7: Run Length Encoding
--------------------------------
Difficulty: ⭐⭐⭐⭐

TODO:
1. You are given a list of characters or integers.
2. Compress the list using Run Length Encoding (RLE).
3. Replace consecutive duplicates with [element, count].
4. Return a flattened list of elements and their counts.
5. Single elements (count = 1) should still show the count.

Example:
    Input: ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c']
    Output: ['a', 3, 'b', 2, 'c', 4]

    Input: [1, 1, 1, 2, 2, 3]
    Output: [1, 3, 2, 2, 3, 1]

    Input: ['a', 'b', 'c']
    Output: ['a', 1, 'b', 1, 'c', 1]

    Input: [5, 5, 5, 5, 5]
    Output: [5, 5]

    Input: []
    Output: []

Hint: Track the current element and its count.
      When the element changes, add [element, count] to result.
      Don't forget to add the last group after the loop!
"""

def main():
    # Test data
	data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c']
	data2 = []

    # Write your code here
	count = 1
	

	for i in range(1,len(data)):
		j = i - 1
		if data[i] == data[j]:
			count += 1
		else:
			data2.append(data[j])
			data2.append(count)
			count = 1 
		if i == len(data) - 1:
			data2.append(data[i])
			data2.append(count)	
			
	print("Output:" , data2)




if __name__ == '__main__':
    main()
