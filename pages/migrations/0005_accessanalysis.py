# Generated by Django 2.0 on 2019-05-07 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular', models.BooleanField(default=False, verbose_name='是否是回头客')),
                ('uid', models.CharField(max_length=32, verbose_name='访问者ID')),
                ('method', models.CharField(max_length=16, verbose_name='HTTP方法')),
                ('url', models.TextField(verbose_name='访问的URL')),
                ('referer', models.TextField(blank=True, default=None, null=True, verbose_name='访问来源页面URL')),
                ('remote_addr', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='访问者网络地址')),
                ('x_real_ip', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='访问者真实IP')),
                ('x_forwarded_for', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='访问者反向代理地址')),
                ('accept_language', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='访问者语言')),
                ('host', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='访问的站点主机')),
                ('remote_host', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='访问者主机')),
                ('remote_user', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='访问者用户')),
                ('user_agent', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='访问者User-Agent标识')),
                ('x_requested_with', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='XHR标识')),
                ('dt_str', models.CharField(blank=True, default=None, max_length=26, null=True, verbose_name='访问时间(字符串)')),
                ('access_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='访问时间')),
            ],
            options={
                'verbose_name': '站点访问统计',
                'verbose_name_plural': '站点访问统计',
            },
        ),
    ]
