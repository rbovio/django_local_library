# Generated by Django 4.2.4 on 2023-08-29 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_view_all_books_borrowed', 'Can view all books borrowed'), ('can_mark_returned', 'Can mark returned'))},
        ),
    ]