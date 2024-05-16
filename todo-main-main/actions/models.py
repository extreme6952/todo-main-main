from django.db import models

from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.auth.models import User


class Actions(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='actions')
    
    verb = models.CharField(max_length=266)

    created = models.DateTimeField(auto_now_add=True)

    target_ct = models.ForeignKey(ContentType,
                                  on_delete=models.CASCADE,
                                  related_name='target_obj')
    
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True)
    
    target = GenericForeignKey('target_ct','target_id')

    class Meta:

        ordering = ['-created']

        indexes = [
            models.Index(fields=['-created'])
        ]

class Comment(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     related_query_name='comments')
    
    object_id = models.PositiveIntegerField(blank=True,
                                            null=True)
    
    content_object = GenericForeignKey('content_type','object_id')

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
        return f" Comment {self.user.username} by {self.content_object}"
    
