from django.contrib.auth.models import User
from django.core.mail import  send_mail

from celery import shared_task

from .models import Post
   

@shared_task()
def task_execute(job_params):

    user_list = User.objects.all()    
    from_email = 'email@example.com'
    subject = 'Последние статьи'
    
    for user in user_list:
        message = ''
        subscribes = Follow.objects.filter(user=user).values('author')
        posts = Post.objects.filter(author__pk__in=subscribes)[:5]
        recipient_list = [email, ]
        for post in posts:
            message += (
                f'''\n{post.title}\
                    \n{post.text}\
                    \n{post.author.username}\
                    \n{post.pub_date}\
                    \n{post.blog.title}\
                '''
            )
        send_mail(subject, message, from_email, recipient_list)
