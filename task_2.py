cubes = []
for i in range(1, 1001, 2):
    i = i ** 3
    cubes.append(i)
sum_num = 0

for i in cubes:
    n = i
    a = 0
    while n > 0:
        a += n % 10
        n = n // 10

    if a % 7 == 0:
        sum_num += i


print(sum_num)
