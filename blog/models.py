from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(models.Model):
    id = models.AutoField('user_id', primary_key=True)
    name = models.CharField('user_name', max_length=150)
    surname = models.CharField('user_surname', max_length=150)
    nickname = models.CharField('user_nickname', max_length=150, blank=True, null=True)
    email = models.EmailField('user_email', unique=True)
    password = models.CharField('user_password')
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']
    
    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
    
    @property
    def is_authenticated(self):
        return True
    
    @classmethod
    def create_user(cls, name, surname, nickname, email, password):
        nickname = nickname if nickname else name.split()[0].lower() + surname
        user = cls(name=name, surname=surname, nickname=nickname,email=email)
        user.set_password(password)
        user.save()
        return user
    

class Post(models.Model):

    id = models.AutoField('post_id', primary_key=True)
    title= models.CharField('post_title', max_length=200)
    content = models.TextField('post_content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} created by {self.author.name} {self.author.surname}"
    
class Comment(models.Model):

    Star = [(1,'*'), (2,'**'), (3,'***'), (4,'****'), (5,'*****')]

    id = models.AutoField('comment_id', primary_key=True)
    star = models.IntegerField('comment_star', default=1, choices=Star)
    content = models.TextField('comment_content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Comment by {self.author.name} {self.author.surname} on post {self.post.title} with {self.star} stars"
    

