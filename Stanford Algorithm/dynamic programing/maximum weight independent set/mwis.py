file = open("mwis.txt", "r")
#file = open("test.txt", "r")
data = file.read().splitlines() # use splitlines() to remove the newlines
num = int(data[0])
vals = [int(val) for val in data[1:]] # then convert from string to integer

A = [0] * (1 + num)
A[0] = 0
A[1] = vals[0]
#elif n == 0:
#	return a
#elif n == 1:
#	return b
#else:
for i in range(1,num):
    A[i+1] = max(A[i], vals[i] + A[i - 1])

S = []
idx = num
while idx >= 1:
    if A[idx - 1] >= A[idx - 2] + vals[idx - 1]:
        idx -= 1
    else:
        S.append(idx)
        idx -= 2

candidates = [1, 2, 3, 4, 17, 117, 517, 997]
for can in candidates:
    print(can in S)