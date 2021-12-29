from collections import deque
import sys
if __name__ == '__main__':
    N,M = map(int,input().split())
    if N == 0:
        print(0)
        sys.exit()

    numbers = list(map(int, input().split()))
    dq = deque(range(1, N + 1))

    result = 0

    for i in range(len(numbers)):
        if numbers[i] == dq[0]:
            dq.popleft()
            continue
        dq_idx = dq.index(numbers[i])

        if dq_idx > len(dq) // 2:
            # 시계
            dq.rotate(len(dq) - dq_idx)
            result += (len(dq) - dq_idx)
        elif dq_idx <= len(dq) // 2:
            # 반시게
            dq.rotate(-dq_idx)
            result += dq_idx
        dq.popleft()

    print(result)