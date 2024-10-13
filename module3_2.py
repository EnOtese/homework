def send_email(message, recipient, *, sender="university.help@gmail.com"):
    domain = ".com", ".ru", ".net"
    check_dog = False
    check_domain_r = False
    check_domain_s = False
    for i in domain:
        if i in recipient:
            check_domain_r = True
        if i in sender:
            check_domain_s = True
    if "@" in recipient or sender:
        check_dog = True
    if check_domain_s == False or check_domain_r == False or check_dog == False:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if recipient == sender:
        return print('Нельзя отправить письмо самому себе!')
    if sender == "university.help@gmail.com":
        return print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        return print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
