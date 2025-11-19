#LeetCode 509
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        f1 = 1
        f2 = 1
        i = 1
        while i < n:
            f1, f2 = f2, f1 + f2
            i += 1
        return f1
        

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


# LeetCode 75
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1

        i = 0
        j = 0
        while i < len(nums):
            while count[j] > 0:
                nums[i] = j
                i += 1
                count[j] -= 1
            j += 1
