def prost_ch(n, delit=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % delit == 0:
        return False
    if delit*delit > n:
        return True
    return prost_ch(n, delit + 1)
n = int(input())
if prost_ch(n):
    print("YES")
else:
    print("NO")


