# Homework 4
new_data = input("Введіть дані ")
# Check for digits
if new_data.isdigit():
    print("You entered digits")
    if int(new_data) % 2 == 0:
# Even - Odd check
        print("This is an even number")
    else:
        print("This number is odd")
# Letters check
elif new_data.isalpha():
    print("You entered letters")
    print("The word you entered consists of", len(new_data), "letters")
# Закінчення в разі введення комбінації тексту і цифр
else:
    print("You entered digits with letters")
### В процесі виникло питання - обчислення довжини рядка можна було зробити окремою змінною
### умовно l = len(new_data), а потім виводити l - це має сенс чи це просто лишня нагрузка?

