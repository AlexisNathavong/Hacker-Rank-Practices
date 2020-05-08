#!/bin/python3

import math
import os
import random
import re
import sys

# PROBLEM NOTES:
    # Query 1: inserting a number, x, into the list
    # Query 2: deleting 1 occurence of a number, y, from the list (if present)
    # Query 3: Check if any number is present whose frequency is exactly z (meaning check for a duplicate number), if yes print '1', if not, print '0'
    # Return an array of 0s and 1s

## START HERE ###
# HIGH LEVEL PROBLEM EXPLANATION:
    # Given a list of queries, where each query is in the form of x and y values. There are 3 different types of queries: Insertion, deleteion, and reoccurance. The goal is to check if any number is present whose frequency is exactly the given number of reoccurance. If it is, print 1, if not, print 0. Then we return the list of 0s and 1s.


# HIGH LEVEL SOLUTION:
    # ​Look through the queries list, checking if the 1st index for each query is a 1, 2, or 3. If it is a 1, then we add the value in the 1st dictionary, and add the value for the given key in the 2nd dictionary. If it is a 2, remove the value in the 1st dictionary and remove the value for the given key in the 2nd dictionary. If it is a 3, check if the key of the 2nd dictionary is present and if the value is greater than 0, add a 1 to the results list, otherwise add 0 to the results list.  Return the results list.

# SOLUTION:
    # Step 1: Create a frequency dictionary to track the key value pairs of the frequencies of each number
    # Step 2: Create an empty list for storage, called results to be returned
    # Step 3: Create a second frequency dictionary to keep track of how many times each key of the 1st dictionary appears
    # Step 4: Loop through queries list
    # Step 5: Check if the x axis(1st index) in the query is set to 1, if it is, increment the value if it exists in the 1st dictionary (frequency), and increment the value for the given key in the 2nd dictionary (frequencyValues)
    # Step 6: Check if the x axis element in the query is set to 2, if it is, decrement the value, if it exists, in the 1st dictionary (frequency) setting to 0 so it can't go to a negative integer, and decrement the value for the given key in the 2nd dictionary (frequencyValues)
    # Step 7: Check if the x axis element in the query is set to 3, if it is, check if the key of the 2nd dictionary is present and if it is, check its value to see if it is greater than 0, if it is, add 1 to the results array, otherwise add 0 to the results array.
    # Step 8: Return the results array.

# The Runtime: O(n) because the for loop is linear and the if statements are constants. 
# The for loop is O(n) and each if statements are O(1). 

def frequencyQueries(queries):
    # Create a frequency dictionary to track the key value pairs of the frequencies of each number
    frequency = {}
    # Create an empty list for storage, called results to be returned
    results = []
    # Create a second frequency dictionary to keep track of how many times each key of the 1st dictionary appears
    frequencyValues = {}

    # Loop through queries list
    for query in queries:
        q = query[0]
        val = query[1]

        # Check if the 1st index in the query is set to 1, if it is, increment the value if it exists in the 1st dictionary (frequency), and increment the value for the given key in the 2nd dictionary (frequencyValues)
        if q == 1:
            frequency[val] = frequency.get(val, 0) + 1
            freq = frequency[val]
            frequencyValues[freq] = frequencyValues.get(freq, 0) + 1
            frequencyValues[freq-1] = frequencyValues.get(freq-1, 1) - 1

        # Check if the 1st index in the query is set to 2, if it is, decrement the value if it exists in the 1st dictionary(frequency) and then decrement the value for the given key in the 2nd dictionary (frequencyValues).
        # If the value in the 1st dictionary is less than 0, then set it to 0 so it can't go to a negative integer.
        elif q == 2:
            if val in frequency:
                freq = frequency[val]
                frequencyValues[freq] = frequencyValues.get(freq, 1) - 1

                frequency[val] += - 1
                frequencyValues[freq-1] = frequencyValues.get(freq-1, 1) + 1

                if frequency[val] < 0:

                    frequency[val] = 0

        # Check if the 1st index in the query is set to 3, if it is, check if the key of the 2nd dictionary is present and if it is, check its value to see if it is greater than 0, if it is, add 1 to the results array, otherwise add 0 to the results array.
        elif q == 3:
            if val in frequencyValues.keys():
                if frequencyValues[val] > 0:

                    results.append(1)
                else:
                    results.append(0)
            else:
                results.append(0)

    # Return the results array.
    return results



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     queries_rows = int(input().strip())
#     queries_columns = int(input().strip())

#     queries = []

#     for _ in range(queries_rows):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = frequencyQueries(queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()