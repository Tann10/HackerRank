size = int(input())

numbers = list(map(int,input().split()))

weight = list(map(int,input().split()))

summ=0
total = 0
for i in range(size):
    summ += weight[i]*numbers[i]
    total += weight[i]

print(round(summ/total,1))