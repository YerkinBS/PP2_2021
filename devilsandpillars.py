
def visible_pillar_cnt(L, R, cnt, mx):
    for i in range(L, R+1, 1):
        if height[i] > mx:
            mx = height[i]
            cnt += 1

    return cnt

n = int(input())
height = list(map(int, input().split()))
q = int(input())
v = []
while q > 0:
    X = list(map(int, input().split()))
    L = X[0]
    R = X[1] 
    mx = height[L]
    v.append(visible_pillar_cnt(L, R, 1, mx))
    q -= 1

for i in range(len(v)):
    print(v[i])