# https://www.acmicpc.net/problem/16637
# https://t.ly/GWl7

N = int(input())  # 수식의 길이를 입력 받음
exp = input()  # 수식을 입력 받음
result = None  # 최종 결과값을 저장할 변수


# 두 수를 주어진 연산자로 계산하는 함수
def cal(num1, op, num2):
    if op == "+":
        return int(num1) + int(num2)
    if op == "-":
        return int(num1) - int(num2)
    if op == "*":
        return int(num1) * int(num2)


# DFS를 활용하여 수식의 계산과 최대값 갱신을 수행하는 함수
def dfs(idx, val):
    global result

    if idx == N - 1:
        # 수식을 모두 계산했을 때
        result = max(result, val) if result is not None else val
        # 최대값 갱신
        return

    if idx + 2 < N:  # 괄호 없이 다음 연산자를 처리하는 경우
        new_val = cal(val, exp[idx + 1], exp[idx + 2]) # 현재 연산자의 다음 숫자와 연산 수행
        dfs(idx + 2, new_val) # 다음 숫자로 이동하여 DFS 재귀 호출

    if idx + 4 < N:  # 괄호를 추가하여 다음 연산자를 처리하는 경우
        bracket = cal(exp[idx + 2], exp[idx + 3], exp[idx + 4])  # 괄호 내의 연산 수행
        new_val = cal(val, exp[idx + 1], bracket)  # 현재 연산자와 괄호 내의 결과값 연산
        dfs(idx + 4, new_val)  # 괄호 다음 숫자로 이동하여 DFS 재귀 호출


dfs(0, int(exp[0]))  # 초기 인덱스와 첫 번째 숫자를 넣고 DFS 시작
print(result)  # 최대값 출력

