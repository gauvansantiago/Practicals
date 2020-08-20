# Gauvan Santiago Prac_02 Task_04 files
# 1
# Creates a file named name.txt and asks for name input
out_file = open("name.txt", "w")
name = input("Enter your name: ")
# adds the name in the file name.txt
print(name, file=out_file)
out_file.close()


# 2
# Opens file named name.txt and prints the name in the text file
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# 3
#  Creates a text file called numbers.txt and adds the first two numbers
in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
# Prints both numbers and adds them together
print(number_1, number_2)
print(number_1 + number_2)

# 4
in_file = open("numbers.txt", "r")
total = 0
# adds the total of the numbers in numbers.txt file
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
