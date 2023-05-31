# https://www.acmicpc.net/problem/17070
N = int(input())
status = []
for _ in range(N):
    status.append(list(map(int,input().split())))
# print(status)

result = 0


def dfs(r1, c1, r2, c2):
    # print(r1, c1, ' ', r2, c2)
    global result
    if r2 == N and c2 == N:
        # print("도달!")
        result += 1
        return
    v = r1 == r2  # 같은 행 (가로 방향)
    # if v:
        # print("가로 방향")
    h = c1 == c2  # 같은 열 (세로 방향)
    # if h:
        # print("세로 방향")
    c = (r1 != r2 and c1 != c2)
    # if c:
        # print("대각선 방향")
    if h or c:  # 세로 방향이거나 대각선이라면
        if r2 < N:  # 인덱스 벗어나지 않는 한에서
            if not status[r2][c2-1]: # 행 방향 전진 (세로)
                dfs(r2, c2, r2+1, c2)
    if v or c:  # 가로 방향이거나 대각선이라면
        if c2 < N:  # 인덱스 벗어나지 않는 한에서
            if not status[r2-1][c2]: # 열 방향 전진 (가로)
                dfs(r2, c2, r2, c2+1)
    if r2 < N and c2 < N:
        if not sum((status[r2][c2-1], status[r2-1][c2], status[r2][c2])):
            dfs(r2, c2, r2 + 1, c2 + 1)


dfs(1, 1, 1, 2)
print(result)
# 시간초과