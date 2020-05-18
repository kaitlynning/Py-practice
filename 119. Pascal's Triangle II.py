class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result =[1] + [0]*rowIndex 
        
        for i in range(rowIndex):
            for j in range(i+1,0,-1):
                result[j] += result[j-1]
            
        return result
                    
'''
Leetcode-Easy
119. Pascal's Triangle II
Runtime: 20 ms, faster than 98.39%


'''
