##########################################
# Functions to be used with U13 assignment
# 2 program.
#
# Written October 2020.
##########################################

def open_book_file(book_file_path):
    book_file = open(book_file_path, "r")
    book = book_file.read()
    print(book)
    book_file.close()


def open_dvd_file(dvd_file_path):
    dvd_file = open(dvd_file_path, "r")
    dvd = dvd_file.read()
    print(dvd)
    dvd_file.close()


def open_member_file(members_file_path):
    member_file = open(members_file_path, "r")
    member = member_file.read()
    print(member)
    member_file.close()


def search_for_film_by_title(dvd_file_path, dvd_keyword):
    film_file = open(dvd_file_path, "r")
    film_record = film_file.readline()
    counter = 0

    while film_record != "":
        field = film_record.split("\t")
        film_id = field[0]
        film_title = field[1]
        film_director = field[2]
        film_genre = field[3]
        film_certificate = field[4]
        if dvd_keyword.lower() in film_title.lower():
            counter += 1
            print(
                f"ID: {film_id}\nTitle: {film_title}\nDirector: {film_director}"
                f"\nGenre: {film_genre}\nRating: {film_certificate}")
        film_record = film_file.readline()
    if counter == 1:
        print(f"There is {counter} MEMBERS with '{dvd_keyword}' in the title.")
    else:
        print(f"There are {counter} DVDs with '{dvd_keyword}' in the title.")
    film_file.close()


def search_for_book_by_title(book_file_path, book_keyword):
    book_file = open(book_file_path, "r")
    book_record = book_file.readline()
    counter = 0

    while book_record != "":
        field = book_record.split("\t")
        book_id = field[0]
        book_author = field[1]
        book_title = field[2]
        book_publisher = field[3]
        book_genre = field[4].strip()
        if book_keyword.lower() in book_title.lower():
            counter += 1
            print(
                f"\nID: {book_id}\nTitle: {book_title}\nAuthor: {book_author}"
                f"\nPublisher: {book_publisher}\nGenre: {book_genre}")
        book_record = book_file.readline()
    print(f"\nThere are {counter} members with '{book_keyword}' in the title.")
    book_file.close()

def search_for_member_by_name(member_file_path, member_keyword):
    member_file = open(member_file_path, "r")
    member_record = member_file.readline()
    counter = 0

    while member_record != "":
        field = member_record.split(",")
        member_id = field[0]
        member_first_name = field[1]
        member_last_name = field[2]
        member_email_address = field[3]
        member_telephone_num = field[4]
        member_dob = field[5].strip()
        if (member_keyword.lower() in member_first_name.lower()) or (member_keyword.lower() in member_last_name.lower()):
            counter += 1
            print(
                f"\nID: {member_id}\nFirst name: {member_first_name}\nLast name: {member_last_name}\nEmail: {member_email_address}"
                f"\nTelephone Number: {member_telephone_num}\nDOB: {member_dob}")
        member_record = member_file.readline()
    print(f"\nThere are {counter} BOOKS with '{member_keyword}' in their name.")
    member_file.close()

def update_member_details():
    print(" \n##### FUNCTIONALITY NOT YET PROGRAMMED #####\n")

