#python
def calculatemean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if(a>b):
        print('a is greater')
    elif(a==b):
        print('b and a is equal')
    else:
        print('b is greater ')
    
a=int(input('enter a number = '))
b=int(input('enter 2nd number = '))

calculatemean(a,b)
isgreater(a,b)
