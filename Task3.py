user_number = int(input('Введите число'))
ost = ''
while user_number >0:

    ost = str(user_number % 2) + ost
    user_number = user_number //2
print(ost)

