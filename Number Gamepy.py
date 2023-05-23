Number = int(input("The Numbers you want to print"))
B = []
C = ""

for num in range(Number+1,0,-1):
    A = num - 1
    B.append(A)
    
  
for num in B:
    C += str(num)

print (C)



