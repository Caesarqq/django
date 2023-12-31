from django.core.mail import send_mail
from web.celery import app

from .service import send
from .models import Contact

"""
В представленном коде содержатся две Celery-задачи, которые отвечают за отправку уведомлений по электронной почте
в проекте Friendship Store.
"""
from web.celery import app
from django.contrib.auth.models import User
from django.core.mail import send_mail

import datetime


# @app.task
# def send_beat_email():
#     """
#     Эта задача отправляет электронное письмо каждому пользователю в базе данных.
#     Для отправки письма используется функция send_mail() из модуля django.core.mail.
#     В письме содержится приветствие с именем пользователя и информация о новом товаре в магазине.
#     В письме также присутствует ссылка на веб-сайт и заключительное сообщение от Friendship Skate Shop.
#     """
#     for user in User.objects.all():
#         send_mail(
#             'friendship',
#             f'Здравствуйте, {user.first_name}!\n\n'
#             'Мы рады представить вам новый товар, '
#             'который поступил в продажу в нашем магазине!\n'
#             'Чтобы ознакомится с ним переходите по ссылке:\n'
#             'http://www.friendship.ru\n\n'
#             'С наилучшими пожеланиями, Friendship Skate Shop.',
#             'friendship@mail.ru',
#             [user.email],
#             fail_silently=False,
#         )
#
#
# @app.task
# def order_notice(first_name, total_price, email):
#     """
#     Эта задача отправляет уведомление пользователю после успешной покупки.
#     Опять же, используется функция send_mail() для отправки письма.
#     В письме есть приветствие с именем пользователя и информация о покупке, такая как дата и общая сумма.
#     В письме также присутствует благодарственное сообщение.
#     Обе задачи используют адрес электронной почты friendship@mail.ru в качестве отправителя и адрес электронной почты
#     пользователя в качестве получателя.
#     """
#     send_mail(
#         'friendship',
#         f'Здравствуйте, {first_name}!\n\n'
#         f'Мы рады сообщить, что ваша покупка была успешно соверщена.\n\n'
#         f'Дата покупки: {datetime.datetime.now().strftime("%d.%m.%Y")} '
#         f'Сумма покупки: {total_price}\n\n'
#         f'Спасибо, что выбрали наш магазин!',
#         'friendship@mail.ru',
#         [email],
#         fail_silently=False,
#     )


@app.task
def send_spam_email(user_email):
    send_mail(user_email)


@app.task
def send_beat_mail():
    for contact in Contact.objects.all():
        send_mail(
            'SPAM',
            [contact.email],
            fail_silently=False,
        )
