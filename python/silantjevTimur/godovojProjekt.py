print("Привет ты не можешь попасть в дом")
print("У тебя есть выбор либо пойти во двор либо попытаться зайти на крыльцо")
doroga = input("Ответьте крыльцо или двор: ")
while doroga != "крыльцо" and doroga != "двор":
    doroga = input("Ответьте крыльцо или двор: ")
if doroga == "крыльцо":
    print("Вы пришли на крыльцо вы не знаете как попасть домой но вы увидели коврик и кувшин куда вы посмотрите")
    doroga = input("Ответьте кувшин/коврик: ")
    while doroga != "кувшин" and doroga != "коврик":
         doroga = input("Ответьте кувшин/коврик: ")
    if doroga == "кувшин":
        print("Вы нашли 1 ключ но когда вы его вставили вас ударило током и вы умерли")
    elif doroga == "коврик":
        print("Вы заглядываете под коврик и находите 2 ключа")
        doroga = input("Ответьте первый ключ или второй ключ: ")
        while doroga != "первый ключ" and doroga != "второй ключ":
            doroga = input("Ответьте первый ключ или второй ключ: ")
        if doroga == "первый ключ":
            print("Поздравляю!!! Ты смог попасть домой")
        elif doroga == "второй ключ":
            print("К сожалению после попытки вставить ключ у твоего организма закончились силы и он сдох")
elif doroga == "двор":
    print('''Вы увидели мага он предложил сыграть вам в игру он будет
        загадывать число от 1 до трех и если вы дадите правильный ответ
        он даст вам ключ для входа в дом''')
    doroga = input("Маг говорит говори число один два или три: ")
    while doroga != "один" and doroga != "два" and doroga != "три":
        doroga = input("Маг говорит говори число один два или три: ")
    if doroga == "один":
        print("Когда ты вставлял ключ ты умер")
    elif doroga == "два":
        print("К сожалению когда ты вставлял ключ ты умер")
    elif doroga == "три":
        print("Поздравляю!!! Ты смог попасть домой!")
