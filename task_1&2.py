#task_1
def odd_to_N(n):
    for i in range(1, n + 1, 2):
        yield i


odd_to_10 = odd_to_N(10)
next(odd_to_10)
#task_2

odd_to_ = ( i for i in range(1, int(input('Enter number: ')), 3))
print(next(odd_to_), next(odd_to_), next(odd_to_))