import sys
input = sys.stdin.readline

n, t = map(int, input().split())
gepek = list(map(int, input().split()))

bal = 0
jobb = min(gepek) * t
valasz = jobb

while bal <= jobb:
    mid = (bal + jobb) // 2
    legyartott = 0

    for k in gepek:
        legyartott += mid // k
        if legyartott >= t:
            break

    if legyartott >= t:
        valasz = mid
        jobb = mid - 1
    else:
        bal = mid + 1

print(valasz)
