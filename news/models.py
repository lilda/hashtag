from django.db import models
from django.conf import settings
from django.urls.base import reverse
from django.contrib.auth.models import User
import re

# Create your models here.
class Tag(models.Model):
    tag=models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.tag

class News(models.Model):
    
    title=models.CharField(max_length=30)
    content=models.TextField()
    time=models.DateTimeField()
    photo=models.ImageField(upload_to="images/", blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', blank=True)
        
    def __str__ (self):
        return self.title +" - "+ self.content

    def summary(self):
        return self.content[:50]
        
    def get_absolute_url(self):
        return reverse('detail',args=[self.id])  
        
        # NOTE: content에서 tags를 추출하여, Tag 객체 가져오기, 신규 태그는 Tag instance 생성, 본인의 tag_set에 등록,
    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.content)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가
        
class Comment(models.Model):
    news=models.ForeignKey(News, on_delete=models.CASCADE)
    content=models.TextField()
    time=models.DateTimeField()
    photo=models.ImageField(upload_to="images/", blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__ (self):
        return self.content

class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    news=models.ForeignKey(News, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Hashtag(models.Model):
    news=models.ForeignKey(News, on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag, on_delete=models.PROTECT)
