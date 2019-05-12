# Generated by Django 2.2 on 2019-04-21 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacePath',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=30, verbose_name='图片路径')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faces', to='sign.Student', verbose_name='所属学生')),
            ],
            options={
                'verbose_name': '照片路径',
                'verbose_name_plural': '照片路径',
                'ordering': ['-create_time'],
            },
        ),
        migrations.DeleteModel(
            name='FaceUrl',
        ),
    ]
