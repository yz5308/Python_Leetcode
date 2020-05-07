class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]

        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for y in self.permute(n):
                ans.append([num] + y)
        return ans






    """
        Given a collection of distinct integers, return all possible permutations.

        Example:

        Input: [1,2,3]
        Output:
        [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]

        记传入数组为nums，若nums的长度不大于1，则直接返回[nums]

        遍历nums，从中抽取一个数num，递归计算剩余数字组成的数组n，然后将num与结果合并
    """
