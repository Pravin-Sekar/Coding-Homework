"""Given an array arr, find the floor of average of the prefix array at every index. 

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: [10, 15, 20, 25, 30] 
Explanation: 10 / 1 = 10, (10 + 20) / 2 = 15, (10 + 20 + 30) / 3 = 20 and so on.
Input: arr[] = [12, 1]
Output: [12, 6] """
class Solution:

    def prefixAvg(self, arr):
         # code here
        res=[]
        tot=0
        for i in range(len(arr)):
            tot+=arr[i]
            res.append(tot//(i+1))
        return res