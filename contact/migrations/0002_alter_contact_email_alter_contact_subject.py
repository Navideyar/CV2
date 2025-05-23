# Generated by Django 5.1.7 on 2025-04-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="subject",
            field=models.CharField(
                blank=True, default="بدون موضوع", max_length=250, null=True
            ),
        ),
    ]
