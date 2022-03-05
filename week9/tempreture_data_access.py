import sys

try:
    my_file = open("temperature_data.cvs", "a")
except FileNotFoundError:
    print("File can not be found, action aborted.")
    sys.exit()

my_string = "25:37:42:95"
my_list = my_string.split(":")
for item in my_list:
    my_file.write("\n")
    my_file.write(f"{item}, ")

try:
    my_file = open("temperature_data.cvs", "r")
except FileNotFoundError:
    print("File can not be found, action aborted.")
    sys.exit()

for next_line in my_file:
    print(next_line, end='')

my_file.close()
