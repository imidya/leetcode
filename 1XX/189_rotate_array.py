class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            pass
        else:
            k = k % len(nums)
            move = len(nums) - k
            nums[:] = nums[move:] + nums[:move]
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1], 0))
    print(s.rotate([1, 2], 1))
    print(s.rotate([1, 2, 3], 2))
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
