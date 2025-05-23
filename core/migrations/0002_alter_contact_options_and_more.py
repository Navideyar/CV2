# Generated by Django 5.1.7 on 2025-03-29 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='pub_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='author',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='بدون موضوع', max_length=250),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
