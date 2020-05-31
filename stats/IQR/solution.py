
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

def get_quarlites(arr):
    n = len(arr)
    if n%2!=0:
        q = arr[n//2]
    else:
        q = (arr[n//2] + arr[(n//2)-1])/2
    return q

if n%2 !=0:
    print(round(get_quarlites(arr[:n//2])))
    print(round(get_quarlites(arr)))
    print(round(get_quarlites(arr[(n//2)+1:])))
else:
    print(round(get_quarlites(arr[:n//2])))
    print(round(get_quarlites(arr)))
    print(round(get_quarlites(arr[(n//2):])))


