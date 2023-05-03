# Homework 4
new_data = input("Введіть дані ")
# Перевірка чи введене число
if new_data.isdigit():
    print("You entered digits")
    if int(new_data) % 2 == 0:
# Перевірка на парність числа
        print("This is an even number")
    else:
        print("This number is odd")
# Перевірка чи введені дані це текст
elif new_data.isalpha():
    print("You entered letters")
    print("The word you entered consists of", len(new_data), "letters")
# Закінчення в разі введення комбінації тексту і цифр
else:
    print("You entered digits with letters")
### В процесі виникло питання - обчислення довжини рядка можна було зробити окремою змінною
### умовно l = len(new_data), а потім виводити l - це має сенс чи це просто лишня нагрузка?

