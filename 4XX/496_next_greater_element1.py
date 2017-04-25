class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        for i, findNum in enumerate(findNums):
            cands = None
            for num in nums[nums.index(findNum):]:
                if num > findNum:
                    cands = num
                    break
            if cands:
                results.append(cands)
            else:
                results.append(-1)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))
