def send_email(message, recipient, sender='university.help@gmail.com'):
    ending = ('.com', '.ru', '.net')
    a = '@' in recipient; b = '@' in sender; c = recipient.endswith(ending); d = sender.endswith(ending)
    if recipient == sender:
        print('Письмо нельзя отправить самому себе.')
    else:
        if a == False or b == False or c == False or d == False:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        else:
            if sender =='university.help@gmail.com':
                print('Письмо отправлено с адреса', sender, 'на адрес', recipient)
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)





send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



