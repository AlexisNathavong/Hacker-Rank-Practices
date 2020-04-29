# PROBLEM
# Karl has list of integers, what he want to do is reduce the list so that all of the numbers left are equal to eachother. By doing that we would have to detirmine the min numbers to delete in the list. For example, if his list consists of 1, 2, 2, 3; we could delete the numbers 1 and 3, leaving inside the list 2, 2; or we could delete the numbers 2 and 2, and either 1 or 3 but that would be 3 deletions and the min number of deletions will be 2. We need to return the min number of deletions, which in the example is 2.


# SOLUTION:
# Step 1: Set a counter to zero, to count the number of equal elements from the given array.
# Step 2: Create an Elements dictionary to store the given array's key value pairs.
# Step 3: Loop through the array, arr, to find the elements that are equal to eachother.
# Step 4: Check if the element of i is not in the Elements dictionary, then move onto the next element of the array at index j.
# Step 5: Check if element of i is equal to element of j, then increment the counter.
# Step 6: Add the count to the Elements dictionary
# Step 7: Find the key with the largest value.
# Step 8: Return the min number of deletions by subtracting the largest value from the length of the original array.


def equalizeArray(arr):
    count = 0
    Elements = {}

    for i in arr:
        if i not in Elements:
            for j in arr:
                if i == j:
                    count= count+1
            Elements[i] = count
            count = 0

    max_val = max(Elements, key= Elements.get)

    return (len(arr) - Elements[max_val])