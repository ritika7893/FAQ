# Generated by Django 5.0.2 on 2025-02-01 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='question_bn',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_hi',
        ),
    ]
