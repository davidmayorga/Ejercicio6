



# output


c = int(input("Digite el valor de C: "))
D = 2*c
N = 0


#Processing
while c<D:
    c=c+(0.05)*c
    N=N+1
print("En ", N, "meses el capital tendra un valor de: ", c)