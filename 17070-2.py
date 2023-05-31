# https://www.acmicpc.net/problem/17070
# https://pacific-ocean.tistory.com/458

N = int(input())  # 격자의 크기를 입력 받음
s = [list(map(int, input().split())) for _ in range(N)]  # 격자의 정보를 입력 받음
result = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]  # 결과를 저장할 DP 배열 초기화

result[0][0][1] = 1  # 가로 방향 파이프의 시작점 (0, 1)을 1로 초기화

# 가로 방향으로 이동하는 파이프의 경우 초기화
for i in range(2, N):
    if not s[0][i]:  # 통행이 가능한 경우
        result[0][0][i] = result[0][0][i - 1]  # 가로 열방향으로 이전 값과 같은 값을 가짐

# 행 방향으로 이동하는 파이프의 경우와 대각선 방향으로 이동하는 파이프의 경우를 계산
for i in range(1, N):  # 행 방향
    for j in range(2, N):  # 열 방향
        if not s[i][j] and not s[i - 1][j] and not s[i][j - 1]:  # 현재 위치, 위쪽, 왼쪽이 모두 통행 가능한 경우
            # 대각선 방향으로 이동하는 파이프의 경우의 수는 가로, 세로, 대각선의 이전 경우의 수를 합산한 값임
            result[2][i][j] = result[0][i - 1][j - 1] + result[1][i - 1][j - 1] + result[2][i - 1][j - 1]
        if not s[i][j]:  # 현재 위치가 통행 가능한 경우
            # 가로 방향으로 이동하는 파이프의 경우의 수는 이전 열에서 가로 방향, 대각선 방향의 경우의 수를 합산한 값임
            result[0][i][j] = result[0][i][j - 1] + result[2][i][j - 1]
            # 세로 방향으로 이동하는 파이프의 경우의 수는 이전 행에서 세로 방향, 대각선 방향의 경우의 수를 합산한 값임
            result[1][i][j] = result[1][i - 1][j] + result[2][i - 1][j]

# 최종 결과값 계산
print(sum([r[N - 1][N - 1] for r in result]))