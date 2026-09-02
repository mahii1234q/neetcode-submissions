class Solution(object):
    def twoSum(self, nums, target):
        hmap={}
        for i, n in enumerate(nums):
            difference=target-n
            if difference in hmap:
                return[hmap[difference],i]
            hmap[n]=i    
        return[]        
    

        