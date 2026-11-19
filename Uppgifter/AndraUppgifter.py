import random
l = []
l1 = []
l2 = []

for i in range(1,20):
    l.append(random.randrange(1,50))

for i in range(len(l)):
    n = l[i]
    if n % 2 == 0:
        l1.append(n)
    else:
        l2.append(n)

print("Jämna tal:",l1)
print("Udda tal:",l2)