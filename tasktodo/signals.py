from django.core.cache import cache

from django.db.models.signals import post_save, m2m_changed,post_delete

from django.dispatch import receiver

from .models import Task


@receiver(m2m_changed,sender=Task)
@receiver(post_delete,sender=Task)
@receiver(post_save,sender=Task,)
def cache_delete_list(sender,instance,**kwargs):

    cache.delete('all_task')