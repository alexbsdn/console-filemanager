
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

def account_run():
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
            os.exit()
        else:
            print('Неверный пункт меню')
