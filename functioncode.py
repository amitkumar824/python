#python
p=open(r'C:\Users\hp\OneDrive\Desktop\New folder\hello.txt',"w+")    
def multiple(x,y):
    c=x*y
    return c

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
e=input("what do you want - for  multiply press a ")
if(e=="a"):
 l=multiple(a,b)
 print(l)

 

 
else:
    print("invalid")
p.write("first number is"+str(a))
p.write("\nsecond number is"+str(b))
p.write("\nproduct is"+str(l))

p.close()