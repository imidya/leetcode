class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for k, v in count.items():
            if v == 1:
                return k


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 1, 2, 2, 3, 3, 4, 4, 5]))
