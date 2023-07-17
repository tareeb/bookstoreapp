# Generated by Django 4.2.3 on 2023-07-17 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapp', '0007_book_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('delivery', 'Delivery'), ('received', 'Received')], default='pending', max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstoreapp.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstoreapp.user')),
            ],
        ),
    ]