from django.db import models
from django.forms import PasswordInput
from django.contrib.auth.hashers import make_password

# Create your models here.
class Client(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
     
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self.password:
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

class Comment(models.Model):
    text=models.TextField(max_length=500)
    comment_date=models.TimeField(auto_now_add=True)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)


class Post(models.Model):
    image= models.ImageField(upload_to="static/images")
    title=models.CharField(max_length=50)
    body=models.TextField(max_length=1000)
    post_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    comment_text=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,blank=True)
       
def __str__(self):
        return str(self.id)
 
