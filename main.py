


def book_number():
    number = int(input("Enter a number: "))
    print("The number is negative: ", number < 0)
    print("The number is even: ", number % 2 == 0)
    print("The number of digits in the number is equal to ", len(str(number)))
    print("The number is expanded", str(number)[::-1])
    print("The sum of the digits of the number is equal to", sum([int(i) for i in str(number)]))

    first_digit, last_digit = int(str(number)[0]), int(str(number)[-1])
    print("The first digit of the number: ", first_digit)
    print("The last digit of the number: ", last_digit)
    print("The sum of the first and last digits of the number: ", first_digit + last_digit)



def book_number_2():
    number, number2 = int(input("Enter a number: ")), int(input("Enter a number 2: "))
    print("The first digits of the numbers are the same: ", str(number)[0] == str(number2)[0])
    print("The first number divides the second number without remainder: ", number % number2 == 0)
    print("The first number is divided by the second number, the remainder is equal to: ", number % number2)



def book_line():
    line = input("Enter the line: ")
    print("Line length:", len(line))
    print("The first three characters of the string:", line[:3])
    print("The last three characters of the string:", line[-3:])
    print("Characters of a string with even indexes:", line[::2])
    print("The line is inverted:", line[::-1])
    print("The index of the first zero in the row is", line.find('0'))
    print("A string without duplicated characters:", ''.join(set(line)))
    if line[-1] != 'ь':
        print("The last character of the string:", line[-1])
    elif len(line) > 1:
        print("The penultimate character of the string:", line[-2])
    print(*[i for i in line][::-1])


def book_line_2():
    line, line2 = input("Enter the line: "), input("Enter the line 2: ")
    print("The first characters in the lines are the same: ", line[0] == line2[0])



def book_scroll():
    scroll = [i for i in range(10, 1000)]
    print(scroll[:3])
    print(scroll[2:-1])
    print(scroll[-2:])
    print(scroll[::2])
    print([i * 1.1 for i in scroll])
    print("Numbers with the sum of the first and second digits equal to five:", *[i for i in scroll if int(str(i)[0]) + int(str(i)[1]) == 5])
    del_symbol = int(input("Enter a character, it will be deleted:"))
    print([i for i in scroll if i != del_symbol])
    scroll = ['http://Putin.ru', 'http://lider.com', 'bole.ru', 'http://country.ru', 'Russia.org']
    print([i for i in scroll if i[:7] == "http://"])
    line_scroll = input("Enter the line: ")
    print(list(line_scroll))
    number_scroll = input("Enter the number: ")
    print([int(i) for i in number_scroll])



def book_glossary():
    glossary = {'year' : '2025', 'month': '12', 'day'  : '31',}
    print(glossary['year'], glossary['month'], glossary['day'], sep='-')
    glossary = {'a': 1, 'b': 2, 'c': 3, 'd': 4,}
    print("The sum of the elements of this dictionary is equal to", sum(glossary.values()))
    print("The sum of the squares of the elements of this dictionary is equal to", sum([i ** 2 for i in glossary.values()]))
    for key, value in glossary.items():
        glossary[key] = value * 2
    print(glossary)



def book_kit():
    kit = input("Enter the line: ", )
    print(set(kit))



def book_cortege():
    cortege = (1, 2, 3, 4, 5)
    print(sum(cortege))



def book_total():
    spam = [i for i in range(-100, 101)]
    print("The sum of all the numbers is equal to ", sum(spam))
    print("The sum of all even numbers is equal to ", sum([i for i in spam if i % 2 == 0]))
    print("The sum of all odd numbers is equal to ", sum([i for i in spam if i % 2 != 0]))
    print("The sum of the list items is equal to", sum(spam))
    print("The sum of the squares of the list items is equal to", sum([i ** 2 for i in spam]))
    print("The sum of the square roots of the list items is", sum([i ** 0.5 for i in spam]))
    print("The sum of the positive elements of the list is equal to", sum([i for i in spam if i > 0]))
    print("The  sum of the values of the list items in the range [0, 10] is equal to", sum([i for i in spam if i > 0 and i < 10]))



def book_spam():
    spam = [i for i in range(101)]
    spam2 = [i for i in range(-100, 1)]
    print(*spam)
    print(*spam2)
    print(*spam[::-1])
    print(*[i for i in spam if i % 2 == 0])
    print(*[i for i in spam if i % 3 == 0])



if __name__ == '__main__':

    key = int(input("Enter the key: "))

    if key == 1:
        book_number() # working with a number
    if key == 2:
        book_number_2() # working with two numbers
    if key == 3:
        book_line() # working with a string
    if key == 4:
        book_line_2() # working with two lines
    if key == 5:
        book_scroll() # working with the list
    if key == 6:
        book_glossary() # working with the dictionary
    if key == 7:
        book_kit() # working with sets
    if key == 8:
        book_cortege() # working with tuples
    if key == 9:
        book_total() # working with the results
    if key == 10:
        book_spam() # dealing with spam
    #2_2_1_https://code.mu/ru/python/tasker/stager/2/2/