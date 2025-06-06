"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_input = int(input('Введите ваш возраст '))
    def occupation(user_age):
        if (user_age < 6):
            return 'Детский сад'
        elif (user_age >= 6) and (user_age <18):
            return 'Школа'
        elif (user_age >= 18) and (user_age < 25):
            return 'Университет'
        else:
            return 'Работа'
    
    user_occupation = occupation(user_input)
    print(user_occupation)

if __name__ == "__main__":
    main()
