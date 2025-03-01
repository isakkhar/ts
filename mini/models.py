from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the category name')
    def __str__(self):
        return self.Name

class Author(models.Model):
    Author_Name = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the author name')
    Email = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the author email')
    Image = models.ImageField(upload_to='images/', null=True, blank=True, help_text='Enter the author image')
    def __str__(self):
        return self.Author_Name

class Post(models.Model):
    Title = models.CharField(max_length=100, null=True, blank=True, help_text='Enter a blog title')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Author_Name = models.ForeignKey(Author, on_delete=models.CASCADE)
    Content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title
    class Meta:
        ordering = ['-created']
