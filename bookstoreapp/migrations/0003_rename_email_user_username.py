# Generated by Django 4.2.3 on 2023-07-15 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapp', '0002_rename_book_id_book_id_rename_comment_id_comment_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='username',
        ),
    ]
