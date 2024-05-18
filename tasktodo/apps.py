from django.apps import AppConfig



class TasktodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasktodo'

    def ready(self) -> None:
        
        import tasktodo.signals
