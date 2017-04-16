class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ''
        for i in range(len(s)):
            r += s[-1 * (i + 1)]
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.reverseString('hello'))
