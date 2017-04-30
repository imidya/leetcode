class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_set = a.replace('i', '').split('+')
        b_set = b.replace('i', '').split('+')

        constant = (int(a_set[0]) * int(b_set[0])) + (int(a_set[1]) * int(b_set[1]) * -1)
        abi = (int(a_set[0]) * int(b_set[1])) + (int(a_set[1]) * int(b_set[0]))
        return '%s+%si' % (constant, abi)


if __name__ == '__main__':
    s = Solution()
    print(s.complexNumberMultiply("1+1i", "1+1i"))
    print(s.complexNumberMultiply("1+-1i", "1+-1i"))
