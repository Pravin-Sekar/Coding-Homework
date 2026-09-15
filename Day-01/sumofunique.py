class Solution(object):
    def sumOfUnique(self, nums):
        count={}
        sum=0
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in count:
            if count[i]==1:
                sum+=i
        return sum

        