class Solution(object):
    def findDuplicates(self, nums):
        count={}
        ans=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in count:
            if count[i]>1:
                ans.append(i)
        return ans
        