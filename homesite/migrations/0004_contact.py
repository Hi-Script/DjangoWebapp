# Generated by Django 4.1.2 on 2023-02-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0003_alter_review_options_review_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=b'I01\n')),
                ('email', models.EmailField(max_length=100, null=b'I01\n')),
                ('message', models.TextField(null=b'I01\n')),
                ('created', models.DateTimeField(auto_now_add=True, null=b'I01\n')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
