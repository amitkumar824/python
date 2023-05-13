#python
def multiple(x,y):
    c=x*y
    return c
def addition(f,g):
    s=f+g
    return s
def substraction(d,w):
    q=d-w
    return q
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
e=input("what do you want - for  multiply press * , for addition addition press + , for substraction press -")
if(e=="*"):
 print("the product is",multiple(a,b))
elif(e=="+"):
 print("the addition is",addition(a,b))
elif(e=="-"):
  print("substraction is",substraction(a,b))
else:
    print("invalid")