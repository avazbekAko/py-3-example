print("Маҷмуъҳои адади")
A = {1, 2, 3, 4, 5, 6}
B = {6, 3, 7, 4, 1, 2}
print("A", A)
print("B", B)

s1 = A.union(B)
s1 = A | B
print("Якҷояшави маҷмуъи А ва В : ", s1)

s2 = A.intersection(B)
s2 = A & B
print("Буриши маҷмуъи А ва В : ", s2)

s3 = A.difference(B)
s3 = A - B
print("Фарки маҷмуъи А аз В : ", s3)

s4 = B.difference(A)
s4 = B - A
print("Фарки маҷмуъи B аз A : ", s4)