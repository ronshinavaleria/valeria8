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

def find_second_max(pred_max=-1, teku_max=-1):
    num = int(input())
    if num == 0:
        return teku_max
    if num > pred_max:
        teku_max = pred_max
        pred_max = num
    elif num > teku_max:
        teku_max = num
    return find_second_max(pred_max, teku_max)
result = find_second_max()
print(result)
