#####################################################
# Library program for Unit 13 Assignment 2
# Written October 2020
# This code is to be fully tested in line with
# the test plan created for assignment 2.
#
# This is version 1 of the product.
# Extra functionality is not required in this version.
# Version 2 requirements will be covered in assignment 3.
#
# Please refer to separate MS Word document for the 
# user requirements specification.
#####################################################
import a2_library_functions as lib_func

book_file_path = "csv/a2-books-data-tab.txt"
dvd_file_path = "csv/a2-dvd-data-tab.txt"
members_file_path = "csv/a2-member-data.csv"

while True:
    print("""Please select an option:
    1 - Display all BOOKS in stock
    2 - Display all DVDs in stock
    3 - Display all MEMBERS of the library
    4 - Search for a DVD by title keyword
    5 - Search for a BOOK by title keyword  
    6 - Search for a MEMBER by name
    7 - Update member details""")

    user_selection = input()

    if user_selection == "1":
        lib_func.open_book_file(book_file_path)
    elif user_selection == 2:
        lib_func.open_dvd_file(dvd_file_path)
    elif user_selection == "3":
        lib_func.open_member_file(members_file_path)
    elif user_selection == "4":
        dvd_search = input("Please enter the a keyword search: ")
        lib_func.search_for_film_by_title(dvd_file_path, dvd_search)
    elif user_selection == "5":
        book_keyword = input("Please enter the a keyword search: ")
        lib_func.search_for_book_by_title(book_file_path, book_keyword)
    elif user_selection == "6":
        member_keyword = input("Please enter the a keyword search: ")
        lib_func.search_for_member_by_name(members_file_path, member_keyword)
    elif user_selection == "7":
        lib_func.update_member_details()
    else:
        print("Invalid selection")
