# Generated by Django 3.0.5 on 2020-04-25 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=30, verbose_name='Name_of_article')),
                ('article_text', models.TextField(verbose_name='Text_of_article')),
                ('publishing_date', models.DateTimeField(verbose_name='Date_of_publishing')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30, verbose_name='Name_of_author')),
                ('comment_text', models.CharField(max_length=500, verbose_name='Comment_text')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]