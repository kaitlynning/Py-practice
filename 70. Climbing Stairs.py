class Solution:
    def climbStairs(self, n: int) -> int:
        #input:output
        #2:2
        #3:3
        #4:5
        #5:8
        previous, current = 0, 1
        for i in range(n):
            previous, current = current, previous + current
        return current    
'''
Leetcode-Easy
70. Climbing Stairs
Runtime: 16 ms, faster than 99.66%
'''
