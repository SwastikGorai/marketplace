# Generated by Django 4.1.7 on 2023-04-13 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='message',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='conversationmessage',
            name='sender',
        ),
    ]