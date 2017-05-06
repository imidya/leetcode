class Solution(object):

    def check_direction(self, x, y, matrix):
        # check up
        if x - 1 >= 0:


    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        columns = len(matrix[0])
        rows = len(matrix)




if __name__ == '__main__':
    nums = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    s = Solution()
    print(s.longestIncreasingPath(nums))
