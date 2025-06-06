"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        user_state = input('Как дела?\n')
        if user_state == 'Хорошо':
            print('Рад за тебя!')
            break
        elif user_state.lower() == 'хорошо':
            print('Обмануть меня вздумал? Отвечай нормально!\n')
        else:
            print('Ну ладно, поехали дальше\n')
    
if __name__ == "__main__":
    hello_user()
