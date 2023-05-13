
# Homework 5.1
new_data = input('введіть дані: ')
n = 1
for analysed_symbol in range(0, len(new_data)):
    if new_data[analysed_symbol].isdigit():
        if int(new_data[analysed_symbol]) % 2 == 0:
            print(n, new_data[analysed_symbol], "This is an even number")
        else:
            print(n, new_data[analysed_symbol], "This is odd number")

    elif new_data[analysed_symbol].isalpha():
        if new_data[analysed_symbol].islower():
            print(n, new_data[analysed_symbol], "Letter in lower register")
        else:
            print(n, new_data[analysed_symbol], "Letter in upper register")

    else:
        print(n, new_data[analysed_symbol], "This is a symbol")
    n += 1
