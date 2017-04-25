class Solution(object):
    def cal(self, position, grid):
        x, y = position
        perimeter = 4
        # up
        if x - 1 >= 0 and grid[x-1][y] == 1:
            perimeter -= 1

        # down
        if x + 1 < len(grid) and grid[x+1][y] == 1:
            perimeter -= 1

        # left
        if y - 1 >= 0 and grid[x][y - 1] == 1:
            perimeter -= 1

        # right
        if y + 1 < len(grid[0]) and grid[x][y + 1] == 1:
            perimeter -= 1

        return perimeter

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    perimeter += self.cal((x, y), grid)

        return perimeter



if __name__ == '__main__':
    _map = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]
    s = Solution()
    print(s.islandPerimeter(_map))
