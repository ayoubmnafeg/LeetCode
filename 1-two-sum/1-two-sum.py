class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Map = dict()
        for i in range(len(nums)):
            x = target - nums[i]
            if nums[i] in Map:
                return [Map[nums[i]], i]
            else:
                Map[x] = i 