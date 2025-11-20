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


# LeetCode 75 with Follow-up
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


# LeetCode 347 with Follow-up
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            if num not in cnt.keys():
                cnt[num] = 1
            else:
                cnt[num] += 1    
        return self.counting_sort(cnt)[-k:]
    
    def counting_sort(self, a: dict) -> list[int]:
        cnt = [0]*(max(a.values()) + 1)

        for i in a.values():
            cnt[i] += 1
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i - 1]
        for i in range(len(cnt) - 1, 0, -1):
            cnt[i] = cnt[i - 1]
        cnt[0] = 0

        res = [0]*len(a)
        for key, value in a.items():
            res[cnt[value]] = key
            cnt[value] += 1
        return res
        

# LeetCode 215
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> List[int]:
        max_nums = max(nums)
        min_nums = min(nums)
        cnt = [0]*(max_nums - min_nums + 1)

        for i in nums:
            cnt[i - min_nums] += 1
        for i in range(len(cnt) - 1, 0, -1):
            cnt[i - 1] += cnt[i]
        print(cnt)

        for i in range(len(cnt) - 1, -1, -1):
            if cnt[i] >= k:
                return i + min_nums
        

# LeetCode 20
class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for br in s:
            if not lst and br in '}])':
                return False
                
            match br:
                case '}':
                    if lst[-1] == '{': lst.pop()
                    else: return False
                case ']':
                    if lst[-1] == '[': lst.pop()
                    else: return False
                case ')':
                    if lst[-1] == '(': lst.pop()
                    else: return False
                case _:
                    lst.append(br)
        return not lst


# LeetCode 225 with Follow-up
from queue import Queue

class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.put(x)
        for _ in range(self.queue.qsize() - 1):
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        return self.queue.get()

    def top(self) -> int:
        res = self.queue.get()
        self.push(res)
        return res

    def empty(self) -> bool:
        return self.queue.empty()


# LeetCode 232 with Follow-up
from queue import LifoQueue

class MyQueue:
    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def push(self, x: int) -> None:
        self.s1.put(x)

    def pop(self) -> int:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.put(self.s1.get())
        return self.s2.get()

    def peek(self) -> int:
        res = self.pop()
        self.s2.put(res)
        return res

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()
