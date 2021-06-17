idk = input()
x = idk.splitlines()
x = x.split(" ")
for i in range(0, len(x)):
    x[i] = int(x[i])
print(x)
a=0
b=0
ab=0
bc=3
g=0
for i in range(0, 3):
    if x[ab] > x[bc]:
        a=a+1

    elif x[ab] == x[bc]:
        pass
    elif x[ab] < x[bc]:
        b=b+1

    ab = ab+1
    bc=bc+1
    g=g+1


print(str(a)+" "+ str(b))    
