"""You are given an array arr of size n and an integer k. Your task is to find a pair of integers in the array such that it follows two conditions:

The sum of the pair is the maximum possible but less than k.
Out of all such pairs, choose the one with the maximum absolute difference between the two integers.
If no such pair exists, return (-1, -1).

Example:

Input: arr = [2, 4, 3, 6, 8, 10], k = 10
Output: (3, 6)
Explanation:
The pair (3, 6) has a sum of 9, which is less than 10. Among all pairs with sums less than 10, (3, 6) has the maximum absolute difference.
Input: arr = [2, 3, 4, 6, 10, 8], k = 0
Output: (-1,-1)
Explanation: No pair exists with a sum less than 0."""

class Solution:
    def maxSum(self, arr, k):

        arr.sort()

        left = 0
        right = len(arr) - 1

        maxi = -1
        fin = [-1, -1]

        while left < right:

            total = arr[left] + arr[right]

            if total < k:

                if total > maxi:
                    maxi = total
                    fin = [arr[left], arr[right]]

                elif total == maxi:
                    if abs(arr[right] - arr[left]) > abs(fin[1] - fin[0]):
                        fin = [arr[left], arr[right]]

                left += 1

            else:
                right -= 1

        return fin