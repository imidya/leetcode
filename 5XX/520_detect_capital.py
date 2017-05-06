class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        upper = 0
        lower = 0
        first = False

        for i, c in enumerate(word):
            if c.isupper():
                upper += 1
                if i == 0:
                    first = True
            elif c.islower():
                lower += 1

        if upper == 1 and first:
            return True
        elif lower == 0:
            return True
        elif upper == 0:
            return True
        else:
            return False



if __name__ == '__main__':
    s = Solution()
    print(s.detectCapitalUse('USA'))
    print(s.detectCapitalUse('Google'))
    print(s.detectCapitalUse('leetcode'))
    print(s.detectCapitalUse('FlaG'))
