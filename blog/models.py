from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone as tz


class PostManager(models.Manager):

    def get_reciepts_year(self, year=tz.now().year):
        return self.filter(modified_date__year=year).all()

    def get_reciepts_month(self, year=tz.now().year, month=tz.now().month):
        return self.filter(modified_date__year=year).filter(modified_date__month=month).all()

    def get_reciept_by_id(self, id):
        return self.filter(pk=id)


    def get_last_reciepts(self, quant=12):
        return self.filter(modified_date__lte=tz.now()).order_by('-modified_date')[:quant]






class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    created_date = models.DateTimeField(default=tz.now)
    published_date = models.DateTimeField(default=tz.now)
    modified_date = models.DateTimeField()
    n_comments = models.IntegerField(default=10, blank=True, null=True)
    n_pingback = models.IntegerField(default=10, blank=True, null=True)
    rating = models.IntegerField()


    objects = PostManager()

    def get_comments(self):
        return self.comment_set.all()

    def n_comments(self):
        return self.comment_set.count()


    def __str__(self):
        return self.title




class CommentManager(models.Manager):

    def get_comment_by_id(self, id):
        pass

    def get_last_comments(self, quant=5):
        pass






class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField()

    def add(self, post, author, text, date=tz.now()):
        self.post = post
        self.author = author
        self.text = text
        self.created_date = date

        self.save()

    objects = CommentManager()


    def __str__(self):
        return self.post.title










class MyUser(AbstractUser):


    def auth(self, User):
        pass



# class Blog(models.Model):
#     name = models.CharField(max_length=200)
#     tagline = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=200)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField(default=timezone.now)
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField(default=10)
#     n_pingback = models.IntegerField(default=10)
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.headline



