class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]
        water_count = 0

        while left < right:
            curr_count = 0
            if max_left < max_right:
                curr_count = max_left - height[left]
                left += 1
                max_left = max(height[left], max_left)
                
            else:
                curr_count = max_right - height[right]
                right -= 1
                max_right = max(height[right], max_right)
                
            
            if curr_count > 0:
                water_count += curr_count
            
        return water_count



