from django.db import models


class AccountPhoto(models.Model):
    user_id = models.UUIDField(primary_key=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.user_id