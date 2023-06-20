from django.core.mail import send_mail


def send(user_email):
	# print('я работаю', send_mail)
    send_mail(
		'СПАМ',
		'djangoweb2@gmail.com'
		[user_email],
		fail_silently=False,
	)
