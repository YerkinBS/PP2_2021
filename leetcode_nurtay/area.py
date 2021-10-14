height = [1,8,6,2,5,4,8,3,7]

mx_area = 0
for i in range(len(height)):
    for j in range(i + 1, len(height)):
        S = min(height[i], height[j]) * (j - i)
        if S >= mx_area: mx_area = S
