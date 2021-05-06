from django.db import models

class Todo(models.Model):
    class Meta:
        verbose_name = "Yapılacak"
        verbose_name_plural = 'Yapılacaklar'

    todo = models.CharField(max_length=200, verbose_name='Yapılacak')
    isActive = models.BooleanField(default=False, verbose_name='Yapıldı Mı?')

    def __str__(self):
        return self.todo