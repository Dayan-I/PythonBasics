cubes = []
for i in range(1, 1001, 2):
    i = i ** 3
    cubes.append(i)
sum_num = 0
cubes_1= []
for i in cubes:
    i += 17
    cubes_1.append(i)
for i in cubes_1:
    n = i
    a = 0
    while n > 0:
        a += n % 10
        n = n // 10

    if a % 7 == 0:
        sum_num += i


print(sum_num)
