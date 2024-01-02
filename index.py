# Пользователь вводит строку, состоящую только из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся
# строку
input_string = input("Enter two words (use space): ")
words = input_string.split()

if len(words) == 2:
    reversed_string = " ".join([words[1], words[0]])
    print(reversed_string)
else:
    print("Error! Enter two words, not more!")

# Наступил Новый год, а Вася все еще ставит в документе прошедший, 2020, год.
# Помогите автоматизировать процесс замены номера старого года на новый. Используйте для
# решения метод replace()
input_text = input("Enter ur str with year: ")
oldOne = "2020"
newOne = "2021"
updatedStr = input_text.replace(oldOne, newOne)

print(updatedStr)

# Петя решил подвести итоги четверти и посчитать, сколько он получил пятерок,
# четверок, троек и двоек. Пользователь вводит список цифр через пробел. В первой строке вам
# необходимо вывести количество пятерок, четверок, троек и двоек через пробел. Во второй –
# средний балл Васи
grades = list(map(int, input("Enter vasya's grades: ").split()))

fiveCounter = grades.count(5)
fourCounter = grades.count(4)
threeCounter = grades.count(3)
twoCounter = grades.count(2)
avgGrade = sum(grades) / len(grades) if len(grades) > 0 else 0

print(f"{fiveCounter} {fourCounter} {threeCounter} {twoCounter}")
print(avgGrade)

# Петя очень умный школьник, и поэтому уверен, что оценки в жизни не главное! И,
# чтобы доказать это всем, он придумал план: заменить свои плохие оценки на хорошие. А
# чтобы было не очень заметно, Петя решил заменить двойки на трояки. Да вот одна проблема:
# оценок много, а времени мало. Помогите мальчику автоматизировать процесс
grades = input("Enter vasya's grades: ")

two = "2"
three = "3"
updatedList = grades.replace(two, three)

print(updatedList)


# Шифр Цезаря
def caesarKiller(msg, shift):
    shifr_DAZHI = ""
    for char in msg:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
            if is_upper:
                shifted = shifted.upper()
            shifr_DAZHI += shifted
        else:
            shifr_DAZHI += char
    return shifr_DAZHI


shift = int(input("Enter shift: "))
input_text = input("Your message: ")

result = caesarKiller(input_text, shift)
print("Shhhhhh!!!:", result)
