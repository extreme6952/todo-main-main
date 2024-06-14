from django.db import models

from django.utils import timezone

from django.utils.text import slugify


from unidecode import unidecode

from django.urls import reverse

from django.contrib.auth.models import User

from actions.models import Comment

from easy_thumbnails.fields import ThumbnailerImageField

from django.contrib.auth import get_user_model

from django.contrib.contenttypes.fields import GenericRelation




class Task(models.Model):

    class StatusTask(models.TextChoices):

        ACEPTED = 'Acepted','aceptd'

        IN_PROGRESS = 'In progress','in progress'

        COMPLETED = 'Completed','completed'

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250,
                            blank=True)

    text = models.TextField(blank=True)

    image = ThumbnailerImageField(upload_to='task_image/%Y/%m/%d', 
                                  resize_source=dict(quality=95, 
                                                     size=(820,520), 
                                                     sharpen=True),
                                                     blank=True,
                                                     null=True)

    is_complete = models.BooleanField(default=False)

    status = models.CharField(max_length=50,
                              choices=StatusTask.choices,
                              default=StatusTask.ACEPTED)

    created = models.DateTimeField(auto_now_add=True,null=True)

    updated = models.DateTimeField(auto_now=True,null=True)

    users_like = models.ManyToManyField(User,
                                        related_name='user_like',
                                        blank=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)


    class Meta:

        ordering = ['-created']

        indexes = [
            models.Index(fields=['-created'])
        ]

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(unidecode(self.title))


        super().save(*args, **kwargs )


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("task_detail", args=[self.id,
                                            self.slug])
    



    

class Profile(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    
  
    photo = ThumbnailerImageField(upload_to='profile/%Y/%m/%d', 
                                  resize_source=dict(quality=95, 
                                                     size=(320,320), 
                                  sharpen=True))

    created = models.DateTimeField(auto_now_add=True,
                                   null=True)

  
    def __str__(self):

        return f"Profile the {self.user.username}"
    



class Comment(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    
    task = models.ForeignKey(Task,
                             on_delete=models.CASCADE,
                             related_name='comments')
    
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    class Meta:

        ordering = ['-created']

        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):

        return f"Comment user {self.user.username} by {self.task}"    
    


class ProfileTechnik(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    
    image_t = models.ImageField(upload_to='Technik/%Y/%m/%d')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"Profile technic {self.user.username}"

        