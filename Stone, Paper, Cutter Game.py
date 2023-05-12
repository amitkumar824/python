import random as R
line = "-" * 45 + " RESTART " + "-" * 45

while True:

    z=1
    l=9
    ab=cp=0
    while(z<=10):
        a=["Stone","Paper","Cutter"]
        b=R.choice(a)
        print(">>> Press 'S' or 's' for Stone\n>>> Press 'P' or 'p' for Paper\n>>> Press 'C' or 'c 'for Cutter\n")
        u=str(input("Enter Your Choice:- "))
        u = u.upper()
        c=b+u
        if c=='StoneS' or c=='PaperP' or c=='CutterC':
            print(f"Match Draw! {l} chances left")
        elif c=='StoneP' or c=='PaperC' or c=='CutterS':
            print(f"You Won! {l} chances left")
            ab+=1
        elif c=='StoneC' or c=='PaperS' or c=='CutterP':
            print(f"You Loose! {l} chances left")
            cp+=1
        else:
            print("Invalid Input!!")
            continue;
        z+=1
        l-=1

    if ab>cp:
        print(f"\n\t\t\t\t\t\tYOU WON THE GAME, Your score is {ab}... and computer's score is {cp}\n{line}")
    elif ab<cp:
        print(f"\n\t\t\t\t\t\tYOU LOST THE GAME, Your score is {ab}... and computer's score is {cp}\n{line}")
    else:
        print(f"\n\t\t\t\t\t\t              ITS A TIE, scores are {ab}, {cp}\n{line}")
