
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# 
# Example
# The minimum sum is and the maximum sum is . The function prints
# 16 24


def miniMaxSum(arr):
    total = sum(arr) # O(n)
    min_sum = total - max(arr) # O(n)
    max_sum = total - min(arr) # O(n)

    print(min_sum, max_sum) # O(1)


miniMaxSum([1, 2, 3, 4, 5]) # 10 14   ---> O(n) 
miniMaxSum([7, 69, 2, 221, 8974]) # 299 9271   ---> O(n) 