lis1 = ["Abhi", "Princi", "Papaji"]
lis2 = []
from time import sleep


class Library:

    def display():
        for a in lis1:
            print(a, end="\n")


    def add_book(name):
        lis1.append(name)
        print(f"Your Book {name} is added... Thank You")


    def lend_book(name_of_book):
        lis2.append(name_of_book)
        lis1.remove(name_of_book)
        print("Okk.. This book is now yours.. Thank You")


    def return_book(book_name):
        if book_name in lis2:
            print("okk.. Your book is returned now... Thank You")
            lis1.append(book_name)
            lis2.remove(book_name)

        else:
            print("Thei book is not in our list... Sorry")


try:
    while True:
        q = input(
            "Enter your choice:-\n1.. Display Books name\n2.. Add a Book\n3.. Lend a Book\n4.. Return a Book\n5.. Exit\n>>> ")

        if q == '1':
            Library.display()
            print("========================================================================")

        elif q == '2':
            name = str(input("Enter the name of Book you want to ADD:- "))
            Library.add_book(name)
            print("========================================================================")

        elif q == '3':
            if len(lis1) != 0:
                name_of_book = str(input("Enter the name of Book you want to LEND:- "))
                if name_of_book in lis1:
                    Library.lend_book(name_of_book)

                else:
                    print("Sorry... This book is not in our List..")
            else:
                print("Sorry... We don't have any book to give... please Visit another day... Thank You")
            print("========================================================================")

        elif q == '4':
            if len(lis2)!=0:
                for w in lis2:
                    print(w, end="\n")

                book_name = str(input("Enter the name of Book you want to RETURN:- "))
                Library.return_book(book_name)

            else:
                print("Their is no Book to Return... Thank You")
            print("========================================================================")

        elif q=='5':
            print("Okk.. Thank You... Have a nice day")
            sleep(3)
            break

        else:
            print("Somwthing is Wrong.. Try again!!...")
            print("========================================================================")
            continue

except:
    print("ERROR!!")

finally:
	print("Thanks for using our Library...")
