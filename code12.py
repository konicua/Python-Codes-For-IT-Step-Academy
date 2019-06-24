a = 153
b = str(a)
c = []

for digit in b:
    c.append(int(digit))

summary = 0
for numbers in c:
    summary += numbers**len(c)
    
print(summary)