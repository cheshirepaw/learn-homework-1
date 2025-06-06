"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    try:
        while True:
            user_state = input('Как дела?\n')
            if user_state == 'Хорошо':
                print('Рад за тебя!')
                break
            elif user_state.lower() == 'хорошо':
                print('Обмануть меня вздумал? Отвечай нормально!\n')
            else:
                print('Ну ладно, поехали дальше\n')
    except KeyboardInterrupt:
        print('Пока!')
    
if __name__ == "__main__":
    hello_user()
