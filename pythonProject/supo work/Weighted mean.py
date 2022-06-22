data = [
    [21.61, 0.02],
    [21.59, 0.02],
    [21.65, 0.04],
    [21.40, 0.10],
    [21.55, 0.03],
    [21.59, 0.01],
]

top = 0

bottom = 0

for value in data:
    top += value[0] / (value[1] ** 2)
    bottom += 1 / (value[1] ** 2)

result = top / bottom

print(result, bottom ** -0.5)
