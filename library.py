def list_books():

    #lists books with their informations

    books = open("books.txt", "r")
    for book in books:
        book_info = book.split(",")
        print("""
        
        Name: {}
        Author: {}
        ISBN number: {}
        Checked: {}
        """.format(book_info[1], book_info[2], book_info[0], book_info[3]))
    books.close()


def checked_books():

    #lists books which checked out with their information

    books = open("books.txt", "r")
    for book in books:
        book = book[:-1]
        book_info = book.split(",")
        if book_info[3] == "T":
            print("""

            Name: {}
            Author: {}
            ISBN number: {}
            """.format(book_info[1], book_info[2], book_info[0]))
    books.close()


def add_book(book_ISBN,book_name,author,check = "F"):

    #adds a book with given information to the list of books

    book_introduction = book_ISBN,book_name,author,check
    book_introduction = ",".join(book_introduction)

    books = open("books.txt","a")
    books.write(book_introduction+"\n")
    print("[The book was added.]")
    books.close()


def search_ISBN(ISBN):

    #If ISBN number in the list of books, searchs and shows the book which has same ISBN number with its informations

    books = open("books.txt","r")
    allbooks = books.read()
    if ISBN not in allbooks:
        print("[There is not a book with '{}' ISBN number...]".format(ISBN))
    else:
        books = open("books.txt", "r")
        for book in books:
            book_introduction = book.split(",")
            if ISBN == book_introduction[0]:
                print("""
                
                Name: {}
                Author: {}
                ISBN number: {}
                Checked: {}
                
                """.format(book_introduction[1],book_introduction[2],book_introduction[0],book_introduction[3]))
    books.close()


def search_book_name(book_name):

    #searchs books by a name and shows all a book/books which contains the name

    books = open("books.txt","r")
    for book in books:
        book = book.split(",")
        if book_name.upper() in book[1].upper():
            print("""
            Name: {}
            Author: {}
            ISBN number: {}
            Checked: {}
            """.format(book[1],book[2],book[0],book[3]))
    books.close()


def changing(ISBN_number):

    #changes book's check out information which is checked out to 'T'

    #writing changed form to the rebooks.txt
    rebooks = open("rebooks.txt","w")
    books = open("books.txt","r")

    for book in books:
        book = book[:-1]
        book_info = book.split(",")
        if book_info[0] == ISBN_number:
            book_info[3] = "T"
            book = ",".join(book_info)
            rebooks.write(book+"\n")
        else:
            book = ",".join(book_info)
            rebooks.write(book+"\n")
    rebooks.close()
    books.close()

    #rewriting to the books.txt
    books = open("books.txt","w")
    rebooks = open("rebooks.txt","r")

    for rebook in rebooks:
        books.write(rebook)

    books.close()
    rebooks.close()


def check_out_book(ISBN_number,student_ID):

    #If the given informations are true and book is available, checks out the book to the student

    books = open("books.txt","r")
    students = open("students.txt","r",encoding="utf-8")

    if student_ID in students.read():
        if ISBN_number in books.read():
            books = open("books.txt", "r")
            for book in books:
                book = book[:-1]
                book_info = book.split(",")
                if ISBN_number == book_info[0]:
                    if "F" == book_info[3]:

                        check_out = open("check_out.txt","a")
                        check_out.write(ISBN_number+","+student_ID+","+"C"+"\n")
                        changing(ISBN_number)
                        print("[Checking out is completed.]")
                        check_out.close()

                    else:
                        print("[You cannot check out this book.]")
        else:
            print("[Cannot find the book...]")
    else:
        print("[Cannot find the student...]")

    books.close()
    students.close()


def return_changing(ISBN_number):

    #changes book's check out information which is returned to 'F'

    #writing changed form to the rebooks.txt
    rebooks = open("rebooks.txt","w")
    books = open("books.txt","r")

    for book in books:
        book = book[:-1]
        book_info = book.split(",")
        if book_info[0] == ISBN_number:
            book_info[3] = "F"
            book = ",".join(book_info)
            rebooks.write(book+"\n")
        else:
            book = ",".join(book_info)
            rebooks.write(book+"\n")
    rebooks.close()
    books.close()

    #rewriting to the books.txt
    books = open("books.txt","w")
    rebooks = open("rebooks.txt","r")

    for rebook in rebooks:
        books.write(rebook)

    books.close()
    rebooks.close()


def return_book(ISBN_number,student_ID):

    #If the book checked out with the same student before, returns the book to library

    books = open("books.txt","r")
    students = open("students.txt","r",encoding="utf-8")
    check_out = open("check_out.txt","r")

    if student_ID in students.read():
        for book in books:
            book = book[:-1]
            book_info = book.split(",")
            if ISBN_number == book_info[0]:
                if "T" == book_info[3]:

                    check_out.close()
                    check_out = open("check_out.txt","a")
                    check_out.write(ISBN_number+","+student_ID+","+"R"+"\n")
                    print("[Returning is completed.]")
                    check_out.close()

                    return_changing(ISBN_number)

                else:
                    print("[You cannot return this book.]")
    else:
        print("[Cannot find the student...]")

    books.close()
    students.close()


def list_students():

    #Lists all students with information which checked out books

    students = open("students.txt","r",encoding="utf-8")
    check_outs = open("check_out.txt", "r")
    books = open("books.txt","r")

    for student in students:
        student = student[:-1]
        student_info = student.split()

        print("""
        Full Name : {} {}
        Student ID : {}""".format(student_info[1],student_info[2],student_info[0]))

        for check_out in check_outs:
            check_out = check_out[:-1]
            check_out_info = check_out.split(",")
            if student_info[0] == check_out_info[1]:
                for book in books:
                    book = book[:-1]
                    book_info = book.split(",")
                    if check_out_info[0] == book_info[0] and check_out_info[2] == "C":

                        print("""
        {} - {}/{}""".format(book_info[0],book_info[1],book_info[2]))
                    books = open("books.txt","r")
            check_outs = open("check_out.txt", "r")
    students.close()
    check_outs.close()
    books.close()


def most_checked_books():

    #checks check_out.txt and find and shows top 3 most checked out books

    #checks all checked books' number which is checked out from any student
    check_out = open("check_out.txt","r")
    checks = check_out.readlines()

    check_numbers = []
    checks_dict = {}
    for check in checks:
        check = check[:-1]
        check = check.split(",")

        counter = 0
        for recheck in checks:
            recheck = recheck[:-1]
            recheck = recheck.split(",")
            if check[0] == recheck[0] and check[2] == recheck[2] == "C":
                counter += 1

        check_numbers.append(counter)
    check_numbers_new = check_numbers
    check_out.close()

    #organizes all checked books and their numbers as dictionary
    check_out = open("check_out.txt","r")
    for check in check_out:
        check = check[:-1]
        check_info = check.split(",")
        for number in check_numbers_new:
            checks_dict[check_info[0]] = number
            check_numbers_new.pop(0)
            break
    check_out.close()

    #organizes dictionary's values and keys
    values = []
    for index in checks_dict.values():
        values.append(index)

    keys = []
    for j in checks_dict:
        keys.append(j)

    values_new = values

    #finds top 3 checked out books' indexes
    indexes = []
    for maxs in range(3):
        max_index = values_new.index(max(values_new))
        if max(values_new) == 0:
            break
        else:
            values_new.pop(max_index)
            values_new.insert(max_index, 0)
        indexes.append(max_index)

    #finds out books with indexes and shows top 3 checked books
    n = 0
    for index in indexes:
        top_number = 1 + n
        books = open("books.txt", "r")
        for book in books:
            book = book[:-1]
            book_info = book.split(",")
            if book_info[0] == keys[index]:
                print("""
                -TOP {}-
                ISBN: {} 
                Book's Name: {}
                Book's Author: {}
                """.format(top_number, book_info[0], book_info[1], book_info[2]))
        n += 1
    books.close()


def most_checked_students():

    #checks check_out.txt and find and shows top 3 students with the highest checked out numbers

    #checks all students' checked out numbers which were checked out any book
    check_out = open("check_out.txt", "r")
    checks = check_out.readlines()

    check_numbers = []
    checks_dict = {}
    for check in checks:
        check = check[:-1]
        check = check.split(",")

        counter = 0
        for recheck in checks:
            recheck = recheck[:-1]
            recheck = recheck.split(",")
            if check[1] == recheck[1] and check[2] == recheck[2] == "C":
                counter += 1

        check_numbers.append(counter)
    check_numbers_new = check_numbers

    # organizes all students which were checked books and their checked out numbers as dictionary
    check_out = open("check_out.txt", "r")
    for check in check_out:
        check = check[:-1]
        check_info = check.split(",")
        for number in check_numbers_new:
            checks_dict[check_info[1]] = number
            check_numbers_new.pop(0)
            break

    #organizes dictionary's values and keys
    values = []
    for index in checks_dict.values():
        values.append(index)

    keys = []
    for j in checks_dict:
        keys.append(j)

    values_new = values

    #finds top 3 students' indexes
    indexs = []
    for maxs in range(3):
        max_index = values_new.index(max(values_new))
        if max(values_new) == 0:
            break
        else:
            values_new.pop(max_index)
            values_new.insert(max_index, 0)
        indexs.append(max_index)

    #finds out students with indexes and shows top 3 students
    n = 0
    for index in indexs:
        top_number = 1 + n
        students = open("students.txt","r",encoding="utf-8")
        for student in students:
            student = student[:-1]
            student_info = student.split()
            if student_info[0] == keys[index]:
                print("""
                -TOP {}-
                Student's ID: {} 
                Student's Full Name: {} {}
                """.format(top_number, student_info[0], student_info[1], student_info[2]))
        n += 1
    check_out.close()
    students.close()

while True:
    print("""
    ________________________________________________________________________
    |                                                                      |
    |                        <<<LIBRARY OPTIONS>>>                         |
    |                                                                      |
    | 1- List all books                                                    |
    | 2- List all the books that are checked out                           |
    | 3- Add a new book                                                    |
    | 4- Search a book by ISBN number                                      | 
    | 5- Search a book by name                                             |
    | 6- Check out a book to a student                                     |
    | 7- Return a book from a student                                      |
    | 8- List all the students                                             |
    | 9- List top 3 most checked out books                                 |
    | 10- List top 3 students with the highest checked out numbers -       |
    |                                                                      |
    | [QUIT (q)]                                                           |
    ------------------------------------------------------------------------
    """)

    process = input("Enter a process:")

    if process == "q":
        break

    elif process == "1":

        list_books()

    elif process == "2":

        checked_books()

    elif process == "3":

        book_name = input("Book's name:")
        author = input("Book's author:")
        ISBN_number = input("Book's ISBN number:")

        add_book(ISBN_number,book_name,author)

    elif process == "4":

        ISBN_number = input("ISBN number:")
        search_ISBN(ISBN_number)

    elif process == "5":

        search_name = input("Book's name:")

        search_book_name(search_name)

    elif process == "6":

        student_ID = input("Student ID:")
        ISBN_number = input("ISBN number:")

        check_out_book(ISBN_number, student_ID)

    elif process == "7":

        student_ID = input("Student ID:")
        ISBN_number = input("ISBN number:")

        return_book(ISBN_number,student_ID)

    elif process == "8":
        list_students()

    elif process == "9":
        most_checked_books()

    elif process == "10":
        most_checked_students()

    else:
        print("Enter a valid process...")
