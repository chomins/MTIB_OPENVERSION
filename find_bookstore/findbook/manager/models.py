from django.db import models
from sign.models import *
from customer.models import *

# Create your models here.


class Bookstore(models.Model):
    bookstore_id = models.AutoField(primary_key = True, unique=True)
    addr = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    reg_date = models.DateTimeField(auto_now_add=True)
    tell_no = models.CharField(max_length=200)
    best_seller = models.ManyToManyField(Book, through = 'Bestseller') 
    tag_id = models.ManyToManyField(Tag, through = 'BookstoreTag')
    image = models.ImageField(upload_to = 'bookstore/',null = True, blank = True)

class Notice(models.Model):
    bookstore_id= models.CharField(max_length=1000)
    notice_id = models.AutoField(primary_key = True,unique=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
    def __str__(self):
        return self.title
    

    def summary(self):
        return self.body[:50]

class BookstoreTag(models.Model):
    bookstore_id= models.ForeignKey(Bookstore, on_delete = models.CASCADE, null=True)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'book_tag'

class Bestseller(models.Model):
    bookstore_id= models.ForeignKey(Bookstore, on_delete = models.CASCADE, null=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)



class Review(models.Model):
    bookstore_id= models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    text = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True, null=True)



    # def __str__(self):
    #     return self.writer.username + " " + self.reg_date.strftime("%Y-%m-%d %H:%M:%S")