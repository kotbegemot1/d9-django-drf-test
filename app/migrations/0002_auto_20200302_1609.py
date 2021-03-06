# Generated by Django 3.0.3 on 2020-03-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categorys',
            field=models.ManyToManyField(blank=True, related_name='posts', to='app.Category'),
        ),
    ]
