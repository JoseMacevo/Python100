sum = 0
sum_evens = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum = i
        sum_evens = sum + i
        print(sum_evens)

