"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
def credit(sum):
    sum += int(input('Введите сумму пополнения счёта: '))
    return sum

def purchase(sum, lst):
    price = int(input('Введите цену товара: '))
    if price > sum:
        print('Недостаточно денег на счёте!')
    else:
        good = input('Введите название товара: ')
        lst.append([good, price])
        sum -= price
    return sum, lst

def history(lst):
    print('История покупок', lst)

account = 0
goods = []
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        account = credit(account)
        print('Сумма на счёте = ', account)
    elif choice == '2':
        account, goods = purchase(account, goods)
        print('Сумма на счёте = ', account)
    elif choice == '3':
        history(goods)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
