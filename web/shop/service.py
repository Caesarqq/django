from django.core.mail import send_mail


def send(user_email):
    # print('я работаю', send_mail)
    send_mail(
        'СПАМ',
        'aszxclkh@gamil.com',
        [user_email],
        fail_silently=False,
    )
