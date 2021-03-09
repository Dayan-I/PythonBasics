src = [1, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [i for i in src[1:] if i > src[src.index(i) - 1]]
print(result)