from django.db import models


# Create your models here.


class Book(models.Model):
    book_id = models.AutoField(primary_key = True, unique=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=300,null=True)
    publisher = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.title

    # def createBook(title,author,category,img)




    
