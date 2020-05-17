class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]*rowIndex + [1]
        
        for i in range(2, rowIndex+1):
            for j in range(i-1,0,-1):
                result[j] += result[j-1]
            
        return result
                    
'''
Leetcode-Easy
119. Pascal's Triangle II
Runtime: 52 ms, faster than 5.15%


'''
