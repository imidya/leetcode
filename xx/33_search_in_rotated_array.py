class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([0, 1, 2, 4, 5, 6, 7], 3))
