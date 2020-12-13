from django.db import models
from login.models import userLogin
# Create your models here.

class filetb(models.Model):
    filename = models.CharField(max_length=128, primary_key=True)
    username = models.ForeignKey(userLogin,on_delete=models.CASCADE)
    filedate = models.DateTimeField(auto_now_add=True)
    filepath = models.CharField(max_length=128)

    class Meta:  # 关于 Meta： https://docs.djangoproject.com/zh-hans/3.1/topics/db/models/#meta-options
        db_table = "filetb"

    def __str__(self):
        return self.filename