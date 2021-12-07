nums=[2,7,11,15]
target = 9
# 1.브루트 포스 
def twosums(self, nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]
# 시간복잡도 O(n^2)

# 2.in을 이용한 탐색
def twosum(self,nums,target):
    for i,n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i+1)]

# 시간복잡도 O(n)

# 3.첫번째 수를 뺸 결과 키 조회
def twoSum(self,nums,target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i,num in enumerate(nums):
        nums_map[nums] = i

    # 타겟에서 첫번째 수를 뺸 결과물 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target-num]]

# 시간복잡도 O(1) 최악의 경우 O(n)

# 4. 조회 구조 개선 3번 코드 for문 합치기
def twoSum1(self, nums,target):
    nums_map={}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num],i]
        nums_map[num] = i

# 시간복잡도 O(1) 최악의 경우 O(n)

# 5. 투포인터
# 정렬되어있으니 가능 정렬이 안되있다면 인덱스 찾는 문제에서는 에러 발생
def twoSum2(self, nums,target):
    left, right = 0, len(nums) - 1
    while not left == right :
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target :
            left +=1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target :
            right -=1
        else :
            return [left, right]
