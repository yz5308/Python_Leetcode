class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, last = 0, len(nums) - 1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return last + 1

if __name__ == "__main__":
    print(Solution().removeElement([1, 2, 3, 4, 2, 3], 2))






    """
        Time Complexity = O(N)
        Space Complexity = O(1)

        Given an array nums and a value val, remove all instances of that value in-place and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place
        with O(1) extra memory.
        The order of elements can be changed. It doesn't matter what you leave beyond the new length.

        Example:
        Given nums = [3,2,2,3], val = 3,
        Your function should return length = 2, with the first two elements of nums being 2.
        It doesn't matter what you leave beyond the returned length.
    """
