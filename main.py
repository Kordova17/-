print("Приветствую тебя, пользователь, в церковном калькуляторе")
name = input("Твое имя при крещении")
print("Храни вас Господь ," , name )

while True:

    act = input("Выберите действие: (+,-,,/,): ")
    if act in ('+', '-', '', '/' ):
        number1 =float(input("Страница ветхого завета= "))
        number2 = float(input("Страница нового завета= "))
        if act == '+':
            print("Ответ:", (number1 + number2))
        elif act == '-':
            print("Ответ:", (number1 - number2))
        elif act == '*':
            print("Ответ:", (number1 * number2))
        elif act == '/':
                print("И сказал Христос:", (number1 / number2))