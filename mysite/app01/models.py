from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
