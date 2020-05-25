class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start+1, end+1]
            elif sum < target:
                start += 1
            else:
                end -= 1
        return []    
        
        #two pointer不斷移動左指針 調整又指針 向中間移相等即可
        #有備註說明Your returned answers (both index1 and index2) are not zero-based,若習慣從0開始,所以最後return再加一也可 [start+1, end+1]
       
            
        
        
'''
Leetcode-Easy
167. Two Sum II - Input array is sorted
Runtime: 64 ms, faster than 68.77%

sorted in ascending order 上升排序

'''
