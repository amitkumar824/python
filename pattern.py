#python
x= int(input("Enter the value: "))
for i in range(1,x):
 for j in range(1,(x-i)+1):
  print(" ",end=" ")
 for k in range(i*2-1):
  print("*",end=" ")
 print(" ")
for l in range(x):
 for m in range(l):
  print(" ",end=" ")
 for n in range(2*(x-l)-1):
  print("*",end=" ")
 print(" ")
 
 
 