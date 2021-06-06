from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        

class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    film = models.ForeignKey('Film', on_delete=models.CASCADE)
    comment = models.TextField(max_length=140)
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
