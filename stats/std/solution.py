n = int(input())

arr = list(map(int, input().split()))

total = 0
for i in arr:
    total += i

mean = total/n

sum_dev= 0
for i in arr:
    sum_dev += (i-mean)**2

print(round((sum_dev/n)**(1/2),1))