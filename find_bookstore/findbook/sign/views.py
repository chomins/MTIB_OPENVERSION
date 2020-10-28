from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout, update_session_auth_hash
from django.http import HttpResponse
from .models import User
import json
from django.core.serializers.json import DjangoJSONEncoder
from .helper import email_auth_num,send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from manager.views import *
from django.db.models import Count
import operator
# Create your views here.



# 메인화면
def before_sign(request):
    return render(request, 'before_sign.html')

def sign_up_check(request):
    return render(request, 'sign_up_check.html')

def before_psy(request):
    return render(request, 'before_psy.html')


# 심리테스트 페이지
def sign_psy(request):
    return render(request, 'sign_psy.html')

def sign_psy2(request):
    return render(request, 'sign_psy2.html')

def sign_psy2_1(request):
    return render(request, 'sign_psy2_1.html')

def sign_psy2_2(request):
    return render(request, 'sign_psy2_2.html')

def sign_psy2_3(request):
    return render(request, 'sign_psy2_3.html')

def sign_psy3(request):
    return render(request, 'sign_psy3.html')

def sign_psy3_1(request):
    return render(request, 'sign_psy3_1.html')

def sign_psy3_2(request):
    return render(request, 'sign_psy3_2.html')

def sign_psy3_3(request):
    return render(request, 'sign_psy3_3.html')


# 심리테스트페이지 끝


# ID/PW 찾기
def before_search(request):
    return render(request, 'before_search.html')

def recovery_id(request):
    
    return render(request, 'recovery_id.html')

def recovery_pw(request):
    
    return render(request, 'recovery_pw.html')
     

def ajax_find_id_view(request):
    email = request.POST.get('email')
    result_id = User.objects.get(email=email)      
    return HttpResponse(json.dumps({"result_id": result_id.username}, cls=DjangoJSONEncoder), content_type = "application/json")

def ajax_find_pw_view(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    target_user = User.objects.get(username=username, email=email)
    print(target_user)
    if target_user:
        auth_num = email_auth_num()
        target_user.auth = auth_num 
        target_user.save()
        send_mail(
            '비밀번호 찾기 인증메일입니다.',
            [email],
            html=render_to_string('recovery_email.html', {
                'auth_num': auth_num,
            }),
        )
    return HttpResponse(json.dumps({"result": target_user.username}, cls=DjangoJSONEncoder), content_type = "application/json")

def auth_confirm_view(request):
    username = request.POST.get('username')
    input_auth_num = request.POST.get('input_auth_num')
    target_user = User.objects.get(username=username, auth=input_auth_num)
    print(target_user)
    target_user.auth = ""
    target_user.save()
    request.session['auth'] = target_user.username 
    return HttpResponse(json.dumps({"result": target_user.username}, cls=DjangoJSONEncoder), content_type = "application/json")

def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = User.objects.get(username=session_user)
        auth_login(request, current_user)
        if request.POST['password1'] == request.POST['password2']:
            password1=request.POST['password1'] 
            current_user.set_password(password1)
            current_user.save()
            messages.success(request, "비밀번호 변경완료! 변경된 비밀번호로 로그인하세요.")
            auth_logout(request)
            return redirect('before_sign')
        else:
            auth_logout(request)
            request.session['auth'] = session_user
    else:
        return render(request, 'reset_pw.html')
    return render(request, 'reset_pw.html')

   
# 손님 회원 가입
def c_register(request):
    
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password1'] == request.POST['password2']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'], 
            usertype=request.POST['usertype'],auth='',tell_no=request.POST['tell_no'],addr=request.POST['addr1']+','+request.POST['addr2'])
            # 로그인 한다
            user.usertype='C'
            auth_login(request, user)
            tags = Tag.objects.all()
            if (len(tags)==0):
                print(tags)
                tag1 = Tag()
                tag1.tag_name='잔잔한'
                tag2 = Tag()
                tag2.tag_name='수수한'
                tag3 = Tag()
                tag3.tag_name='부드러운'
                tag4 = Tag()
                tag4.tag_name='재미있는'
                tag5 = Tag()
                tag5.tag_name='신나는'
                tag6 = Tag()
                tag6.tag_name='활발한'
                tag7 = Tag()
                tag7.tag_name='시적인'
                tag8 = Tag()
                tag8.tag_name='침착한'
                tag9 = Tag()
                tag9.tag_name='깔끔한'
                tag10 = Tag()
                tag10.tag_name='쾌적한'
                tag11 = Tag()
                tag11.tag_name='넓직한'
                tag12 = Tag()
                tag12.tag_name='평화로운'
                tag1.save()
                tag2.save()
                tag3.save()
                tag4.save()
                tag5.save()
                tag6.save()
                tag7.save()
                tag8.save()
                tag9.save()
                tag10.save()
                tag11.save()
                tag12.save()
            else:
                print(tags)
            return redirect('before_psy')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'sign_c_register.html')

# 사장님 회원 가입
def m_register(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password1'] == request.POST['password2']:
            # user 객체를 새로 생성
            user = User.objects.manage_user(username=request.POST['username'],email=request.POST['email'], password=request.POST['password1'], usertype=request.POST['usertype'],
            tell_no=request.POST['tell_no'], addr=request.POST['addr1']+','+request.POST['addr2'], auth='')
            # 로그인 한다
            user.usertype='M'
            auth_login(request, user)
            tags = Tag.objects.all()
            if (len(tags)==0):
                print('태그 빔')
                tag1 = Tag()
                tag1.tag_name='잔잔한'
                tag2 = Tag()
                tag2.tag_name='수수한'
                tag3 = Tag()
                tag3.tag_name='부드러운'
                tag4 = Tag()
                tag4.tag_name='재미있는'
                tag5 = Tag()
                tag5.tag_name='신나는'
                tag6 = Tag()
                tag6.tag_name='활발한'
                tag7 = Tag()
                tag7.tag_name='시적인'
                tag8 = Tag()
                tag8.tag_name='침착한'
                tag9 = Tag()
                tag9.tag_name='깔끔한'
                tag10 = Tag()
                tag10.tag_name='쾌적한'
                tag11 = Tag()
                tag11.tag_name='넓직한'
                tag12 = Tag()
                tag12.tag_name='평화로운'
                tag1.save()
                tag2.save()
                tag3.save()
                tag4.save()
                tag5.save()
                tag6.save()
                tag7.save()
                tag8.save()
                tag9.save()
                tag10.save()
                tag11.save()
                tag12.save()
            else:
                print(tags)
            return redirect('register_store')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'sign_m_register.html')

# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    user= request.user
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = authenticate(username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            if user.usertype=='C':
                # 로그인 한다
                auth_login(request, user)
                tags = Tag.objects.all()
                if (len(tags)==0):
                    print('태그 빔')
                    tag1 = Tag()
                    tag1.tag_name='잔잔한'
                    tag2 = Tag()
                    tag2.tag_name='수수한'
                    tag3 = Tag()
                    tag3.tag_name='부드러운'
                    tag4 = Tag()
                    tag4.tag_name='재미있는'
                    tag5 = Tag()
                    tag5.tag_name='신나는'
                    tag6 = Tag()
                    tag6.tag_name='활발한'
                    tag7 = Tag()
                    tag7.tag_name='시적인'
                    tag8 = Tag()
                    tag8.tag_name='침착한'
                    tag9 = Tag()
                    tag9.tag_name='깔끔한'
                    tag10 = Tag()
                    tag10.tag_name='쾌적한'
                    tag11 = Tag()
                    tag11.tag_name='넓직한'
                    tag12 = Tag()
                    tag12.tag_name='평화로운'
                    tag1.save()
                    tag2.save()
                    tag3.save()
                    tag4.save()
                    tag5.save()
                    tag6.save()
                    tag7.save()
                    tag8.save()
                    tag9.save()
                    tag10.save()
                    tag11.save()
                    tag12.save()
                else:
                    print(tags)
                return redirect('home')
            elif user.usertype=='M':
                # 로그인 한다
                auth_login(request, user)
                tags = Tag.objects.all()
                if (len(tags)==0):
                    print('태그 빔')
                    tag1 = Tag()
                    tag1.tag_name='잔잔한'
                    tag2 = Tag()
                    tag2.tag_name='수수한'
                    tag3 = Tag()
                    tag3.tag_name='부드러운'
                    tag4 = Tag()
                    tag4.tag_name='재미있는'
                    tag5 = Tag()
                    tag5.tag_name='신나는'
                    tag6 = Tag()
                    tag6.tag_name='활발한'
                    tag7 = Tag()
                    tag7.tag_name='시적인'
                    tag8 = Tag()
                    tag8.tag_name='침착한'
                    tag9 = Tag()
                    tag9.tag_name='깔끔한'
                    tag10 = Tag()
                    tag10.tag_name='쾌적한'
                    tag11 = Tag()
                    tag11.tag_name='넓직한'
                    tag12 = Tag()
                    tag12.tag_name='평화로운'
                    tag1.save()
                    tag2.save()
                    tag3.save()
                    tag4.save()
                    tag5.save()
                    tag6.save()
                    tag7.save()
                    tag8.save()
                    tag9.save()
                    tag10.save()
                    tag11.save()
                    tag12.save()
                else:
                    print(len(tags))
                return redirect('manager_main')
                # return HttpResponse(user)
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'before_sign.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'before_sign.html')

# 로그 아웃
def logout(request):
    auth_logout(request)
    return render(request, 'before_sign.html')

# 태그
def tag_comfort(request):
    user= request.user
    taglist=UserTag.objects.all()
    if (len(taglist)==0): # user tag 없는 경우
        usertag1=UserTag()
        usertag2=UserTag()
        usertag3=UserTag()
        usertag1.username = user
        usertag1.tag_id = Tag.objects.get(tag_name="잔잔한")
        usertag2.username = user
        usertag2.tag_id = Tag.objects.get(tag_name="수수한")
        usertag3.username = user
        usertag3.tag_id = Tag.objects.get(tag_name="부드러운")
        usertag1.save()
        usertag2.save()
        usertag3.save()
        # print(taglist)
        return render(request, 'tag_comfort.html')
    else: # user tag 있는 경우
        for tag in taglist:
            tag.delete()
        usertag1=UserTag()
        usertag2=UserTag()
        usertag3=UserTag()
        usertag1.username = user
        usertag1.tag_id = Tag.objects.get(tag_name="잔잔한")
        usertag2.username = user
        usertag2.tag_id = Tag.objects.get(tag_name="수수한")
        usertag3.username = user
        usertag3.tag_id = Tag.objects.get(tag_name="부드러운")
        usertag1.save()
        usertag2.save()
        usertag3.save()
        # print(taglist)
        return render(request, 'tag_comfort.html')
    

def tag_simple(request):
    user=request.user
    taglist=UserTag.objects.all()
    if (len(taglist)==0): # user tag 없는 경우
        usertag1=UserTag()
        usertag2=UserTag()
        usertag3=UserTag()
        usertag1.username = user
        usertag1.tag_id = Tag.objects.get(tag_name="시적인")
        usertag2.username = user
        usertag2.tag_id = Tag.objects.get(tag_name="침착한")
        usertag3.username = user
        usertag3.tag_id = Tag.objects.get(tag_name="깔끔한")
        usertag1.save()
        usertag2.save()
        usertag3.save()
        return render(request, 'tag_simple.html')
    else: # user tag 있는 경우
        for tag in taglist:
            tag.delete()
        usertag1=UserTag()
        usertag2=UserTag()
        usertag3=UserTag()
        usertag1.username = user
        usertag1.tag_id = Tag.objects.get(tag_name="시적인")
        usertag2.username = user
        usertag2.tag_id = Tag.objects.get(tag_name="침착한")
        usertag3.username = user
        usertag3.tag_id = Tag.objects.get(tag_name="깔끔한")
        usertag1.save()
        usertag2.save()
        usertag3.save()
        return render(request, 'tag_simple.html')


def tag_cool(request):
    user=request.user
    taglist=UserTag.objects.all()
    if (len(taglist)==0): # user tag 없는 경우
        usertag1=UserTag()
        usertag2=UserTag()
        usertag3=UserTag()
        usertag1.username = user
        usertag1.tag_id = Tag.objects.get(tag_name="쾌적한")
        usertag2.username = user
        usertag2.tag_id = Tag.objects.get(tag_name="넓직한")
        usertag3.username = user
        usertag3.tag_id = Tag.objects.get(tag_name="평화로운")
        usertag1.save()
        usertag2.save()
        usertag3.save()
        return render(request, 'tag_cool.html')
    else: # user tag 있는 경우
        for tag in taglist:
            tag.delete()
        usertag1=UserTag()
        usertag2=UserTag()
        usertag3=UserTag()
        usertag1.username = user
        usertag1.tag_id = Tag.objects.get(tag_name="쾌적한")
        usertag2.username = user
        usertag2.tag_id = Tag.objects.get(tag_name="넓직한")
        usertag3.username = user
        usertag3.tag_id = Tag.objects.get(tag_name="평화로운")
        usertag1.save()
        usertag2.save()
        usertag3.save()
        return render(request, 'tag_cool.html')


def tag_enjoy(request):
    user=request.user
    taglist=UserTag.objects.all()
    if (len(taglist)==0): # user tag 없는 경우
        usertag1=UserTag()
        usertag2=UserTag()
        usertag3=UserTag()
        usertag1.username = user
        usertag1.tag_id = Tag.objects.get(tag_name="재미있는")
        usertag2.username = user
        usertag2.tag_id = Tag.objects.get(tag_name="신나는")
        usertag3.username = user
        usertag3.tag_id = Tag.objects.get(tag_name="활발한")
        usertag1.save()
        usertag2.save()
        usertag3.save()
        return render(request, 'tag_enjoy.html')
    else: # user tag 있는 경우
        for tag in taglist:
            tag.delete()    
        usertag1=UserTag()
        usertag2=UserTag()
        usertag3=UserTag()
        usertag1.username = user
        usertag1.tag_id = Tag.objects.get(tag_name="재미있는")
        usertag2.username = user
        usertag2.tag_id = Tag.objects.get(tag_name="신나는")
        usertag3.username = user
        usertag3.tag_id = Tag.objects.get(tag_name="활발한")
        usertag1.save()
        usertag2.save()
        usertag3.save()
        return render(request, 'tag_enjoy.html')

def recommend_store(request):
    user = request.user
    usertag = UserTag.objects.filter(username=user).all()
    usertaglist = []
    bookstores = BookstoreTag.objects.all()
    
    count=0
    for tag in usertag:
        usertaglist.append(tag)
    bst = []
    bsts = []
    n=3
    bsts = [bookstores[i * n:(i + 1) * n] for i in range((len(bookstores) + n - 1) // n )]
        
    matchings= {}
    
    for i in bsts:
        print(i)
        count=0
        for k in i:
            print(k)
            
            for j in usertaglist:
                print(k.tag_id,j.tag_id)
                if k.tag_id == j.tag_id:
                    count+=1
                
        matchings[i[0].bookstore_id] = count
    matchings = sorted(matchings.items(), key=operator.itemgetter(1),reverse=True)
    print(matchings)
    recommend_stores = []
    for i in matchings:
        recommend_stores.append(i[0])
    li=[]
    li.append(recommend_stores[0])
    li.append(recommend_stores[1])
    li.append(recommend_stores[2])
    li.append(recommend_stores[3])
    return render(request, 'recommend_store.html' ,{'usertaglist':usertaglist, 'recommend_stores':li})