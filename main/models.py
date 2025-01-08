from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    corbado_user_id = models.CharField(unique=True, max_length=255)
    city = models.CharField(max_length=255, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.corbado_user_id} - {self.city}"