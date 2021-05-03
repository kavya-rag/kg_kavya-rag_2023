import sys

mapper = {
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine",
    0:"Zero",
}


input = list(sys.argv)[1:]

out = ""

for i in range(len(input)):
    number = str(input[i])
    for digit in number:
        out += mapper[int(digit)]
    if i != len(input) - 1:
        out += ","

print(out)
