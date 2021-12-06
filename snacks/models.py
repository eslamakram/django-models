from django.db import models
from django.contrib.auth import get_user_model

# add name as a CharField with maximum length of 64 characters.
# add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
# from django.contrib.auth import get_user_model
# add description TextField
# Create your models here.
class Snack(models.Model):
        name = models.CharField(max_length=64)
        purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
        description = models.TextField(default=0)


        def __str__(self):
         return self.name