n = int (input("Veuillez saisir un nombre: "))
S=0
j=1
for i in range(n):
    S = S + (j ** 2)
    j = j +2
print ("La somme des nombres impaires est: ", S )