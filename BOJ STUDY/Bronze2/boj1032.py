# 자연수 입력 반복문을 통한 문자열 입력 문자열 공통점 찾기
# 공통문자 출력후 나머지 문자열 ?로 표시
N = int(input())
prompt = list(input())
for i in range(N-1):
    prompts = list(input())
    for j in range(len(prompt)):
        if prompt[j] != prompts[j]:
            prompt[j] = '?'
print(''.join(prompt))