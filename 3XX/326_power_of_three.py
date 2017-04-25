class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False



if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(3))
    print(s.isPowerOfThree(9))
    print(s.isPowerOfThree(5))
