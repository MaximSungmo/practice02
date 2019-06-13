import os
import random

print()
# dir, file = os.path.split(os.getcwd())
# print(dir, file, sep="\n")

# print(dir.split(sep='\\'))


# 1 ~ 100 랜덤
max, min = 100, 1
n = random.randrange(max) + min

print(n)