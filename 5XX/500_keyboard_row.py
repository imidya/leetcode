class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = 'qwertyuiop'
        row_2 = 'asdfghjkl'
        row_3 = 'zcxvbnm'
        rows = [row_1, row_2, row_3]

        results = []
        for word in words:
            for row in rows:
                all_in = True
                for c in word:
                    if c.lower() in row:
                        pass
                    else:
                        all_in = False
                        break
                if all_in:
                    results.append(word)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
    print(s.findWords(["asdfghjkla","qwertyuiopq","zxcvbnzzm","asdfghjkla","qwertyuiopq","zxcvbnzzm"]))
