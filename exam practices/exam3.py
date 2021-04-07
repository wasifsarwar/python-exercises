import random
r = random.randint(0,10)
result = r - random.random() * 5
if result < 0.0:
    result = 5.0
else:
    result += 2.0
result = int(result)
print(result)