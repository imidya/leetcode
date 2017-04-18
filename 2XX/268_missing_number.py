class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums) + 1):
            try:
                if i != nums[i]:
                    return i
            except:
                return i

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([0, 1, 3]))
