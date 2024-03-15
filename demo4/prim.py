a = int(input("Enter value for a: "))
q = int(input("Enter value for q: "))

i = 1

lst = []

while i < q:
    result = (a**i) % q
    lst.append(result)
    i += 1

lst.sort()
print(lst)

