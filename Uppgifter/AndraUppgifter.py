s = "561231-4913"
a = s[:-1]
n = a.replace("-","")
i = 1
l = ""
m = 0

for c in n:
    if i == 1:
        l = l+str(int(c) * 2)
    elif i == 2:
        l = l+str(int(c) * 1)
    i = i + 1
    if i == 3:
        i = 1

m = sum([int(c2) for c2 in l])

t = m+int(s[10])

if float(t/10) == float(str(t)[0]):
    print("Ditt personnummer är korrekt")
else:
    print("Ditt personnummer är inte korrekt")