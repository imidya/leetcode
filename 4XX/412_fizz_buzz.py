class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []
        for i in range(n):
            number = i + 1
            if number % 15 == 0:
                r.append('FizzBuzz')
                continue
            if number % 5 == 0:
                r.append('Buzz')
                continue
            if number % 3 == 0:
                r.append('Fizz')
                continue
            r.append(str(number))
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))
