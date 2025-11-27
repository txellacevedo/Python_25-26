a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
r = 0
#n = 10
#i = 1
while not ((a<b) or (c>0)): #and (i<= n):
    #print("i =",i, end= " ")
    if b%2==0:
        b = b -1
        print("b= ",b)
    else:
        r=r+c
        b=b-1
        print("b=",b, "r=",r)
    #i = i + 1
#print("r = ",r)

