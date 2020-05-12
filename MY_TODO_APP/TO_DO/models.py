from django.db import models


class Todo(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
