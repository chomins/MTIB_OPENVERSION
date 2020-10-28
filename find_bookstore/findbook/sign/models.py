from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager, PermissionsMixin
from django.db import models
from manager.models import *


class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def manage_user(self, email, username, usertype, tell_no, addr ,auth, password=None):        
        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            username = username,     
            usertype = usertype,
            tell_no = tell_no,
            addr = addr,
            auth = auth
        )        
        user.set_password(password)
        user.save(using=self._db)        
        return user     

    def create_user(self, email, username, usertype, auth, tell_no, addr, password=None):        
        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            username = username,     
            usertype = usertype,
            auth=auth,
            tell_no= tell_no,
            addr= addr  
        )        
        user.set_password(password)
                
        user.save(using=self._db)        
        return user     

    def create_superuser(self, email, username,password ):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            username = username,
            usertype = 'A',            
            password = password,
            auth = '',
            tell_no='',
            addr='',                
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user      

class Tag(models.Model):
    tag_id = models.AutoField(primary_key = True, unique=True)
    tag_name = models.CharField(max_length=20,null=False, unique=False)
    class Meta:
        db_table = 'tag'
        
class User(AbstractBaseUser,PermissionsMixin):    
    
    objects = UserManager()
    
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )

    auth = models.CharField(max_length=8,null=True,unique=False) # 유저인증
    bookstore_id = models.CharField(max_length=100, null=True)
    tell_no = models.CharField(max_length=20,null=True,unique=False)
    addr = models.CharField(max_length=100,null=True,unique=False)
    usertype = models.CharField(max_length=3,null=True,unique=False)#고객이면 C 서점주인이면 M 관리자면 S
    tag_id = models.ManyToManyField(Tag, through = 'UserTag')      
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True) #REG_DATE    
    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'user'



class UserTag(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'user_tag'


