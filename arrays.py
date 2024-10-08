#Static Arrays- allocated size and type; Can't change once declared and can't store additional elements

#26- Remove Duplicates from Sorted Array
    #

class Solution:
    def removeDuplicates(self, num):
    l=1
    for r in range(1,len(num)):
        if num[r] != num[r-1]:
           num[l] = num[r]
           l += 1
    return l


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        k = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1
            
