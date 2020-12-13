from django.db import models

# Create your models here.

class userLogin(models.Model):
    username = models.CharField(max_length=128,primary_key=True)
    password = models.CharField(max_length=128)

    class Meta:  # 关于 Meta： https://docs.djangoproject.com/zh-hans/3.1/topics/db/models/#meta-options
        db_table = "userlogin"

    def __str__(self):
        return self.username
