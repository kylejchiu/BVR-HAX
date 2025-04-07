import random
pioverfour = 0
total = 0
randomx = 0
randomy = 0
percent = 0
for i in range (100000):
    percent += 0.001
    print(percent)
    for i in range(10000):
        randomx = random.uniform(-1, 1)
        randomy = random.uniform(-1, 1)
        total += 1
        if (randomx ** 2 + randomy ** 2 < 1):
            pioverfour += 1
pi = pioverfour / total
print(pi * 4)