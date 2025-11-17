# LeetCode 70
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        n1, n2 = 1, 2
        while n > 1:
            n -= 1
            n1, n2 = n2, n1 + n2
        return n1

        
