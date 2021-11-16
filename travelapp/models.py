from django.db import models

# Create your models here.
class place(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class blogs(models.Model):
    def __str__(self):
        return self.title

    blog_date=models.IntegerField()
    blog_month=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.TextField()
    blog_image=models.ImageField(upload_to='pic')


