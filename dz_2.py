def send_email(message, recipient, *, sender="university.help@gmail.com"):
    len_recipient = len(recipient)
    len_sender = len(sender)
    if '@' in recipient and '@' in sender:
        if recipient[len_recipient - 4:len_recipient] == '.com' or recipient[len_recipient - 4:len_recipient] == '.net'\
                or recipient[len_recipient - 3:len_recipient] == '.ru' and sender[len_sender - 4:len_sender] == '.com' \
                or sender[len_sender - 4:len_sender] == '.net' or sender[len_sender - 3:len_sender] == '.ru':
            if sender == recipient:
                print('Нельзя отправить письмо самому себе!')
            elif sender != 'university.help@gmail.com':
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
