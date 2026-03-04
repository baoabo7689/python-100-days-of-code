f1 = open('file1.txt', 'r', encoding="utf-8")
f2 = open('file2.txt', 'r', encoding="utf-8")
ns1 = [int(s) for s in f1]
ns2 = [int(s) for s in f2]
result = [n1 for n1 in ns1 if n1 in ns2]

print(result)