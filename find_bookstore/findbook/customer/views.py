from django.shortcuts import render
from .models import Book
import operator
from manager.models import *
from django.core.paginator import Paginator


# Create your views here.
def main(request):
    bookstore = Bookstore.objects.get(bookstore_id=1)
    return render (request, 'customer/customer_main.html', {'bookstore':bookstore})
    
def notice(request,bookstore_id):
    bookstore = Bookstore.objects.get(bookstore_id=bookstore_id)
    notices = Notice.objects.filter(bookstore_id=bookstore_id).all()
    bestsellers = Bestseller.objects.filter(bookstore_id=bookstore_id).all()
    paginator = Paginator(notices,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    bookstore_tag_ids = BookstoreTag.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    bookstore_bestsellers = Bestseller.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    tag_ids= []
    for i in bookstore_tag_ids :
        tag_ids.append(i.tag_id)
    tags= []
    for j in tag_ids:
        tags.append(j.tag_name)
    bestseller_ids = []
    for b in bookstore_bestsellers:
        bestseller_ids.append(b.book_id)        
    bestsellers = []
    for b in bestseller_ids :
        bestsellers.append(b)
  

    print(notices, bookstore, bestsellers)
    return render (request, 'customer/detailnotice_minsu.html', {'notices':notices, 'bookstore':bookstore,'tags':tags,'bestsellers':bestsellers, 'posts':posts})


def review(request,bookstore_id):
    bookstore = Bookstore.objects.get(bookstore_id=bookstore_id)
    bestsellers = Bestseller.objects.filter(bookstore_id=bookstore_id).all()
    reviews = Review.objects.filter(bookstore_id=bookstore_id).all()
    

    bookstore_tag_ids = BookstoreTag.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    bookstore_bestsellers = Bestseller.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    tag_ids= []
    for i in bookstore_tag_ids :
        tag_ids.append(i.tag_id)
    tags= []
    for j in tag_ids:
        tags.append(j.tag_name)
    bestseller_ids = []
    for b in bookstore_bestsellers:
        bestseller_ids.append(b.book_id)        
    bestsellers = []
    for b in bestseller_ids :
        bestsellers.append(b)
  

    print(bookstore, bestsellers,reviews)

    return render (request, 'customer/detailreview.html', {'bookstore':bookstore, 'bestsellers':bestsellers,'tags':tags, 'reviews':reviews})



def review_add(request,bookstore_id):
    bookstore = Bookstore.objects.get(bookstore_id=bookstore_id)
    bestsellers = Bestseller.objects.filter(bookstore_id=bookstore_id).all()
    reviews = Review.objects.filter(bookstore_id=bookstore_id).all()
    

    bookstore_tag_ids = BookstoreTag.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    bookstore_bestsellers = Bestseller.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    tag_ids= []
    for i in bookstore_tag_ids :
        tag_ids.append(i.tag_id)
    tags= []
    for j in tag_ids:
        tags.append(j.tag_name)
    bestseller_ids = []
    for b in bookstore_bestsellers:
        bestseller_ids.append(b.book_id)        
    bestsellers = []
    for b in bestseller_ids :
        bestsellers.append(b)
        
    user = request.user
    new_review = Review()
    new_review.bookstore_id = bookstore_id
    new_review.writer = user
    new_review.text = request.POST['review_text']
    new_review.save()
    
    
        
    return render (request, 'customer/detailreview.html' ,{'bookstore':bookstore, 'bestsellers':bestsellers, 'tags':tags,'reviews':reviews})


def review_del(request,bookstore_id):
    bookstore = Bookstore.objects.get(bookstore_id=bookstore_id)
    bookstore_bestsellers = Bestseller.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    reviews = Review.objects.filter(bookstore_id=bookstore_id).all()
    user = request.user
    bestseller_ids = []
    for b in bookstore_bestsellers:
        bestseller_ids.append(b.book_id)        
    bestsellers = []
    for b in bestseller_ids :
        bestsellers.append(b)
    
    reviews.delete()

    return render (request, 'customer/detailreview.html' ,{'bookstore':bookstore, 'bestsellers':bestsellers, 'reviews':reviews})

