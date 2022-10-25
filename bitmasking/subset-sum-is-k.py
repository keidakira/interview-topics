"""
Given an array of numbers (set), find if there is a subset of the numbers in the
array that adds up to a given number (K).

For example, given the array [2, 4, 8, 6] and K = 14, return true since 2 + 4 + 8
"""
def subset_sum_is_k(arr, k):
    """
    Return true if there is a subset of arr that adds up to k

    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    # Base case
    if k == 0:
        return True

    if len(arr) == 0:
        return False

    # Recursive case
    if arr[0] > k:
        return subset_sum_is_k(arr[1:], k)
    return subset_sum_is_k(arr[1:], k - arr[0]) or subset_sum_is_k(arr[1:], k)

def subset_sum_equal_k(arr, val):
    """
    Use bitmasking to solve it in O(2^n)

    - There are 2^n possible combinations of numbers in a set
    - Go through each combination, and add the numbers
    - If the sum is equal to val, return True
    """
    n = len(arr)
    for x in range(pow(2, n)):
        total = 0
        for k in range(n):
            if x & (1 << k):
                total += arr[k]
        if total == val:
            return True
    
    return False

if __name__ == "__main__":
    arr = [2, 4, 8, 6]
    k = 14
    print(subset_sum_equal_k(arr, k))