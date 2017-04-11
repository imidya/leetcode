import math


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = format(x, 'b')[::-1]
        bin_y = format(y, 'b')[::-1]

        max_len = max(len(bin_x), len(bin_y))

        distance = 0
        for i in range(max_len):
            x_bit = bin_x[i] if i < len(bin_x) else 0
            y_bit = bin_y[i] if i < len(bin_y) else 0
            if int(x_bit) != int(y_bit):
                distance += 1

        return distance


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
