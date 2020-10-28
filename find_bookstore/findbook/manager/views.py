from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from .models import *
from sign.models import User
from django.utils import timezone
from customer.models import *
from django.core.paginator import Paginator

# Create your views here.

def register_store(request):
    return render(request, 'register_store.html')

def new_bookstore(request):
    user=request.user
    new_bookstore = Bookstore()
    new_bookstore.name = request.POST['store_name']
    new_bookstore.addr = request.POST['store_addr1']+','+request.POST['store_addr2']
    new_bookstore.tell_no = request.POST['store_tel']
    new_bookstore.description = request.POST['store_description']
    new_bookstore.save()
    user.bookstore_id = new_bookstore.bookstore_id
    user.save()
    #나중에 for문으로 바꿔주셈
    tag1 = Tag.objects.get(tag_name=request.POST['tag1'])
    tag2 = Tag.objects.get(tag_name=request.POST['tag2'])
    tag3 = Tag.objects.get(tag_name=request.POST['tag3'])
    new_bookstore_tag1 = BookstoreTag()
    new_bookstore_tag2 = BookstoreTag()
    new_bookstore_tag3 = BookstoreTag()
    new_bookstore_tag1.bookstore_id=new_bookstore
    new_bookstore_tag2.bookstore_id=new_bookstore
    new_bookstore_tag3.bookstore_id=new_bookstore
    new_bookstore_tag1.tag_id=tag1
    new_bookstore_tag2.tag_id=tag2
    new_bookstore_tag3.tag_id=tag3
    new_bookstore_tag1.save()
    new_bookstore_tag2.save()
    new_bookstore_tag3.save()
    # #나중에 for문으로 바꿔주셈
    return redirect('manager_main') #render(request,'manager_main.html')#,{'user_bs_id':user.bookstore_id})

def booksearch(request):
    return render(request, 'booksearch.html')


#hashtag 추가 완료
def manager_main(request):
    user = request.user
    bookstore_id = user.bookstore_id
    bookstore = get_object_or_404(Bookstore,pk=bookstore_id)
    notices = Notice.objects.filter(bookstore_id=user.bookstore_id).all()
    bookstore_tag_ids = BookstoreTag.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    bookstore_bestsellers = Bestseller.objects.filter(bookstore_id=bookstore.bookstore_id).all()
    paginator = Paginator(notices,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    
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

    return render(request, 'manager_main.html', {'bookstore':bookstore,'tags':tags, 'bestsellers':bestsellers, 'notices':notices, 'posts':posts})

def store_edit(request):
    user = request.user
    bookstore_id = user.bookstore_id
    edit_bookstore = get_object_or_404(Bookstore,pk=bookstore_id)
    bookstore_tag_ids = BookstoreTag.objects.filter(bookstore_id=edit_bookstore.bookstore_id).all()
    bookstore_bestsellers = Bestseller.objects.filter(bookstore_id=edit_bookstore.bookstore_id).all()
    bestseller_ids = []
    for b in bookstore_bestsellers:
        bestseller_ids.append(b.book_id)
    bestsellers = []
    for b in bestseller_ids :
        bestsellers.append(b)
    
    tag_ids= []
    for i in bookstore_tag_ids :
        tag_ids.append(i.tag_id)
    tags= []
    for j in tag_ids:
        tags.append(j.tag_name)
    return render(request,'store_edit.html',{'bookstore':edit_bookstore,'bestsellers':bestsellers,'tags':tags})

def store_update(request):
    user = request.user
    bookstore_id = user.bookstore_id
    update_bookstore = get_object_or_404(Bookstore,pk=bookstore_id)
    update_bookstore.name = request.POST['edit_storename']
    update_bookstore.addr = request.POST['edit_addr']
    update_bookstore.tell_no = request.POST['edit_tell_no']
    update_bookstore.description = request.POST['edit_description']
    update_bookstore.image = request.FILES['store_image']
    update_bookstore.save()
    return redirect('manager_main')


def manager_notice_detail(request,notice_id):
    notice = Notice.objects.get(notice_id=notice_id)
    print(notice)
    return render(request,'manager_notice_detail.html',{'notice':notice})

def manager_notice_new(request):
    #user = request.user
    #bookstore_id = user.bookstore_id
    return render(request, 'manager_notice_new.html')

def manager_notice_create(request):
    user = request.user
    bookstore_id = user.bookstore_id
    new_notice = Notice()
    new_notice.bookstore_id =  bookstore_id
    new_notice.title = request.POST['manager_notice_title']
    new_notice.pub_date = timezone.datetime.now()
    new_notice.body = request.POST['manager_notice_body']
    new_notice.save()
    return redirect('manager_main')

def manager_notice_edit(request,notice_id):
    edit_notice = Notice.objects.get(notice_id=notice_id)
    return render(request,'manager_notice_edit.html',{'notice':edit_notice})

def manager_notice_update(request,notice_id):
    update_notice = get_object_or_404(Notice,pk=notice_id)
    update_notice.title = request.POST['manager_notice_title']
    update_notice.pub_date = timezone.datetime.now()
    update_notice.body = request.POST['manager_notice_body']
    update_notice.save()
    return redirect('manager_notice_detail',update_notice.notice_id)

def manager_notice_delete(request,notice_id):
    user = request.user
    delete_notice = Notice.objects.get(notice_id=notice_id)
    print(delete_notice)
    delete_notice.delete()
    return redirect('manager_main')

def addbook(request):
    user = request.user
    book = Book()
    book.author = request.GET['author']
    book.title = request.GET['title']
    book.img = request.GET.get('img', False)
    book.publisher = request.GET['publisher']
    book.save()
    bookstore = get_object_or_404(Bookstore, pk=user.bookstore_id)
    bestseller = Bestseller()
    bestseller.bookstore_id = bookstore
    bestseller.book_id = book
    bestseller.save()
    return redirect('booksearch')

def deletebook(request,book_id):
    user = request.user
    bookstore_id = user.bookstore_id
    bestseller = Bestseller.objects.filter(bookstore_id=bookstore_id,book_id=book_id)
    bestseller.delete()
    return redirect('store_edit')
