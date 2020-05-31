n =int(input())

arr = list(map(int, input().split()))
freq = list(map(int, input().split()))

arr = [arr[index] for index in range(len(arr)) for i in range(freq[index])]


arr.sort()

def get_quarlites(arr):
    n = len(arr)
    if n%2!=0:
        q = arr[n//2]
    else:
        q = (arr[n//2] + arr[(n//2)-1])/2
    return q

n = len(arr)
if n%2 !=0:
    q1 = (round(get_quarlites(arr[:n//2])))
    q3 = (round(get_quarlites(arr[(n//2)+1:])))
else:
    q1 = (round(get_quarlites(arr[:n//2])))
    q3 = (round(get_quarlites(arr[(n//2):])))

print('{:.1f}'.format(round(q3-q1,1)))