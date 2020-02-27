from django.db import models


class Messages(models.Model):


    email=models.EmailField()
    body=models.TextField(max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
