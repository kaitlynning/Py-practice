190. Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:

        return int(bin(n)[2:].zfill(32)[::-1], 2)
        
'''
Leetcode-Easy
190. Reverse Bits
Runtime: 32 ms, faster than 59.19%



'''
