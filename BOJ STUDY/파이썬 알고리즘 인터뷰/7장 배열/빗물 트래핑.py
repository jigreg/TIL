# 높이를 입력 받아 비 온후 얼마나 많은 물이 쌓일 수 있는지 계산

def trap(self, height) :
    if not height:
        return 0

    volume = 0
    left, right = 0 , len(height) -1
    left_max, right_max = height[left],height[right]

    while left < right :
        left_max, right_max = max(height[left], left_max), max(height[right],right_max)
        if left_max <= right_max:
            volume += left_max - height[left]
            left +=1
        else :
            volume += right_max - height[right]
            right ==1
        return volume
