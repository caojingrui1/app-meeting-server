# Generated by Django 2.2.5 on 2020-08-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=128, verbose_name='昵称')),
                ('avatar', models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='用户头像')),
                ('gender', models.CharField(choices=[(1, '男'), (2, '女')], default=1, max_length=6, verbose_name='性别')),
                ('openid', models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='openid')),
                ('unionid', models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='uninon')),
                ('is_admin', models.SmallIntegerField(choices=[(1, '是'), (0, '否')], default=0, verbose_name='是否管理员')),
                ('is_maintainer', models.SmallIntegerField(choices=[(1, '是'), (0, '否')], default=0, verbose_name='是否维护者')),
                ('signature', models.CharField(blank=True, max_length=255, null=True, verbose_name='个性签名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_login_time', models.DateTimeField(auto_now=True, verbose_name='最近登陆时间')),
            ],
        ),
        migrations.AlterField(
            model_name='meetingitem',
            name='type',
            field=models.SmallIntegerField(choices=[(2, '预定会议'), (1, '紧急会议')], default=2, null=True, verbose_name='会议类型'),
        ),
    ]
