#python
f=open(r'C:\Users\hp\OneDrive\Desktop\New folder\hello.txt','w+')
a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
c=a+b
f.write("1st number is"+str(a))
f.write("\n2nd number is"+str(b))
f.write("\naddition is"+str(c))

f.close()