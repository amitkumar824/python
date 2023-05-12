dict1={'a':'·-', 'b':'-···', 'c':'-·-·', 'd':'-··', 'e':'·', 'f':'··-·', 'g':'--·', 'h':'····', 'i':'··'
       , 'j':'·---', 'k':'-·-', 'l':'·-··', 'm':'--', 'n':'-·', 'o':'---', 'p':'·--·', 'q':'--·-', 'r':'·-·',
       's':'···', 't':'-', 'u':'··-', 'v':'···-', 'w':'·--', 'x':'-··-', 'y':'-·--', 'z':'--··', ' ':' ', '.':'.'}

while True:
    mystr=str(input("Enter your text:- "))
    ms_space=" ".join(mystr)
    ms_tup=tuple(ms_space)

    for a1 in ms_tup:
        a2=dict1.get(a1)
        print(a2,end="")

    if mystr=='exit':
        break

    print("\n","_" * 75)
