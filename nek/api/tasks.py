from django.contrib.auth.models import User
from django.core.mail import send_mail

from celery import shared_task

from blog.models import Post

from users.models import Follow
   

@shared_task
def task_execute():

    user_list = User.objects.all()[:10] 

    for user in user_list:
        subject = 'Last News!!!'
        from_email = 'email@example.com'
        email = user.email
        message = ''
        subscribes = Follow.objects.filter(user=user).values('author')
        posts = Post.objects.filter(author__pk__in=subscribes)[:5]
        recipient_list = [email, ]
        print(posts)
        if posts:
            for post in posts:
                message += (
                    f'''\n{post.title}\
                        \n{post.text}\
                        \n{post.author.username}\
                        \n{post.pub_date}\n
                    '''
                )
            send_mail(subject, message, from_email, recipient_list)
        else:
            continue
        
    return "Done"
