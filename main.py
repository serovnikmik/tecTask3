FILENAME1 = "ex.txt"
FILENAME2 = "ex2.txt"
FILENAME3 = "ex3.txt"

def check_for_10(data):
    for i in data:
        if i == 10:
            return True
    return False


def min_number(data):
    return min(data)


def max_number(data):
    return max(data)


def sum_of_numbers(data):
    current_sum = 0
    for i in data:
        try:
            current_sum += i
        except OverflowError:
            return OverflowError
    return current_sum


def comp_of_numbers(data):
    current_comp = 1
    for i in data:
        try:
            current_comp *= i
        except OverflowError:
            return OverflowError
    return current_comp


file = open(FILENAME1, "r")
all_numbers = []
for line in file:
    numbers = map(int, line.split(" "))
    all_numbers += numbers
file.close()

print("minimal number: " + str(min_number(all_numbers)))
print("maximal number: " + str(max_number(all_numbers)))
SUM = 0
try:
    SUM = sum_of_numbers(all_numbers)
    print("summary of all numbers is: " + str(SUM))
except OverflowError:
    print("Summary of all numbers is more than python can hold")

COMP = 0
try:
    COMP = comp_of_numbers(all_numbers)
    print("composition of all numbers is: " + str(COMP))
except OverflowError:
    print("Composition of all numbers is more than python can hold")

print("-=-=-=-=-=-=-=-=-=-END-=-=-=-=-=-=-=-=-=-")