a = 3
q = 17

i = 1

lst = []

while i < q:
    result = (a**i) % q
    lst.append(result)
    i += 1

lst.sort()
print(lst)

