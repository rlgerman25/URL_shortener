from django.db import models
# Models.py -> make place in DB to store data

class kirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique= True)
    timestamp = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.url)
