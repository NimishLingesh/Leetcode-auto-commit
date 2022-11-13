class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """heap = []
        
        for num in nums:
            if num+1 in nums or num-1 in nums:
                heapq.heappush(heap, num)
                
        max_count = 0
        count = 1
        # print(heap)
        for idx, ele in enumerate(heap):
            print(ele)
            if idx == len(heap) - 1:
                break
            if ele == heap[idx+1]-1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1
        return max(max_count, count)"""
            
        longest = 0
        nums = set(nums)
        
        for num in nums:
            if num-1 not in nums:
                length = 1
                while(num+length in nums):
                    length += 1
                longest = max(longest, length)
        return longest
            