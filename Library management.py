class library:

    def __init__(self, books, name) -> None:
        self.books = books
        self.name = name
        self.booknotavailable = {}

    def display(self):
        print("Books are:")
        j = 1
        for i in self.books:
            print(f" {j}.{i}")
            j = j+1

    def lend(self):
        nameofper = input("Enter your name:")
        print(f"Mr. {nameofper}, you can lend these books,")
        self.display()
        lendbook = int(input("Enter which book do you want to lend:"))
        if self.booknotavailable.keys().__contains__(self.books[lendbook-1]):
            print(
                f"The book with name {self.books[lendbook-1]} is with {self.booknotavailable[self.books[lendbook-1]]}")
        else:
            print(
                f"Now, you can use book with name {self.books[lendbook-1]} ")
            self.booknotavailable.update(
                {self.books[lendbook-1]: nameofper})

    def add(self):
        addbook = input("Enter the name of book:")
        print(
            f"Now, we have successfully added your book with name {addbook}")
        self.books.append(addbook.capitalize())

    def returnB(self):
        enterName = input("Enter your name:")
        for key, value in self.booknotavailable.items():
            if value == enterName:
                print(f"We think you might have book named {key}")
                if input("Enter 'yes' to return:") == "yes":
                    usekey = key

        try:
            self.booknotavailable.pop(usekey)
        except:
            print()


E_library = library([
    " How To Win Friend And Influence People",
    " Ikigai: The Japanese Secret To A Long And Happy Life",
    " As A Man Thinketh",
    " The Rudest Book Ever",
    " Rich Dad Poor Dad",
    " Think And Grow Rich",
    " See You At The Top",
    " Thinking Fast And Slow",
    " The Alchemist"], "ReadMuch")


while(True):
    whatdowant = input(
        "What do you want:\n 1.Display books\n 2.Lend book\n 3.Add book\n 4.Return\n")

    if whatdowant == "1":
        E_library.display()
    elif whatdowant == "2":
        E_library.lend()
    elif whatdowant == "3":
        E_library.add()
    elif whatdowant == "4":
        E_library.returnB()
    else:
        print("You have only 4 options.")

    print("Press q to quit and c to continue")
    user_choice2 = ""
    while(user_choice2!="c" and user_choice2!="q"):
        user_choice2 = input()
        if user_choice2 == "q":
            exit()

        elif user_choice2 == "c":
            continue