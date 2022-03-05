import sys
# Open File
try:
    my_file = open("testfile.txt", "w")
except FileNotFoundError:
    print("Folder/file permissions prohibit creation/writing. Program aborted.")
    sys.exit()

# # Debug the Writing Logic in Your Console
# print("Here is a table of squares, squares, cubes, square roots\n"
#       "and cube roots of the first 20 positive integers: ")
#
# print("\n   k       k^3     sqrt k      cube rt k")
#
# for k in range(1, 21):
#     print(f"{k:4} {k ** 3:8d}  {k ** (1/2):9.3f} {k ** (1/3):10.3}")

my_file.write("Here is a table of squares, squares, cubes, square roots\n"
               "and cube roots of the first 20 integers:\n")
my_file.write("\n   k       k^2      k^3    sqrt k   cube rt k\n" )

for k in range(1, 21):
    my_file.write(f"{k:4} {k ** 2:8d} {k ** 3:8d} "
                  f"{k ** (1/2):9.3f} {k ** (1/3):10.3}\n")

try:
    my_file = open("testfile.txt", "a")
except FileNotFoundError:
    print("File not found. Program aborted.")
    sys.exit()

my_file.write("FootHill College")

try:
    my_file = open("birthday.txt", "r+")
except FileNotFoundError:
    print("File not found. Program aborted.")
    sys.exit()

my_file.write("Happy Birthday")

try:
    my_file = open("testfile.txt", "r")   #Open file and read "r"
except FileNotFoundError:
    print("File not found. Program aborted.")
    sys.exit()

# read and display each line, careful to suppress print()'s newline
for next_line in my_file:
    print(next_line, end='')    #'\n' already in text file line
                                  # \n is included in a file read of one line


# always close when done with a file
my_file.close()


"""
2nd Parameter	Operators
'r'             (or nothing)	open file for reading. (default artument is 'r' )
'a'	            open file for appending - writes to end of existing data without erasing prior file
'r+'	        open file for both reading and writing
'rb'	        open file for reading in binary mode. Every character is read as-is. That is, '\n', '\r' and non-printable characters are included in read data, if present and no end of line characters are added to returned lines
'wb'	        open files for writing in binary mode.
'r+b'	        open files for reading and writing in binary mode.
"""