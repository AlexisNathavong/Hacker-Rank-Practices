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


# HIGH LEVEL PROBLEM EXPLANATION:
    # Given a list of queries, where each query is in the form of x and y values. The number 1 in the x value represents insertion into your data structure, and the number 2 in the x value represents deletion, if a number is present, from the data structure. The number 3 in the x value checks if the number in the y axis matches the amount of times a number appears in the data structure. If it does appear the correct number of times in the data structure then return a '1' in the output list and if not, return a '0' in the output list. The goal is to return the output list of 0s and 1s.


# HIGH LEVEL SOLUTION:
    # ​Look through the queries list, checking if the x axis value for each query is a 1, 2, or 3. If it is 1, add the value in the 1st dictionary, and add the value for the given key in the 2nd dictionary. If it is 2, subtract the value in the 1st dictionary and subtract the value for the given key in the 2nd dictionary. If it is 3, check if the key of the 2nd dictionary is present and if the value is greater than 0, if it is, add 1 to the results list, otherwise add 0 to the results list. In the end return the results list.

# SOLUTION:
    # Step 1: Create a frequency dictionary to track the key value pairs of the frequencies of each number
    # Step 2: Create an empty list for storage, called results to be returned
    # Step 3: Create a second frequency dictionary to keep track of how many times each key of the 1st dictionary appears
    # Step 4: Loop through queries list
    # Step 5: Check if the x axis(1st index) in the query is set to 1, if it is, increment the value if it exists in the 1st dictionary (frequency), and increment the value for the given key in the 2nd dictionary (frequencyValues)
    # Step 6: Check if the x axis element in the query is set to 2, if it is, decrement the value, if it exists, in the 1st dictionary (frequency) setting to 0 so it can't go to a negative integer, and decrement the value for the given key in the 2nd dictionary (frequencyValues)
    # Step 7: Check if the x axis element in the query is set to 3, if it is, check if the key of the 2nd dictionary is present and if it is, check its value to see if it is greater than 0, if it is, add 1 to the results array, otherwise add 0 to the results array.
    # Step 8: Return the results array.

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

        # Check if the x axis element in the query is set to 1, if it is, increment the value if it exists in the 1st dictionary (frequency), and increment the value for the given key in the 2nd dictionary (frequencyValues)
        if q == 1:
            frequency[val] = frequency.get(val, 0) + 1
            freq = frequency[val]
            frequencyValues[freq] = frequencyValues.get(freq, 0) + 1
            frequencyValues[freq-1] = frequencyValues.get(freq-1, 1) - 1

        # Check if the x axis element in the query is set to 2, if it is, decrement the value, if it exists, in the 1st dictionary (frequency) setting to 0 so it can't go to a negative integer, and decrement the value for the given key in the 2nd dictionary (frequencyValues)
        elif q == 2:
            if val in frequency:
                freq = frequency[val]
                frequencyValues[freq] = frequencyValues.get(freq, 1) - 1

                frequency[val] += - 1
                frequencyValues[freq-1] = frequencyValues.get(freq-1, 1) + 1

                if frequency[val] < 0:

                    frequency[val] = 0

        # Check if the x axis element in the query is set to 3, if it is, check if the key of the 2nd dictionary is present and if it is, check its value to see if it is greater than 0, if it is, add 1 to the results array, otherwise add 0 to the results array.
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


# #
# # Complete the 'frequencyQueries' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts 2D_INTEGER_ARRAY queries as parameter.
# #

# # loop through the queries and increment and decrement the frequencies of each number accordingly in a dict ... simultaneously in a separate dict keep track of how many times each key of the other dict appears

# # when checking if any integer is present whose frequency is exactly y for QUERY 3 you would check if the count of y in the second dict exists...


# def frequencyQueries(queries):
#     # Write your code here
#     # Set frequency to a dictionary
#     frequency = {}
#     # Set results to an empty list for storage.
#     results = []
#     # Set another dictionary of frequencyValues
#     frequencyValues = {}
#     # For loop:
#     for query in queries:
#         # Set query to index of 0.
#         q = query[0]

#         # Val is equal to set query to index of 1.
#         val = query[1]
#         # If q is equal to 1.
#         if q == 1:
#             # Then the value of frequency is equal to frequency value of the given key.
#             # Get method returns the value for the given key, if present in the dictionary. If not, then it will return None.
#             frequency[val] = frequency.get(val, 0) + 1
#             # Setting freq to frequency value.
#             freq = frequency[val]
#             # Now checking in the frequencyValue dict and sets it to value for the given key, if present in the dictionary.
#             frequencyValues[freq] = frequencyValues.get(freq, 0) + 1
#             frequencyValues[freq-1] = frequencyValues.get(freq-1, 1) - 1
#         # Otherwise if q is equal to 2.
#         elif q == 2:
#             # If val in frequency
#             if val in frequency:
#                 # Set freq to equal to frequency[value]
#                 freq = frequency[val]
#                 # Set the other dictionary(frequencyValues) that passes in the freq to equal to frequencyValues.get(freq, 1) - 1. 
#                 frequencyValues[freq] = frequencyValues.get(freq, 1) - 1

#                 # decrement line
#                 frequency[val] += - 1 
#                 frequencyValues[freq-1] = frequencyValues.get(freq-1, 1) + 1
#                 # If frequency of the value is less than 0
#                 if frequency[val] < 0:
#                     # The frquency of the value is 0.
#                     frequency[val] = 0
#         elif q == 3:
            
#             # keys() returns a view object that displays a list of all the keys in the dictionary.
#             if val in frequencyValues.keys():
                
#                 # If the frequencyValue dictionary's value is greater than 0.
#                 if frequencyValues[val] > 0:
                    
#                     # Then take the list and adds a single item to the existing list. It doesn't return a new list of items but will modify the original list by adding the item to the end of the list. After executing the method append on the list the size of the list increases by one.
#                     results.append(1)
#                 # Otherwise add 0 to the list
#                 else:
#                     results.append(0)
#             # Repeat
#             else:
#                 results.append(0)


#     return results

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