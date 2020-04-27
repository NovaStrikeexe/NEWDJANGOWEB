from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Name_of_article', max_length=30)
    article_text = models.TextField('Text_of_article')
    publishing_date = models.DateTimeField('Date_of_publishing')

    def __str__(self):
        return self.article_title

    def was_published_in_two_days(self):
        return self.publishing_date >= (timezone.now() - datetime.timedelta(days=2))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Name_of_author', max_length=30)
    comment_text = models.CharField('Comment_text', max_length=500)

    def __str__(self):
        return self.author_name
