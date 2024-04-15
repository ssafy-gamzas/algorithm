import sys
input = sys.stdin.readline

N = int(input())
building = []
ans = 0

for _ in range(N):
    x, y = map(int, input().split())
    if not building and y:   # 스택에 아무것도 없고 y > 0 이면 담음
        building.append(y)
    elif building and building[-1] < y:  # 더 높은 빌딩이 들어오면 담음
        building.append(y)
    elif building and building[-1] > y:  # 담은 빌딩보다 낮은 빌딩이 들어오면 높은 빌딩들의 개수를 셈
        while building:
            if building[-1] > y:
                building.pop()
                ans += 1
            else:
                break
        if y and y not in building:
            building.append(y)

# 남은 빌딩의 수랑 더해줌
print(ans+len(building))
