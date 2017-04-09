class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        exp = len(format(num, 'b'))
        max_num = ''.join(['1']*exp)
        result = int(max_num, 2) - num
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))
