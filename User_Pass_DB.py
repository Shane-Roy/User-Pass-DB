# Username_Password Database Program v.1
# By Shane Roy
# Created on 7/13/2021
from tabulate import tabulate  # Module used to make a table

db_users = [['Username']]  # Header for the username row on DB
db_passwords = [['Password']]  # Header for the password row on DB


def show_db():  # Function to display the database to the user
    show_db_yes_no = str(input("Do you want to view the db? [y/n]: ")).lower()  # View the current DB YES or NO
    if show_db_yes_no == 'y':
        print(tabulate(db_users, headers='firstrow', tablefmt='fancy_grid', showindex=True, missingval='N/A'))
        print(tabulate(db_passwords, headers='firstrow', tablefmt='fancy_grid', showindex=True, missingval='N/A'))
    else:
        pass
    main()


def final_input_to_db():
    # Final pass to adding content to DB, this is where the DB takes it's actual input of usernames and passwords
    # to store
    db_username_input = [str(input("Enter a username: "))]  # Official username to pass
    db_password_input = [str(input("Enter a password: "))]  # Official password to pass
    add_username_to_db = db_users.append(db_username_input)  # Append user-given name to DB
    add_password_to_db = db_passwords.append(db_password_input)  # Append user-given password to DB


def take_db_input():  # Function for adding content to DB
    x_to_db_entries = int(input("Enter an integer for how many additions to the db you would like to make [1-100]: "))
    db_users.clear()
    db_passwords.clear()
    db_users.append(['Username'])
    db_passwords.append(['Password'])
    if x_to_db_entries == 1:  # Single entry via user decision
        final_input_to_db()
    elif x_to_db_entries >= 2:  # Multiple entries via user decision
        for i in range(x_to_db_entries):
            print("")
            final_input_to_db()
    else:
        print("Entry unknown, returning to main menu.")  # Unknown entry given, return to main menu
        main()


def main():  # Intro to the program
    print("")
    print("=========")
    print("Main menu")
    print("=========")
    print("User_Pass_DB Program v.1")
    print("")
    view_option = str(input("View current DB or continue? [v/c]: "))  # View DB or continue with program
    if view_option == 'v':
        show_db()
    main_menu_question = str(input("Are you reading, creating or exporting a DB file? [r/c/e]: ")).lower()
    if main_menu_question == 'r':  # Read choice
        read_create()
    if main_menu_question == 'c':  # Create choice
        read_create()
    if main_menu_question == 'e':  # Export choice
        export()
    else:
        exit_or_not = str(input("Seems like you chose an incorrect option, do you want to quit? [y/n]: ")).lower()
        if exit_or_not != 'n':
            exit()
        else:
            main()


def export():  # Export the DB file to a local directory
    export_db = str(input("Would you like to export the DB to a file? [y/n]: ")).lower()
    if export_db == 'y':
        export_file_name_type = str(input("Enter the file name and type [.db, .txt, .csv, ect]: "))  # File name choice
        f = open(export_file_name_type, "w")  # Write given file name to said file
        # Below here the code starts the writing process, where the DB is exported to the chosen file
        f.write(str(db_users))
        f.write(str("\n"))
        f.write(str(db_passwords))
        f.close()
        main()
    main()


def read_create():  # This function controls the file operation
    rc_confirm = str(input("Please confirm- read or create a file? [r/c]: ")).lower()  # READ/CREATE
    if rc_confirm == 'r':  # READ choice, open a file and read it
        ask_r = str(input("What is the name of the file to read from your current directory? [example: file.txt]: "))
        f = open(ask_r, "r")
        print(f.read())
        f.close()
        str(input("File read, press enter to continue: "))
        main()
    if rc_confirm == 'c':  # CREATE choice, pick a name for the file and create it
        ask_c = str(input("What is the name of the file you want to create? [example.db, .txt, .csv, ect]: "))
        f = open(ask_c, "w")
        take_db_input()
        f.write(str(db_users))
        f.write(str("\n"))
        f.write(str(db_passwords))
        f.close()
        rc_ask_c_view_db = str(input("File created and written to, view DB or continue? [v/c]: ")).lower()
        if rc_ask_c_view_db == 'v':
            show_db()
        if rc_ask_c_view_db == 'c':
            pass
        main()

    else:
        invalid_option = str(input("Invalid option, return to main menu or continue operation? [r/c]: "))
        if invalid_option == 'r':
            main()
        if invalid_option == 'c':
            read_create()
    main()


main()
