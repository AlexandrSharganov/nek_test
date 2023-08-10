from django.contrib.auth.models import User
from django.core.mail import send_mail

from celery import shared_task


def send_news_mail(email):
    subject = 'Последние статьи'
    message = 
    from_email = DEFAULT_FROM_EMAIL
    recipient_list = [email, ]
    return send_mail(subject, message, from_email, recipient_list)


@shared_task()
def task_execute(job_params):

    user = User.objects.get(pk=job_params["db_id"])

    user.sum = assignment.first_term + assignment.second_term

    user.save()