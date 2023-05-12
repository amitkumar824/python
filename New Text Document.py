""" <<<<<<<<<<<< INSTRUCTIONS >>>>>>>>>>>>>

1. Welcome to the QUIZ GAME... Test Your Knowledge Here...
2. This game has 3 Levels... Level-1, Level-2, Level-3
3. You have to answer 5 easy questions in Level-1... 3 medium questions in Level-2... and 2 difficult questions in Level-3...
4. If you answered 3 question correctly in Level-1, You'll reach Level-2... where you have to answer atleast 2
   questions correctly to reach Level-3... where u have to answer atleast 1 question correctly to win the Game...

5. ALL THE VERY BEST... GOOD LUCK...

"""

from random import choice
from winsound import Beep, MessageBeep

line = "\n<" + "-" * 30 + " THANK YOU " + "-" * 30 + ">\n"

easy = [
    ["The International Literacy Day is observed on", ["SEPT 8", "Nov 28", "May 2", "Sept 22"]],
    ["The language of Lakshadweep, a Union Territory of India, is...?", ["Tamil", "Hindi", "MALAYALAM", "Telugu"]],
    ["Bahubali festival is related to?", ["Hinduism", "Islam", "Buddhism", "JAINISM"]],
    ["Which day is observed as the World Standards Day?", ["OCT 14", "June 26", "Nov 15", "Dec 2"]],
    ["Who is the author of 'Manas Ka-Hans'?",
     ["Khushwant Singh", "AMRIT LAL NAGAR", "Prem Chand", "Jayashankar Prasad"]],
    ["Who is the author of the epic 'Meghdoot'?", ["Vishakadatta", "Valmiki", "Banabhatta", "KALIDAS"]],
    ["Which of the following is observed as Sports Day every year?",
     ["22nd April", "26th  july", "29TH AUGUST", "2nd October"]],
    ["Pongal is a popular festival of which state?", ["Karnataka", "Kerala", "Andhra Pradesh", "TAMIL NADU"]],
    ["Ghototkach in Mahabharat was the son of...?", ["Duryodhana", "BHIMA", "Arjuna", "Yudhishthir"]]
]

medium = [
    ["Who is the CEO of Google?", ["Satya Nadela", "Divyanshu Khandelwal", "SUNDAR PICHAI", "Jeff Bezos"]],
    ["Who is the owner of Amazon?", ["JEFF BEJOS", "Mukesh Ambani", "Elon Musk", "Tim Cook"]],
    ["Creta is a car of which company?", ["Maruti Suzuki", "HYUNDAI", "Ford", "Honda"]],
    ["Android Belongs to which company", ["GOOGLE", "Tesla", "Microsoft", "It is an Independent Company"]],
    ["Which WiFi company is available in Rohta?", ["Jio Fiber", "Airtel Xtreme", "Timble", "NONE OF THESE"]],
]

hard = [
    ["Who was the SECOND man landed on Moon?", ["Neil Armstrong", "BUZZ ALDRIN", "Edmond Halley", "Donald Slayton"]],
    ["Who was the Vice President of America in 2017?",
     ["Donald J. Trump", "Mike PomPeo", "JOE BIDEN", "Kamala Harris"]],
    ["What was the name of the Mission NASA sent on Saturn?", ["CASSINI", "ShaniYaan", "S.O.M", "H. Herschel"]],
    ["Whats is the name of the Black Hole at the centre of our Milky Way?",
     ["TON 618", "SAGITTARIUS A*", "M87", "Photobomb"]]
]

# ===================================================== LEVEL 1 ========================================================

while True:

    level_1 = []  # Isme level 1 ke 5 QUESTIONS hn
    level_2 = []  # Isme level 2 ke 3 QUESTIONS hn
    level_3 = []  # Isme level 3 ke 2 QUESTIONS hn

    score1 = 0
    score2 = 0
    score3 = 0

    try:

        for game1 in range(0, 5):
            qn = choice(easy)
            level_1.append(qn)
            easy.remove(qn)

            print(
                f"Question {game1 + 1} :-  {level_1[game1][0]} \n\n 1. {level_1[game1][1][0].title()} \n 2. {level_1[game1][1][1].title()}"
                f" \n 3. {level_1[game1][1][2].title()} \n 4. {level_1[game1][1][3].title()}\n")
            ans = int(input(">>> "))

            if level_1[game1][1][ans - 1] == level_1[game1][1][ans - 1].upper():
                print("And This is the RIGHT ANSWER!!🥳🥳🥳\n")
                score1 += 1

            else:
                Beep(320, 345)
                print("Ohh Hoo... Ye GALAT JAWAB hai😓😓😓\n")


    except:
        MessageBeep()
        print("Something Is Wrong level-1... Try Again!!...")

    # ===================================================== LEVEL 2 ====================================================

    if score1 >= 3:
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> LEVEL 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
        try:

            for game2 in range(0, 3):
                qn2 = choice(medium)
                level_2.append(qn2)
                medium.remove(qn2)

                print(
                    f"Question {game2 + 1} :-  {level_2[game2][0]} \n\n 1. {level_2[game2][1][0].title()} \n 2. {level_2[game2][1][1].title()}"
                    f" \n 3. {level_2[game2][1][2].title()} \n 4. {level_2[game2][1][3].title()}\n")
                ans2 = int(input(">>> "))

                if level_2[game2][1][ans2 - 1].upper() == level_2[game2][1][ans2 - 1]:
                    print("And This is the RIGHT ANSWER!!\n")
                    score2 += 1

                else:
                    Beep(320, 345)
                    print("Ohh Hoo... Ye GALAT JAWAB hai\n")


        except:
            MessageBeep()
            print("Something Is Wrong level-2 ... Try Again!!...")

    else:
        print(f"Your Score on Level-1 is {score1}\n")

        print("We are Sorry to inform you that you didn't scored enough to reach Level-2...\n")
        print("BETTER LUCK NEXT TIME...\n")
        print("F - First")
        print("A - Attempt")
        print("I - In")
        print("L - Life")
        print(line)
        break

    # ===================================================== LEVEL 3 ====================================================

    if score2 >= 2:
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> LEVEL 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
        try:

            for game3 in range(0, 2):
                qn3 = choice(hard)
                level_3.append(qn3)
                hard.remove(qn3)

                print(
                    f"Question {game3 + 1} :-  {level_3[game3][0]} \n\n 1. {level_3[game3][1][0].title()} \n 2. {level_3[game3][1][1].title()}"
                    f" \n 3. {level_3[game3][1][2].title()} \n 4. {level_3[game3][1][3].title()}\n")
                ans3 = int(input(">>> "))

                if level_3[game3][1][ans3 - 1].upper() == level_3[game3][1][ans3 - 1]:
                    print("And This is the RIGHT ANSWER!!\n")
                    score3 += 1

                else:
                    Beep(320, 345)
                    print("Ohh Hoo... Ye GALAT JAWAB hai\n")
                    pass

        except:
            MessageBeep()
            print("Something Is Wrong level -3 ... Try Again!!...")
            pass

    else:
        print(f"Your Score on Level-1 is {score1}\n")
        print(f"Your Score on Level-2 is {score2}\n")

        print("We are Sorry to inform you that you didn't scored enough to reach Level-3... Don't Worry... \n")

        print("BETTER LUCK NEXT TIME...\n")
        print("F - First")
        print("A - Attempt")
        print("I - In")
        print("L - Life")

        print(line)
        break

    if score3 >= 1:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t YOU * WON * THE GAME!! \n")

    else:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t YOU * LOST * THE GAME!! \n")

    break
