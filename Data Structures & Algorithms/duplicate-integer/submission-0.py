class Solution(object):
    def hasDuplicate(self, nums):
        hset = set()
        for n in nums:
            if n in hset:
                return True
            hset.add(n)
        return False