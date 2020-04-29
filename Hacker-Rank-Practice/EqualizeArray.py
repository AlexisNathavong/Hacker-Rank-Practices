#!/bin/python3
​
import math
import os
import random
import re
import sys
​
​
#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
​
def equalizeArray(arr):

    # Set the count to zero as a starting point to count the equal elements from the given array.
    count = 0
    
    # Created an elements dictionary to store the key value pairs from the array given. 
    Elements = {}
	
	# Looping through the array to find all the numbers are equal to each other.
    for i in arr:
		
		# If the index is not in the array.
        if i not in Elements:
			
			# Iterate over the array again, starting with the next index.
            for j in arr:
				
				# If both indexes are the same.
                if i == j:
					
					# Then counts all the similar elements
                    count= count+1
					
			# and sets the value of that key as the count.
            Elements[i] = count
            count = 0
    # Where Elements is the dictionary and we use max() to find out the key with the largest value.           
    max_val = max(Elements, key= Elements.get)
	
    # Return the value of the key and subtract the value from the length of the original array.
	# Determine the fewest number of elements to delete.
    return (len(arr) - Elements[max_val])
​
​
# Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. Determine the fewest number of elements to delete to reach his goal.
# For example, if his array is , arr=[1,2,2,3] we see that he can delete the 2 elements 1 and 3 leaving arr=[2,2] . He could also delete both twos and either the 1 or the 3, but that would take 3 deletions. The minimum number of deletions is 2.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
​
    arr_count = int(input().strip())
​
    arr = []
​
    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)
​
    result = equalizeArray(arr)
​
    fptr.write(str(result) + '\n')
​
    fptr.close()