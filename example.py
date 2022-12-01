inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
ls = []
for i in range(1, (a+1), b):
    ls.append(i)
print(ls[len(ls)-2])