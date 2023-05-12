line = "-" * 45 + " RESTART " + "-" * 45

while True:

    characters = {'a':'@', 'b':'B', 'c':'(', 's':'$', 'i':'!', 'j':'?', 'l':'|', 'o':'0', 'v':'Ѷ', 'x':'*', 'y':'¥', 'f':'ɟ', 'h':'Ҥ'}

    text = str(input("Enter your password:- "))

    for a1 in text:
        if a1 in characters:
            text = text.replace(a1, characters[a1])

        else:
            continue

    print(f"\nYour new Password = {text}\n\n{line}")