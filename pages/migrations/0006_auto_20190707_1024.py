# Generated by Django 2.0 on 2019-07-07 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_accessanalysis'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '工具分类关联',
                'verbose_name_plural': '工具分类关联',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='工具名')),
                ('cover', models.TextField(blank=True, default=None, null=True, verbose_name='封面')),
                ('cover_type', models.CharField(blank=True, choices=[('LINK', ''), ('TEXT', '')], default=None, max_length=55, null=True, verbose_name='封面类型')),
                ('intro', models.TextField(blank=True, default=None, null=True, verbose_name='简介')),
                ('detail', models.TextField(blank=True, default=None, null=True, verbose_name='详细(使用)介绍')),
                ('index', models.IntegerField(default=1, verbose_name='排序索引')),
                ('display', models.BooleanField(default=True, verbose_name='是否显示')),
            ],
            options={
                'verbose_name': '工具',
                'verbose_name_plural': '工具',
            },
        ),
        migrations.CreateModel(
            name='ToolCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='分类名')),
                ('index', models.IntegerField(default=1, verbose_name='排序索引')),
                ('display', models.BooleanField(default=True, verbose_name='是否显示')),
                ('tools', models.ManyToManyField(through='pages.CategoryTools', to='pages.Tool')),
            ],
            options={
                'verbose_name': '工具分类',
                'verbose_name_plural': '工具分类',
            },
        ),
        migrations.AddField(
            model_name='categorytools',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.ToolCategory'),
        ),
        migrations.AddField(
            model_name='categorytools',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Tool'),
        ),
    ]