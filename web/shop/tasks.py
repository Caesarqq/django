from django.core.mail import send_mail
from web .celery import app

from .service import send
from .models import Contact

@app.task
def send_spam_email(user_email):
	print('hello')
	send(user_email)

@app.task
def send_beat_mail():
	for contact in Contact.objects.all():
		send_mail(
			'SPAM',
			[contact.email],
			fail_silently=False,
		)