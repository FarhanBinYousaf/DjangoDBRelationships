from django.db import models

# Create your models here.


# One-to-one Relation

class User(models.Model):
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100,blank=True,unique=True)
    contact = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.name
    

# One to Many / Many to One relation

class Author(models.Model):
    name = models.CharField(max_length=100,blank=True)
    Age = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=100)
    publishDate = models.DateField()

    def __str__(self):
        return self.title
    

# Many to Many relation

class Tag(models.Model):
    name = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=50,blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    

