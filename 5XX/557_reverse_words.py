class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split(' ')

        r_words = []
        for word in words:
            r_words.append(word[::-1])

        return ' '.join(r_words)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
