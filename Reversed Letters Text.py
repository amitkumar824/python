dict1 = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p'
         , 'l':'o', 'm':'n', 'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g', 'u':'f', 'v':'e',
         'w':'d', 'x':'c', 'y':'b', 'z':'a', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8',
         '9':'9', '0':'0', '.':'.', ',':',', '!':'!', '?':'?', '(':'(', ')':')', '/':'/', ' ':' '}

line = "-" * 35 + " RESTART " + "-" * 35

while True:

    text = str(input("Enter the text:- "))

    for a in text:
        if a in dict1:
            print(dict1[a], end="")

        else:
            print("Invalid!!")
            continue

    print(f"\n{line}")
