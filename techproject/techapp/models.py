from django.db import models
from django.forms import PasswordInput
from django.contrib.auth.hashers import make_password
from autoslug import AutoSlugField


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
    password=models.CharField(max_length=50,null=True)
    is_staff=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name


class Post(models.Model):
    image= models.ImageField(upload_to="static/images")
    title=models.CharField(max_length=50)
    body=models.TextField(max_length=1000)
    post_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    # comment_text=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,blank=True)
    slug=AutoSlugField(populate_from="title",null=True) 

    def __str__(self):
        return str(self.id)
    
class Comment(models.Model):
    text=models.TextField(max_length=500)
    comment_date=models.TimeField(auto_now_add=True)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment_text")

    def __str__(self):
        return str(self.id)