# Task 2
from mybox import MyBox, FillBox

print('------------Task 2----------------')
lowercase_alphabet = {}
numbers = [i for i in range(1, 27)]
letters = [chr(letter) for letter in range(97, 123)]
for x in range(len(numbers)):
    lowercase_alphabet[letters[x]] = numbers[x]

try:
    check_letter = lowercase_alphabet['d']
    if check_letter:
        print(lowercase_alphabet)
except KeyError:
    print('This alphabet has only english lowercase letters!')

try:
    check_index = numbers[30]
    if check_index:
        print('Indexing is OK')
except IndexError:
    print('The length of this alphabet is 26 letters! That index is not here!')

try:
    if open("TestFile.txt", "r"):
        print('File was open successfully!')
except IOError:
    print("Error: File doesn't exist.")

# Task 3
print('------------Task 3----------------')
box = MyBox()
user = FillBox('Nate', 'Munday', '12.11.1985', 'France')
box.add(user)
user = FillBox('Alex', 'Brown', '12.12.2001', 'Spain')
box.add(user)
box.__contains__('Alex', 'Huge', '12.12.2001', 'Spain')
for data in box:
    print(data)
