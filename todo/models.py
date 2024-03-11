from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    class Meta:
        db_table = "todo"
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
    
    def __str__(self) -> str:
        return self.title