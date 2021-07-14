# User_Pass_DB
Python 3 Database to store Usernames and Passwords

This program essentially makes a list of lists in Python and is easy to use.
Lists may be viewed in table format, and have a header for the rows "Usernames" and "Passwords".

The options are:
-read a DB from a folder
-create/export a DB to a folder
-view the current DB stored to the program

Must have tabulate installed.
https://pypi.org/project/tabulate/

''' Installation
To install the Python library and the command line utility, run:

pip install tabulate
The command line utility will be installed as tabulate to bin on Linux (e.g. /usr/bin); or as tabulate.exe to Scripts in your Python installation on Windows (e.g. C:\Python27\Scripts\tabulate.exe).

You may consider installing the library only for the current user:

pip install tabulate --user
In this case the command line utility will be installed to ~/.local/bin/tabulate on Linux and to %APPDATA%\Python\Scripts\tabulate.exe on Windows.

To install just the library on Unix-like operating systems:

TABULATE_INSTALL=lib-only pip install tabulate
On Windows:

set TABULATE_INSTALL=lib-only
pip install tabulate '''

Use python3 ./User_Pass_DB.py to start program
